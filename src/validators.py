"""Validation system for generated infrastructure code"""

import yaml
import re
from typing import Dict, List, Tuple


class ValidationResult:
    """Container for validation results"""
    
    def __init__(self):
        self.valid = True
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []
    
    def add_error(self, message: str):
        """Add an error message"""
        self.valid = False
        self.errors.append(message)
    
    def add_warning(self, message: str):
        """Add a warning message"""
        self.warnings.append(message)
    
    def add_suggestion(self, message: str):
        """Add a suggestion"""
        self.suggestions.append(message)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "valid": self.valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "suggestions": self.suggestions,
        }


def validate_yaml_syntax(content: str) -> ValidationResult:
    """
    Validate YAML syntax
    
    Args:
        content: YAML content as string
    
    Returns:
        ValidationResult: Validation results
    """
    result = ValidationResult()
    
    try:
        yaml.safe_load(content)
    except yaml.YAMLError as e:
        result.add_error(f"YAML syntax error: {str(e)}")
    
    return result


def validate_kubernetes_manifest(content: str) -> ValidationResult:
    """
    Validate Kubernetes manifest structure
    
    Args:
        content: YAML content as string
    
    Returns:
        ValidationResult: Validation results
    """
    result = validate_yaml_syntax(content)
    
    if not result.valid:
        return result
    
    try:
        manifest = yaml.safe_load(content)
        
        # Check required fields
        if "apiVersion" not in manifest:
            result.add_error("Missing required field: apiVersion")
        
        if "kind" not in manifest:
            result.add_error("Missing required field: kind")
        
        if "metadata" not in manifest:
            result.add_error("Missing required field: metadata")
        
        # Check metadata
        if "metadata" in manifest:
            if "name" not in manifest["metadata"]:
                result.add_error("Missing required field: metadata.name")
        
        # Kind-specific validation
        kind = manifest.get("kind", "")
        
        if kind == "Deployment":
            if "spec" not in manifest:
                result.add_error("Deployment missing spec field")
            elif "replicas" not in manifest["spec"]:
                result.add_warning("Deployment spec missing replicas (will default to 1)")
            
            # Check for security context
            if "spec" in manifest and "template" in manifest["spec"]:
                template_spec = manifest["spec"]["template"].get("spec", {})
                if "securityContext" not in template_spec:
                    result.add_suggestion("Consider adding securityContext for pod security")
        
        elif kind == "Service":
            if "spec" not in manifest:
                result.add_error("Service missing spec field")
            elif "ports" not in manifest["spec"]:
                result.add_error("Service spec missing ports")
    
    except Exception as e:
        result.add_error(f"Validation error: {str(e)}")
    
    return result


def validate_terraform_syntax(content: str) -> ValidationResult:
    """
    Basic Terraform syntax validation
    
    Args:
        content: Terraform content as string
    
    Returns:
        ValidationResult: Validation results
    """
    result = ValidationResult()
    
    # Check for basic HCL structure
    if not content.strip():
        result.add_error("Empty Terraform file")
        return result
    
    # Check for balanced braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    
    if open_braces != close_braces:
        result.add_error(f"Unbalanced braces: {open_braces} opening, {close_braces} closing")
    
    # Check for provider block
    if 'provider "' not in content:
        result.add_warning("No provider block found")
    
    # Check for terraform block
    if 'terraform {' not in content:
        result.add_suggestion("Consider adding terraform block with required_version")
    
    return result


def validate_dockerfile(content: str) -> ValidationResult:
    """
    Validate Dockerfile
    
    Args:
        content: Dockerfile content as string
    
    Returns:
        ValidationResult: Validation results
    """
    result = ValidationResult()
    
    lines = content.strip().split('\n')
    
    # Check for FROM instruction
    has_from = False
    for line in lines:
        if line.strip().startswith('FROM'):
            has_from = True
            break
    
    if not has_from:
        result.add_error("Dockerfile must start with FROM instruction")
    
    # Check for WORKDIR
    if 'WORKDIR' not in content:
        result.add_suggestion("Consider using WORKDIR to set working directory")
    
    # Check for USER (security best practice)
    if 'USER' not in content:
        result.add_suggestion("Consider adding USER instruction to run as non-root")
    
    # Check for COPY before RUN (layer caching)
    copy_index = -1
    run_index = -1
    
    for i, line in enumerate(lines):
        if line.strip().startswith('COPY'):
            copy_index = i
        elif line.strip().startswith('RUN') and run_index == -1:
            run_index = i
    
    if copy_index > -1 and run_index > -1 and copy_index > run_index:
        result.add_suggestion("Consider copying dependency files before RUN for better layer caching")
    
    return result


def validate_generated_code(content: str, code_type: str) -> ValidationResult:
    """
    Main validation function that routes to specific validators
    
    Args:
        content: Code content as string
        code_type: Type of code (kubernetes, terraform, docker)
    
    Returns:
        ValidationResult: Validation results
    """
    validators = {
        "kubernetes": validate_kubernetes_manifest,
        "terraform": validate_terraform_syntax,
        "docker": validate_dockerfile,
    }
    
    validator = validators.get(code_type, validate_yaml_syntax)
    return validator(content)

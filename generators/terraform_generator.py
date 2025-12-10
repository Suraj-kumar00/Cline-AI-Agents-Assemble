"""Terraform Code Generator"""

import os
import re
from typing import Dict
from src.gemini_client import GeminiClient
from src.validators import validate_terraform_syntax


class TerraformGenerator:
    """Generator for Terraform infrastructure code"""
    
    def __init__(self):
        """Initialize Terraform generator"""
        self.client = GeminiClient()
    
    def generate(self, requirements: str) -> Dict[str, str]:
        """
        Generate Terraform code
        
        Args:
            requirements: Natural language requirements
        
        Returns:
            Dict mapping filename to content
        """
        print("🚀 Generating Terraform code...")
        
        # Generate using AI
        raw_output = self.client.generate_terraform_code(requirements)
        
        # Parse output into separate files
        tf_files = self._parse_output(raw_output)
        
        # Validate
        print("\n✅ Validating generated Terraform code...")
        for filename, content in tf_files.items():
            result = validate_terraform_syntax(content)
            
            if not result.valid:
                print(f"\n⚠️  Validation errors in {filename}:")
                for error in result.errors:
                    print(f"   ❌ {error}")
            
            if result.warnings:
                print(f"\n⚠️  Warnings for {filename}:")
                for warning in result.warnings:
                    print(f"   ⚠️  {warning}")
        
        return tf_files
    
    def _parse_output(self, output: str) -> Dict[str, str]:
        """
        Parse AI output into separate Terraform files
        
        Args:
            output: Raw output from AI
        
        Returns:
            Dict mapping filename to content
        """
        tf_files = {}
        
        # Split by file markers
        file_pattern = r'---\s*\n#\s*FILE:\s*(\S+)\s*\n'
        splits = re.split(file_pattern, output)
        
        # Process splits
        for i in range(1, len(splits), 2):
            if i + 1 < len(splits):
                filename = splits[i].strip()
                content = splits[i + 1].strip()
                
                # Clean up formatting
                content = content.replace('```hcl', '').replace('```terraform', '').replace('```', '').strip()
                
                tf_files[filename] = content
        
        # If no file markers, create default files
        if not tf_files:
            output = output.replace('```hcl', '').replace('```terraform', '').replace('```', '').strip()
            tf_files['main.tf'] = output
        
        return tf_files
    
    def save_outputs(self, tf_files: Dict[str, str], output_dir: str):
        """
        Save generated Terraform files
        
        Args:
            tf_files: Dict mapping filename to content
            output_dir: Output directory path
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for filename, content in tf_files.items():
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(content)
            
            print(f"✅ Generated: {filepath}")

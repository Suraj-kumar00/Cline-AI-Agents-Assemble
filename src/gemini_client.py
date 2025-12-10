"""AI client for infrastructure code generation using Gemini 3 Pro"""

import google.generativeai as genai
from typing import Optional
from src.config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_MAX_TOKENS


class GeminiClient:
    """Client for interacting with Gemini AI"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize AI client
        
        Args:
            api_key: Optional API key (uses config if not provided)
        """
        self.api_key = api_key or GEMINI_API_KEY
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is required. Set it in .env file or pass it directly.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
    
    def generate_kubernetes_yaml(self, requirements: str) -> str:
        """
        Generate Kubernetes YAML manifests
        
        Args:
            requirements: Natural language requirements for the Kubernetes deployment
        
        Returns:
            str: Generated YAML content
        """
        prompt = f"""You are an expert Kubernetes architect and DevOps engineer.

Generate PRODUCTION-READY Kubernetes YAML manifests based on these requirements:
{requirements}

CRITICAL INSTRUCTIONS:
1. Generate COMPLETE, working YAML (not snippets or examples)
2. Include EVERY required field for production use
3. Add inline comments with links to official Kubernetes documentation
4. Every major field MUST reference the official docs: https://kubernetes.io/docs/...
5. Implement security best practices:
   - runAsNonRoot: true
   - readOnlyRootFilesystem: true (where applicable)
   - allowPrivilegeEscalation: false
   - Drop unnecessary capabilities
   - Resource limits enforced
6. Include health checks (liveness + readiness probes)
7. Use exact field names from official Kubernetes API spec
8. Make code production-ready (no "change-me" placeholders)
9. Include proper labels and selectors
10. Add resource requests and limits

Generate these files in order:
1. deployment.yaml - Complete Deployment manifest
2. service.yaml - Service for networking
3. configmap.yaml - ConfigMap for configuration

Separate each file with:
---
# FILE: filename.yaml

Include documentation comments above each major field explaining what it does and linking to official Kubernetes docs.
"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_terraform_code(self, requirements: str) -> str:
        """
        Generate Terraform infrastructure code
        
        Args:
            requirements: Natural language requirements for infrastructure
        
        Returns:
            str: Generated Terraform code
        """
        prompt = f"""You are an expert Terraform architect specializing in AWS infrastructure.

Generate PRODUCTION-READY Terraform code based on these requirements:
{requirements}

CRITICAL INSTRUCTIONS:
1. Generate complete Terraform code (not snippets)
2. Include proper provider configuration
3. Add inline comments with links to Terraform Registry docs
4. Every resource MUST reference official docs: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/...
5. Implement security best practices:
   - Use VPC with private subnets
   - Enable encryption at rest
   - Proper security group rules
   - Enable logging where applicable
6. Use exact field names from official AWS provider docs
7. Make code production-ready
8. Include proper resource dependencies
9. Use variables for configurable values

Generate these files in order:
1. main.tf - Main infrastructure resources
2. variables.tf - Input variables
3. outputs.tf - Output values

Separate each file with:
---
# FILE: filename.tf

Include documentation comments explaining each resource and linking to official Terraform documentation.
"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_dockerfile(self, requirements: str) -> str:
        """
        Generate optimized Dockerfile
        
        Args:
            requirements: Natural language requirements for Docker image
        
        Returns:
            str: Generated Dockerfile
        """
        prompt = f"""You are an expert Docker architect.

Generate a PRODUCTION-READY, optimized Dockerfile based on these requirements:
{requirements}

CRITICAL INSTRUCTIONS:
1. Use multi-stage builds for optimization
2. Include comments with links to Docker documentation
3. Every instruction MUST have a comment explaining why it's there
4. Reference official docs: https://docs.docker.com/...
5. Implement security best practices:
   - Use specific version tags (not 'latest')
   - Run as non-root user
   - Use minimal base image (alpine/slim variants)
   - Don't include unnecessary packages
6. Optimize for layer caching:
   - Copy dependency files first
   - Copy source code last
7. Use .dockerignore patterns
8. Include HEALTHCHECK if applicable
9. Proper ENTRYPOINT and CMD usage

Generate a complete Dockerfile with detailed comments explaining each instruction and linking to official Docker documentation.
"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_cicd_pipeline(self, requirements: str, platform: str = "github") -> str:
        """
        Generate CI/CD pipeline configuration
        
        Args:
            requirements: Natural language requirements
            platform: CI/CD platform (github, gitlab)
        
        Returns:
            str: Generated pipeline configuration
        """
        platform_config = {
            "github": {
                "file": ".github/workflows/deploy.yml",
                "docs": "https://docs.github.com/en/actions"
            },
            "gitlab": {
                "file": ".gitlab-ci.yml",
                "docs": "https://docs.gitlab.com/ee/ci/"
            }
        }
        
        config = platform_config.get(platform, platform_config["github"])
        
        prompt = f"""You are an expert DevOps engineer specializing in CI/CD pipelines.

Generate a PRODUCTION-READY {platform.upper()} CI/CD pipeline based on these requirements:
{requirements}

CRITICAL INSTRUCTIONS:
1. Generate complete pipeline configuration (not snippets)
2. Include inline comments with links to official {platform} docs
3. Reference: {config['docs']}
4. Implement best practices:
   - Proper job dependencies
   - Caching where applicable
   - Secrets management
   - Parallel execution where possible
5. Include typical stages:
   - Build
   - Test
   - Deploy
6. Use specific action/image versions
7. Add proper error handling

Generate a complete pipeline configuration with detailed comments linking to official documentation.
"""
        
        response = self.model.generate_content(prompt)
        return response.text


# Convenience functions
def generate_k8s_yaml(requirements: str) -> str:
    """Generate Kubernetes YAML (convenience function)"""
    client = GeminiClient()
    return client.generate_kubernetes_yaml(requirements)


def generate_terraform(requirements: str) -> str:
    """Generate Terraform code (convenience function)"""
    client = GeminiClient()
    return client.generate_terraform_code(requirements)


def generate_dockerfile(requirements: str) -> str:
    """Generate Dockerfile (convenience function)"""
    client = GeminiClient()
    return client.generate_dockerfile(requirements)


def generate_cicd(requirements: str, platform: str = "github") -> str:
    """Generate CI/CD pipeline (convenience function)"""
    client = GeminiClient()
    return client.generate_cicd_pipeline(requirements, platform)

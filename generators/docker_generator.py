"""Dockerfile Generator"""

import os
from src.gemini_client import GeminiClient
from src.validators import validate_dockerfile


class DockerGenerator:
    """Generator for optimized Dockerfiles"""
    
    def __init__(self):
        """Initialize Docker generator"""
        self.client = GeminiClient()
    
    def generate(self, requirements: str) -> str:
        """
        Generate Dockerfile
        
        Args:
            requirements: Natural language requirements
        
        Returns:
            str: Generated Dockerfile content
        """
        print("🚀 Generating Dockerfile...")
        
        # Generate using AI
        dockerfile = self.client.generate_dockerfile(requirements)
        
        # Clean up formatting
        dockerfile = dockerfile.replace('```dockerfile', '').replace('```', '').strip()
        
        # Validate
        print("\n✅ Validating generated Dockerfile...")
        result = validate_dockerfile(dockerfile)
        
        if not result.valid:
            print("\n⚠️  Validation errors:")
            for error in result.errors:
                print(f"   ❌ {error}")
        
        if result.warnings:
            print("\n⚠️  Warnings:")
            for warning in result.warnings:
                print(f"   ⚠️  {warning}")
        
        if result.suggestions:
            print("\n💡 Suggestions:")
            for suggestion in result.suggestions:
                print(f"   💡 {suggestion}")
        
        return dockerfile
    
    def save_output(self, dockerfile: str, output_dir: str):
        """
        Save generated Dockerfile
        
        Args:
            dockerfile: Dockerfile content
            output_dir: Output directory path
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, "Dockerfile")
        
        with open(filepath, 'w') as f:
            f.write(dockerfile)
        
        print(f"✅ Generated: {filepath}")
        
        # Also generate .dockerignore
        dockerignore = """# Git
.git
.gitignore

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info
venv/
.venv/
.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Docs
*.md
!README.md

# Build
dist/
build/
"""
        
        dockerignore_path = os.path.join(output_dir, ".dockerignore")
        with open(dockerignore_path, 'w') as f:
            f.write(dockerignore)
        
        print(f"✅ Generated: {dockerignore_path}")

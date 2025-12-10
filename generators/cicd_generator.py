"""CI/CD Pipeline Generator"""

import os
import re
from typing import Dict
from src.gemini_client import GeminiClient


class CICDGenerator:
    """Generator for CI/CD pipeline configurations"""
    
    def __init__(self):
        """Initialize CI/CD generator"""
        self.client = GeminiClient()
    
    def generate(self, requirements: str, platform: str = "github") -> str:
        """
        Generate CI/CD pipeline configuration
        
        Args:
            requirements: Natural language requirements
            platform: CI/CD platform (github, gitlab)
        
        Returns:
            str: Generated pipeline configuration
        """
        print(f"🚀 Generating {platform.upper()} CI/CD pipeline...")
        
        # Generate using AI
        pipeline = self.client.generate_cicd_pipeline(requirements, platform)
        
        # Clean up formatting
        pipeline = pipeline.replace('```yaml', '').replace('```', '').strip()
        
        return pipeline
    
    def save_output(self, pipeline: str, output_dir: str, platform: str = "github"):
        """
        Save generated CI/CD pipeline
        
        Args:
            pipeline: Pipeline configuration content
            output_dir: Output directory path
            platform: CI/CD platform
        """
        if platform == "github":
            # Create .github/workflows directory
            workflows_dir = os.path.join(output_dir, ".github", "workflows")
            os.makedirs(workflows_dir, exist_ok=True)
            filepath = os.path.join(workflows_dir, "deploy.yml")
        elif platform == "gitlab":
            filepath = os.path.join(output_dir, ".gitlab-ci.yml")
            os.makedirs(output_dir, exist_ok=True)
        else:
            filepath = os.path.join(output_dir, "pipeline.yml")
            os.makedirs(output_dir, exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(pipeline)
        
        print(f"✅ Generated: {filepath}")

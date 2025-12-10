"""Kubernetes YAML Generator"""

import os
import re
from typing import Dict, List
from src.gemini_client import GeminiClient
from src.validators import validate_kubernetes_manifest


class K8sGenerator:
    """Generator for Kubernetes manifests"""
    
    def __init__(self):
        """Initialize Kubernetes generator"""
        self.client = GeminiClient()
    
    def generate(self, requirements: str) -> Dict[str, str]:
        """
        Generate Kubernetes manifests
        
        Args:
            requirements: Natural language requirements
        
        Returns:
            Dict mapping filename to content
        """
        print("🚀 Generating Kubernetes manifests...")
        
        # Generate YAML using AI
        raw_output = self.client.generate_kubernetes_yaml(requirements)
        
        # Parse output into separate files
        manifests = self._parse_output(raw_output)
        
        # Validate each manifest
        print("\n✅ Validating generated manifests...")
        for filename, content in manifests.items():
            result = validate_kubernetes_manifest(content)
            
            if not result.valid:
                print(f"\n⚠️  Validation errors in {filename}:")
                for error in result.errors:
                    print(f"   ❌ {error}")
            
            if result.warnings:
                print(f"\n⚠️  Warnings for {filename}:")
                for warning in result.warnings:
                    print(f"   ⚠️  {warning}")
        
        return manifests
    
    def _parse_output(self, output: str) -> Dict[str, str]:
        """
        Parse AI output into separate YAML files
        
        Args:
            output: Raw output from AI
        
        Returns:
            Dict mapping filename to content
        """
        manifests = {}
        
        # Split by file markers
        file_pattern = r'---\s*\n#\s*FILE:\s*(\S+)\s*\n'
        splits = re.split(file_pattern, output)
        
        # Process splits (pattern: [prefix, filename1, content1, filename2, content2, ...])
        for i in range(1, len(splits), 2):
            if i + 1 < len(splits):
                filename = splits[i].strip()
                content = splits[i + 1].strip()
                
                # Clean up common formatting
                content = content.replace('```yaml', '').replace('```', '').strip()
                
                manifests[filename] = content
        
        # If no file markers found, try to split by document separator
        if not manifests:
            docs = [doc.strip() for doc in output.split('---') if doc.strip()]
            
            for i, doc in enumerate(docs):
                # Try to determine filename from kind
                try:
                    # Remove markdown code blocks if present
                    doc = doc.replace('```yaml', '').replace('```', '').strip()
                    
                    # Extract kind
                    kind_match = re.search(r'kind:\s*(\w+)', doc)
                    if kind_match:
                        kind = kind_match.group(1).lower()
                        filename = f"{kind}.yaml"
                        manifests[filename] = doc
                    else:
                        manifests[f"manifest-{i+1}.yaml"] = doc
                except:
                    manifests[f"manifest-{i+1}.yaml"] = doc
        
        return manifests
    
    def save_outputs(self, manifests: Dict[str, str], output_dir: str):
        """
        Save generated manifests to files
        
        Args:
            manifests: Dict mapping filename to content
            output_dir: Output directory path
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for filename, content in manifests.items():
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(content)
            
            print(f"✅ Generated: {filepath}")

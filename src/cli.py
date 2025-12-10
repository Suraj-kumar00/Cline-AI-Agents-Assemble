#!/usr/bin/env python3
"""InfraAgent CLI - Infrastructure Code Generation Tool

Powered by Cline - AI Agents Assemble Hackathon
Built with Gemini 3 Pro Preview
"""

import click
import os
from generators.k8s_generator import K8sGenerator
from generators.terraform_generator import TerraformGenerator
from generators.docker_generator import DockerGenerator
from generators.cicd_generator import CICDGenerator
from generators.documentation_generator import DocumentationGenerator
from src.config import OUTPUT_DIR


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    🚀 InfraAgent - Infrastructure Code Generation Tool
    
    Generate production-ready infrastructure code using AI.
    
    Powered by Cline - AI Agents Assemble Hackathon
    """
    pass


@cli.command(name="generate-k8s")
@click.option('--app', required=True, help='Application type (e.g., flask, django, nodejs)')
@click.option('--replicas', default=3, help='Number of replicas')
@click.option('--port', default=8080, help='Container port')
@click.option('--memory', default='512Mi', help='Memory limit')
@click.option('--cpu', default='250m', help='CPU limit')
@click.option('--output', default=OUTPUT_DIR, help='Output directory')
def generate_k8s(app, replicas, port, memory, cpu, output):
    """
    Generate Kubernetes manifests (Deployment, Service, ConfigMap)
    
    Example:
        infraagent generate-k8s --app flask --replicas 3 --port 8080
    """
    click.echo("=" * 60)
    click.echo("🚀 InfraAgent - Kubernetes Generator")
    click.echo("=" * 60)
    
    requirements = f"""
    Generate Kubernetes deployment for:
    - Application type: {app}
    - Number of replicas: {replicas}
    - Container port: {port}
    - Memory limit: {memory}
    - CPU limit: {cpu}
    
    Requirements:
    - Include LoadBalancer Service for external access
    - Add ConfigMap for environment variables
    - Implement health checks (liveness and readiness probes)
    - Apply security best practices (non-root user, read-only filesystem)
    - Add resource requests and limits
    - Include proper labels and selectors
    """
    
    try:
        # Generate manifests
        generator = K8sGenerator()
        manifests = generator.generate(requirements)
        
        # Save outputs
        generator.save_outputs(manifests, output)
        
        # Generate implementation guide
        doc_gen = DocumentationGenerator()
        guide = doc_gen.generate_implementation_guide("kubernetes", manifests, requirements)
        doc_gen.save_guide(guide, output)
        
        click.echo("\n" + "=" * 60)
        click.echo("✅ SUCCESS! Kubernetes manifests generated")
        click.echo("=" * 60)
        click.echo(f"\n📁 Output directory: {output}")
        click.echo("\nGenerated files:")
        for filename in manifests.keys():
            click.echo(f"  - {filename}")
        click.echo("  - IMPLEMENTATION_GUIDE.md")
        click.echo("\n💡 Next steps:")
        click.echo("  1. Review the generated files")
        click.echo(f"  2. kubectl apply -f {output}/")
        click.echo("  3. Check IMPLEMENTATION_GUIDE.md for detailed instructions")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {str(e)}", err=True)
        raise click.Abort()


@cli.command(name="generate-terraform")
@click.option('--cloud', default='aws', help='Cloud provider (aws, azure, gcp)')
@click.option('--service', default='vpc', help='Service to deploy (vpc, rds, eks, etc.)')
@click.option('--region', default='us-east-1', help='Cloud region')
@click.option('--output', default=OUTPUT_DIR, help='Output directory')
def generate_terraform(cloud, service, region, output):
    """
    Generate Terraform infrastructure code
    
    Example:
        infraagent generate-terraform --cloud aws --service vpc
    """
    click.echo("=" * 60)
    click.echo("🚀 InfraAgent - Terraform Generator")
    click.echo("=" * 60)
    
    requirements = f"""
    Generate Terraform code for {cloud.upper()} infrastructure:
    - Cloud provider: {cloud}
    - Service: {service}
    - Region: {region}
    
    Requirements:
    - Create VPC with public and private subnets
    - Set up Internet Gateway and NAT Gateway
    - Configure security groups with least privilege
    - Enable encryption at rest
    - Include proper tagging
    - Use variables for configurable values
    - Add outputs for important resource IDs
    """
    
    try:
        # Generate Terraform code
        generator = TerraformGenerator()
        tf_files = generator.generate(requirements)
        
        # Save outputs
        generator.save_outputs(tf_files, output)
        
        # Generate implementation guide
        doc_gen = DocumentationGenerator()
        guide = doc_gen.generate_implementation_guide("terraform", tf_files, requirements)
        doc_gen.save_guide(guide, output)
        
        click.echo("\n" + "=" * 60)
        click.echo("✅ SUCCESS! Terraform code generated")
        click.echo("=" * 60)
        click.echo(f"\n📁 Output directory: {output}")
        click.echo("\nGenerated files:")
        for filename in tf_files.keys():
            click.echo(f"  - {filename}")
        click.echo("  - IMPLEMENTATION_GUIDE.md")
        click.echo("\n💡 Next steps:")
        click.echo("  1. Review the generated files")
        click.echo(f"  2. cd {output}")
        click.echo("  3. terraform init")
        click.echo("  4. terraform plan")
        click.echo("  5. terraform apply")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {str(e)}", err=True)
        raise click.Abort()


@cli.command(name="generate-docker")
@click.option('--app', required=True, help='Application type (python, nodejs, java, go)')
@click.option('--base-image', default=None, help='Base image (e.g., python:3.11-slim)')
@click.option('--port', default=8080, help='Exposed port')
@click.option('--output', default=OUTPUT_DIR, help='Output directory')
def generate_docker(app, base_image, port, output):
    """
    Generate optimized Dockerfile with multi-stage builds
    
    Example:
        infraagent generate-docker --app python --port 8080
    """
    click.echo("=" * 60)
    click.echo("🚀 InfraAgent - Dockerfile Generator")
    click.echo("=" * 60)
    
    base_image_instruction = f"Using base image: {base_image}" if base_image else ""
    
    requirements = f"""
    Generate optimized Dockerfile for {app} application:
    - Application type: {app}
    {base_image_instruction}
    - Exposed port: {port}
    
    Requirements:
    - Use multi-stage build for optimization
    - Run as non-root user
    - Use minimal base image (alpine or slim variants)
    - Implement layer caching best practices
    - Add HEALTHCHECK
    - Include security best practices
    - Optimize for small image size
    """
    
    try:
        # Generate Dockerfile
        generator = DockerGenerator()
        dockerfile = generator.generate(requirements)
        
        # Save output
        generator.save_output(dockerfile, output)
        
        # Generate implementation guide
        doc_gen = DocumentationGenerator()
        guide = doc_gen.generate_implementation_guide("docker", {"Dockerfile": dockerfile}, requirements)
        doc_gen.save_guide(guide, output)
        
        click.echo("\n" + "=" * 60)
        click.echo("✅ SUCCESS! Dockerfile generated")
        click.echo("=" * 60)
        click.echo(f"\n📁 Output directory: {output}")
        click.echo("\nGenerated files:")
        click.echo("  - Dockerfile")
        click.echo("  - .dockerignore")
        click.echo("  - IMPLEMENTATION_GUIDE.md")
        click.echo("\n💡 Next steps:")
        click.echo("  1. Review the generated Dockerfile")
        click.echo(f"  2. docker build -t my-app:latest {output}")
        click.echo("  3. docker run -p 8080:8080 my-app:latest")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {str(e)}", err=True)
        raise click.Abort()


@cli.command(name="generate-cicd")
@click.option('--platform', type=click.Choice(['github', 'gitlab']), default='github', help='CI/CD platform')
@click.option('--deploy-target', default='kubernetes', help='Deployment target (kubernetes, aws, docker)')
@click.option('--output', default=OUTPUT_DIR, help='Output directory')
def generate_cicd(platform, deploy_target, output):
    """
    Generate CI/CD pipeline configuration
    
    Example:
        infraagent generate-cicd --platform github --deploy-target kubernetes
    """
    click.echo("=" * 60)
    click.echo(f"🚀 InfraAgent - {platform.upper()} CI/CD Generator")
    click.echo("=" * 60)
    
    requirements = f"""
    Generate {platform.upper()} CI/CD pipeline for:
    - Platform: {platform}
    - Deployment target: {deploy_target}
    
    Requirements:
    - Build stage: Build and test application
    - Docker stage: Build and push Docker image
    - Deploy stage: Deploy to {deploy_target}
    - Include caching for dependencies
    - Add proper secrets management
    - Implement parallel execution where possible
    - Add status badges
    """
    
    try:
        # Generate CI/CD pipeline
        generator = CICDGenerator()
        pipeline = generator.generate(requirements, platform)
        
        # Save output
        generator.save_output(pipeline, output, platform)
        
        # Generate implementation guide
        doc_gen = DocumentationGenerator()
        guide = doc_gen.generate_implementation_guide("cicd", {f"{platform}-pipeline": pipeline}, requirements)
        doc_gen.save_guide(guide, output)
        
        click.echo("\n" + "=" * 60)
        click.echo("✅ SUCCESS! CI/CD pipeline generated")
        click.echo("=" * 60)
        click.echo(f"\n📁 Output directory: {output}")
        click.echo("\nGenerated files:")
        if platform == "github":
            click.echo("  - .github/workflows/deploy.yml")
        else:
            click.echo("  - .gitlab-ci.yml")
        click.echo("  - IMPLEMENTATION_GUIDE.md")
        click.echo("\n💡 Next steps:")
        click.echo("  1. Review the generated pipeline")
        click.echo("  2. Configure required secrets in your repository")
        click.echo("  3. Commit and push to trigger the pipeline")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {str(e)}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    cli()

"""Documentation Generator for Implementation Guides"""

import os
from typing import Dict


class DocumentationGenerator:
    """Generator for implementation guides and documentation"""
    
    def generate_implementation_guide(
        self, 
        infra_type: str, 
        generated_files: Dict[str, str],
        requirements: str
    ) -> str:
        """
        Generate comprehensive implementation guide
        
        Args:
            infra_type: Type of infrastructure (kubernetes, terraform, docker, cicd)
            generated_files: Dict of generated files
            requirements: Original requirements
        
        Returns:
            str: Implementation guide content
        """
        guide = f"""# Implementation Guide: {infra_type.title()}

## Overview

This guide explains the infrastructure code that was generated based on your requirements.

### Requirements
```
{requirements}
```

## Generated Files

"""
        
        # List generated files
        for filename in generated_files.keys():
            guide += f"- **{filename}**: "
            
            # Add description based on filename
            if "deployment" in filename.lower():
                guide += "Kubernetes Deployment manifest for pod management\n"
            elif "service" in filename.lower():
                guide += "Kubernetes Service for networking and load balancing\n"
            elif "configmap" in filename.lower():
                guide += "Kubernetes ConfigMap for configuration management\n"
            elif "main.tf" in filename.lower():
                guide += "Main Terraform configuration with infrastructure resources\n"
            elif "variables.tf" in filename.lower():
               guide += "Terraform input variables for customization\n"
            elif "outputs.tf" in filename.lower():
                guide += "Terraform outputs for resource information\n"
            elif "dockerfile" in filename.lower():
                guide += "Optimized multi-stage Dockerfile for building container images\n"
            elif "workflow" in filename.lower() or "ci" in filename.lower():
                guide += "CI/CD pipeline configuration for automated deployments\n"
            else:
                guide += "Generated infrastructure configuration\n"
        
        # Add deployment instructions
        if infra_type == "kubernetes":
            guide += self._kubernetes_deployment_guide()
        elif infra_type == "terraform":
            guide += self._terraform_deployment_guide()
        elif infra_type == "docker":
            guide += self._docker_deployment_guide()
        elif infra_type == "cicd":
            guide += self._cicd_deployment_guide()
        
        # Add common sections
        guide += self._security_checklist(infra_type)
        guide += self._customization_guide(infra_type)
        guide += self._official_documentation_links(infra_type)
        
        return guide
    
    def _kubernetes_deployment_guide(self) -> str:
        return """
## How to Deploy

### Prerequisites
- kubectl installed and configured
- Access to a Kubernetes cluster
- Proper RBAC permissions

### Deployment Steps

1. **Review the generated manifests**
   ```bash
   cat deployment.yaml
   cat service.yaml
   cat configmap.yaml
   ```

2. **Apply the ConfigMap first**
   ```bash
   kubectl apply -f configmap.yaml
   ```

3. **Deploy the application**
   ```bash
   kubectl apply -f deployment.yaml
   ```

4. **Create the service**
   ```bash
   kubectl apply -f service.yaml
   ```

5. **Verify deployment**
   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get services
   ```

6. **Check pod logs**
   ```bash
   kubectl logs -l app=<your-app-name>
   ```

"""
    
    def _terraform_deployment_guide(self) -> str:
        return """
## How to Deploy

### Prerequisites
- Terraform installed (v1.0+)
- AWS credentials configured
- Proper IAM permissions

### Deployment Steps

1. **Initialize Terraform**
   ```bash
   terraform init
   ```

2. **Review the plan**
   ```bash
   terraform plan
   ```

3. **Apply the configuration**
   ```bash
   terraform apply
   ```

4. **View outputs**
   ```bash
   terraform output
   ```

5. **To destroy (when needed)**
   ```bash
   terraform destroy
   ```

"""
    
    def _docker_deployment_guide(self) -> str:
        return """
## How to Build and Run

### Build the Image

```bash
docker build -t your-app:latest .
```

### Run the Container

```bash
docker run -d -p 8080:8080 your-app:latest
```

### Push to Registry (Optional)

```bash
docker tag your-app:latest your-registry/your-app:latest
docker push your-registry/your-app:latest
```

"""
    
    def _cicd_deployment_guide(self) -> str:
        return """
## How to Use the Pipeline

### Setup

1. Commit the pipeline configuration to your repository
2. Configure required secrets/variables in your CI/CD settings
3. Push to trigger the pipeline

### Required Secrets/Variables

- Cloud provider credentials
- Container registry credentials
- Kubernetes cluster access (if deploying to K8s)

"""
    
    def _security_checklist(self, infra_type: str) -> str:
        return """
## Security Checklist

The generated code implements these security best practices:

- ✅ Non-root user execution
- ✅ Resource limits enforced
- ✅ Security contexts configured
- ✅ Least privilege access
- ✅ Encrypted communication (where applicable)
- ✅ No hardcoded secrets (use environment variables)

### Additional Recommendations

- Review and adjust resource limits based on your needs
- Implement network policies for pod-to-pod communication
- Enable audit logging
- Regularly update base images and dependencies
- Use secrets management (Vault, AWS Secrets Manager, etc.)

"""
    
    def _customization_guide(self, infra_type: str) -> str:
        return """
## How to Customize

### Common Customizations

1. **Adjust resource limits**: Modify CPU and memory values based on application needs
2. **Change replica count**: Scale up or down based on load
3. **Update environment variables**: Modify ConfigMap for configuration changes
4. **Change image**: Update container image references
5. **Modify networking**: Adjust service types and port mappings

### Best Practices

- Test changes in a dev environment first
- Use version control for all modifications
- Document your customizations
- Keep security best practices in mind

"""
    
    def _official_documentation_links(self, infra_type: str) -> str:
        guide = """
## Official Documentation References

"""
        
        if infra_type == "kubernetes":
            guide += """
### Kubernetes Documentation

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Security Contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Health Checks](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
"""
        elif infra_type == "terraform":
            guide += """
### Terraform Documentation

- [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Language](https://developer.hashicorp.com/terraform/language)
- [Variables](https://developer.hashicorp.com/terraform/language/values/variables)
- [Outputs](https://developer.hashicorp.com/terraform/language/values/outputs)
- [Best Practices](https://www.terraform-best-practices.com/)
"""
        elif infra_type == "docker":
            guide += """
### Docker Documentation

- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Multi-stage Builds](https://docs.docker.com/develop/develop-images/multistage-build/)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/dockerfile-best-practices/)
- [Security](https://docs.docker.com/engine/security/)
"""
        
        guide += """

---

*Generated by InfraAgent - Built with Cline for the AI Agents Assemble Hackathon*
"""
        return guide
    
    def save_guide(self, guide: str, output_dir: str):
        """Save implementation guide to file"""
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, "IMPLEMENTATION_GUIDE.md")
        
        with open(filepath, 'w') as f:
            f.write(guide)
        
        print(f"✅ Generated: {filepath}")

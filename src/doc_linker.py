"""Documentation linking system for infrastructure code"""

# Kubernetes Official Documentation Links
K8S_DOC_LINKS = {
    "apiVersion": "https://kubernetes.io/docs/reference/kubernetes-api/",
    "Deployment": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
    "spec.replicas": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#replicas",
    "spec.strategy": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy",
    "containers": "https://kubernetes.io/docs/concepts/containers/",
    "image": "https://kubernetes.io/docs/concepts/containers/images/",
    "livenessProbe": "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/",
    "readinessProbe": "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes",
    "resources": "https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/",
    "resources.requests": "https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-requests-and-limits-of-pod-and-container",
    "resources.limits": "https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-requests-and-limits-of-pod-and-container",
    "securityContext": "https://kubernetes.io/docs/tasks/configure-pod-container/security-context/",
    "runAsNonRoot": "https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod",
    "Service": "https://kubernetes.io/docs/concepts/services-networking/service/",
    "Service.type": "https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types",
    "ConfigMap": "https://kubernetes.io/docs/concepts/configuration/configmap/",
    "namespace": "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/",
    "labels": "https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/",
    "selector": "https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
}

# Terraform Official Documentation Links
TERRAFORM_DOC_LINKS = {
    "aws_vpc": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc",
    "aws_subnet": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet",
    "aws_internet_gateway": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway",
    "aws_route_table": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table",
    "aws_security_group": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group",
    "aws_db_instance": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance",
    "aws_rds_cluster": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster",
    "variable": "https://developer.hashicorp.com/terraform/language/values/variables",
    "output": "https://developer.hashicorp.com/terraform/language/values/outputs",
    "provider": "https://developer.hashicorp.com/terraform/language/providers",
}

# Docker Official Documentation Links
DOCKER_DOC_LINKS = {
    "FROM": "https://docs.docker.com/engine/reference/builder/#from",
    "RUN": "https://docs.docker.com/engine/reference/builder/#run",
    "COPY": "https://docs.docker.com/engine/reference/builder/#copy",
    "ADD": "https://docs.docker.com/engine/reference/builder/#add",
    "WORKDIR": "https://docs.docker.com/engine/reference/builder/#workdir",
    "ENV": "https://docs.docker.com/engine/reference/builder/#env",
    "EXPOSE": "https://docs.docker.com/engine/reference/builder/#expose",
    "ENTRYPOINT": "https://docs.docker.com/engine/reference/builder/#entrypoint",
    "CMD": "https://docs.docker.com/engine/reference/builder/#cmd",
    "USER": "https://docs.docker.com/engine/reference/builder/#user",
    "HEALTHCHECK": "https://docs.docker.com/engine/reference/builder/#healthcheck",
    "multi-stage": "https://docs.docker.com/develop/develop-images/multistage-build/",
    "best-practices": "https://docs.docker.com/develop/dev-best-practices/dockerfile-best-practices/",
}

# CI/CD Documentation Links
CICD_DOC_LINKS = {
    "github-actions": "https://docs.github.com/en/actions",
    "workflow-syntax": "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions",
    "gitlab-ci": "https://docs.gitlab.com/ee/ci/",
    "gitlab-ci-yaml": "https://docs.gitlab.com/ee/ci/yaml/",
}


def get_doc_link(field: str, infra_type: str = "kubernetes") -> str:
    """
    Get documentation link for a specific field
    
    Args:
        field: The field name to get documentation for
        infra_type: Type of infrastructure (kubernetes, terraform, docker, cicd)
    
    Returns:
        str: URL to official documentation
    """
    link_maps = {
        "kubernetes": K8S_DOC_LINKS,
        "terraform": TERRAFORM_DOC_LINKS,
        "docker": DOCKER_DOC_LINKS,
        "cicd": CICD_DOC_LINKS,
    }
    
    links = link_maps.get(infra_type, K8S_DOC_LINKS)
    return links.get(field, f"https://kubernetes.io/docs/")


def format_doc_comment(field: str, infra_type: str = "kubernetes") -> str:
    """
    Format a documentation comment for a field
    
    Args:
        field: The field name
        infra_type: Type of infrastructure
    
    Returns:
        str: Formatted comment with documentation link
    """
    link = get_doc_link(field, infra_type)
    return f"# Reference: {link}"

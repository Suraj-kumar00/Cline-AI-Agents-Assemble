# InfraAgent 🚀

> Infrastructure Code Generation Tool powered by AI
> 
> **Built with Cline for the AI Agents Assemble Hackathon**

Generate production-ready Kubernetes manifests, Terraform code, Dockerfiles, and CI/CD pipelines using natural language. All outputs include links to official documentation and implement industry best practices.

## ✨ Features

- **🐳 Kubernetes YAML Generation** - Complete deployment manifests with services, configmaps, and health checks
- **🏗️ Terraform Code Generation** - AWS infrastructure code with variables and outputs
- **📦 Dockerfile Generation** - Multi-stage builds optimized for production
- **⚙️ CI/CD Pipeline Generation** - GitHub Actions and GitLab CI configurations
- **📚 Official Documentation Links** - Every generated field references official docs
- **🔒 Security Best Practices** - Non-root users, resource limits, security contexts
- **✅ Automatic Validation** - Syntax and best practice validation
- **📖 Implementation Guides** - Step-by-step deployment instructions

## 📋 Prerequisites

- Docker and Docker Compose installed
- Gemini API key (free from [Google AI Studio](https://aistudio.google.com))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/infraagent
cd infraagent
```

### 2. Configure API Key

```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### 3. Build Docker Container

```bash
docker-compose build
```

### 4. Generate Infrastructure Code

#### Kubernetes Manifests

```bash
docker-compose run infraagent generate-k8s --app flask --replicas 3 --port 8080
```

**Output:**
- `deployment.yaml` - Kubernetes Deployment with security contexts
- `service.yaml` - LoadBalancer Service
- `configmap.yaml` - Configuration management
- `IMPLEMENTATION_GUIDE.md` - Deployment instructions

#### Terraform Code

```bash
docker-compose run infraagent generate-terraform --cloud aws --service vpc
```

**Output:**
- `main.tf` - Infrastructure resources
- `variables.tf` - Input variables
- `outputs.tf` - Resource outputs
- `IMPLEMENTATION_GUIDE.md` - Deployment guide

#### Dockerfile

```bash
docker-compose run infraagent generate-docker --app python --port 8080
```

**Output:**
- `Dockerfile` - Multi-stage optimized build
- `.dockerignore` - Build optimization
- `IMPLEMENTATION_GUIDE.md` - Build instructions

#### CI/CD Pipeline

```bash
docker-compose run infraagent generate-cicd --platform github --deploy-target kubernetes
```

**Output:**
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `IMPLEMENTATION_GUIDE.md` - Setup instructions

## 📖 Commands Reference

### Kubernetes Generator

```bash
docker-compose run infraagent generate-k8s [OPTIONS]

Options:
  --app TEXT       Application type (required)
  --replicas INT   Number of replicas [default: 3]
  --port INT       Container port [default: 8080]
  --memory TEXT    Memory limit [default: 512Mi]
  --cpu TEXT       CPU limit [default: 250m]
  --output TEXT    Output directory [default: /app/output]
```

### Terraform Generator

```bash
docker-compose run infraagent generate-terraform [OPTIONS]

Options:
  --cloud TEXT     Cloud provider (aws, azure, gcp) [default: aws]
  --service TEXT   Service to deploy [default: vpc]
  --region TEXT    Cloud region [default: us-east-1]
  --output TEXT    Output directory [default: /app/output]
```

### Docker Generator

```bash
docker-compose run infraagent generate-docker [OPTIONS]

Options:
  --app TEXT         Application type (required)
  --base-image TEXT  Base image (optional)
  --port INT         Exposed port [default: 8080]
  --output TEXT      Output directory [default: /app/output]
```

### CI/CD Generator

```bash
docker-compose run infraagent generate-cicd [OPTIONS]

Options:
  --platform [github|gitlab]  CI/CD platform [default: github]
  --deploy-target TEXT        Deployment target [default: kubernetes]
  --output TEXT               Output directory [default: /app/output]
```

## 📁 Output

All generated files are saved to the `./output` directory on your host machine (automatically mounted from Docker).

Example structure:
```
output/
├── deployment.yaml
├── service.yaml
├── configmap.yaml
└── IMPLEMENTATION_GUIDE.md
```

## 🔒 Security Features

All generated code implements:

- ✅ Non-root user execution
- ✅ Read-only root filesystems (where applicable)
- ✅ Resource limits enforced
- ✅ Security contexts configured
- ✅ Least privilege access
- ✅ No hardcoded secrets

## 📚 Documentation Links

Generated code includes inline comments linking to:

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Terraform Registry](https://registry.terraform.io/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)

## 🏗️ Architecture

```
InfraAgent
├── src/
│   ├── cli.py              # Main CLI interface
│   ├── config.py           # Configuration management
│   ├── gemini_client.py    # AI API integration
│   ├── validators.py       # Code validation
│   └── doc_linker.py       # Documentation linking
├── generators/
│   ├── k8s_generator.py    # Kubernetes YAML generation
│   ├── terraform_generator.py  # Terraform code generation
│   ├── docker_generator.py     # Dockerfile generation
│   ├── cicd_generator.py       # CI/CD pipeline generation
│   └── documentation_generator.py  # Implementation guides
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Docker Compose setup
└── requirements.txt        # Python dependencies
```

## 🛠️ Development

### Running Locally (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export GEMINI_API_KEY=your_key_here

# Run CLI
python src/cli.py generate-k8s --app flask
```

### Running Tests

```bash
# Build container
docker-compose build

# Test Kubernetes generation
docker-compose run infraagent generate-k8s --app flask

# Test Terraform generation
docker-compose run infraagent generate-terraform --cloud aws

# Verify outputs
ls -la output/
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🙋‍♂️ Support

For issues or questions:

- Open an issue on GitHub
- Check the IMPLEMENTATION_GUIDE.md in generated output
- Review official documentation links in generated code

## 🎯 Use Cases

- **DevOps Teams**: Accelerate infrastructure provisioning
- **Developers**: Quickly bootstrap production-ready deployments
- **Learning**: Study best practices with linked documentation
- **Consistency**: Ensure all deployments follow same patterns

## ⚡ Why InfraAgent?

- **Time Savings**: 60+ minutes → 2 minutes
- **Best Practices**: Security and optimization built-in
- **Learning Tool**: Official docs linked for every field
- **Production Ready**: No "change-me" placeholders
- **Validated**: Automatic syntax and best practice checks

---

**Built with ❤️ using Cline for the AI Agents Assemble Hackathon** 🏆

*Powered by Gemini 3 Pro Preview*

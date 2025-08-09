# 🚀 GitHub Deployment Guide

This guide will help you deploy the AI News Reader project to GitHub and set up all necessary configurations.

## 📋 Pre-Deployment Checklist

### ✅ Security Review
- [ ] No API keys in code
- [ ] No sensitive data in commits
- [ ] `.env` file is in `.gitignore`
- [ ] `env.example` file is created
- [ ] All sensitive files are excluded

### ✅ Repository Setup
- [ ] Repository is created on GitHub
- [ ] Local repository is initialized
- [ ] All files are committed
- [ ] Remote origin is set

## 🔧 GitHub Repository Setup

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon and select "New repository"
3. Name: `AI-powered-News-Research-Tool`
4. Description: `A sophisticated news article analyzer powered by Google's Gemini AI`
5. Make it **Public** (for open source)
6. **Don't** initialize with README (we already have one)
7. Click "Create repository"

### 2. Initialize Local Repository

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: initial commit - AI News Reader with Docker support"

# Add remote origin
git remote add origin https://github.com/nagasaiveerla/AI-powered-News-Research-Tool.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Set Up GitHub Secrets

For CI/CD to work properly, you need to set up GitHub Secrets:

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:

#### Required Secrets

| Name | Description | Example |
|------|-------------|---------|
| `GEMINI_API_KEY` | Your Google Gemini API key for testing | `AIzaSyC...` |

#### Optional Secrets

| Name | Description | When to use |
|------|-------------|-------------|
| `DOCKER_USERNAME` | Docker Hub username | If using Docker Hub |
| `DOCKER_PASSWORD` | Docker Hub password | If using Docker Hub |

### 4. Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. You should see the workflows listed
3. Click on each workflow to enable it:
   - **CI** - Runs tests and linting
   - **Docker Deploy** - Builds and publishes Docker images

## 🔄 GitHub Actions Workflows

### CI Pipeline (`.github/workflows/ci.yml`)

This workflow runs on every push and pull request:

- **Python Testing**: Tests on Python 3.8, 3.9, 3.10, 3.11
- **Code Quality**: Runs flake8, black, isort
- **Security**: Runs bandit security checks
- **Docker Build**: Tests Docker image builds
- **Coverage**: Generates test coverage reports

### Docker Deploy (`.github/workflows/docker-deploy.yml`)

This workflow runs on pushes to main/master and tags:

- **Docker Build**: Builds production Docker image
- **Container Registry**: Publishes to GitHub Container Registry
- **Multi-arch**: Supports multiple architectures
- **Caching**: Uses GitHub Actions cache for faster builds

## 📦 GitHub Container Registry

### Accessing Docker Images

After deployment, your Docker images will be available at:

```bash
# Pull the latest image
docker pull ghcr.io/nagasaiveerla/ai-powered-news-research-tool:latest

# Run the container
docker run -p 5000:5000 -e GEMINI_API_KEY=your_key ghcr.io/nagasaiveerla/ai-powered-news-research-tool:latest
```

### Available Tags

- `latest` - Latest commit on main branch
- `main` - Latest commit on main branch
- `v1.0.0` - Semantic version tags
- `sha-abc123` - Commit SHA tags

## 🔍 Monitoring and Maintenance

### GitHub Insights

Monitor your repository health:

1. **Insights** → **Pulse**: View recent activity
2. **Insights** → **Contributors**: See contribution statistics
3. **Actions**: Monitor workflow runs
4. **Issues**: Track bugs and feature requests

### Repository Settings

Recommended settings:

1. **General**:
   - ✅ Allow squash merging
   - ✅ Allow rebase merging
   - ✅ Automatically delete head branches

2. **Branches**:
   - Add branch protection for `main`
   - Require status checks to pass
   - Require pull request reviews

3. **Pages** (Optional):
   - Enable GitHub Pages for documentation
   - Use `/docs` folder for static site

## 🚨 Troubleshooting

### Common Issues

#### Workflow Failures

1. **Missing Secrets**: Ensure `GEMINI_API_KEY` is set
2. **Docker Build Failures**: Check Dockerfile syntax
3. **Test Failures**: Run tests locally first

#### Permission Issues

1. **Workflow Permissions**: Check workflow permissions in Settings
2. **Package Permissions**: Ensure package write permissions

#### Docker Issues

1. **Registry Access**: Check GitHub Container Registry permissions
2. **Image Size**: Optimize Docker image size
3. **Build Time**: Use Docker layer caching

### Debug Commands

```bash
# Check workflow status
gh run list

# View workflow logs
gh run view <run-id>

# Re-run failed workflow
gh run rerun <run-id>

# Check repository status
gh repo view --web
```

## 📈 Next Steps

### After Deployment

1. **Create Issues**: Add feature requests and bugs
2. **Set up Discussions**: Enable GitHub Discussions for community
3. **Add Topics**: Add relevant topics to your repository
4. **Create Releases**: Tag releases for version management

### Community Building

1. **README**: Ensure README is comprehensive
2. **Contributing**: Link to CONTRIBUTING.md
3. **Code of Conduct**: Consider adding a Code of Conduct
4. **Documentation**: Add API documentation

### Advanced Features

1. **Dependabot**: Enable for automatic dependency updates
2. **Security**: Enable security scanning
3. **Analytics**: Set up repository analytics
4. **Sponsors**: Enable GitHub Sponsors

## 🎉 Success!

Your AI News Reader project is now successfully deployed to GitHub with:

- ✅ Full CI/CD pipeline
- ✅ Docker containerization
- ✅ Automated testing
- ✅ Security scanning
- ✅ Documentation
- ✅ Contributing guidelines

The project is ready for open source collaboration and production deployment!

---

**Need help?** Create an issue in the repository or check the [Contributing Guide](CONTRIBUTING.md). 
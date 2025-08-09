# Contributing to AI News Reader

Thank you for your interest in contributing to the AI News Reader project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized development)
- Google Gemini API key

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-powered-News-Research-Tool.git
   cd AI-powered-News-Research-Tool
   ```

2. **Set up your environment**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env and add your Gemini API key
   # GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development dependencies
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=./ --cov-report=html

# Run specific test file
pytest test_main.py

# Run tests with verbose output
pytest -v
```

### Code Quality

```bash
# Run linting
flake8 .

# Run type checking (if using mypy)
mypy .

# Run security checks
bandit -r .
```

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Git Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear commit messages
   - Keep commits atomic and focused

3. **Test your changes**
   ```bash
   pytest
   flake8 .
   ```

4. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Format

Use conventional commit messages:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Build/tooling changes

Examples:
```
feat(api): add new endpoint for article search
fix(ui): resolve mobile layout issues
docs(readme): update installation instructions
```

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Environment details**
   - Operating system
   - Python version
   - Package versions

2. **Steps to reproduce**
   - Clear, step-by-step instructions
   - Sample data if applicable

3. **Expected vs actual behavior**
   - What you expected to happen
   - What actually happened

4. **Additional context**
   - Screenshots if UI-related
   - Error messages and stack traces
   - Browser console logs if applicable

## 🔧 Development with Docker

### Using Docker for Development

```bash
# Build and run development container
docker-compose up --build

# Run tests in container
docker-compose exec ai-news-reader pytest

# Access container shell
docker-compose exec ai-news-reader bash
```

### Production Docker

```bash
# Build and run production container
docker-compose -f docker-compose.prod.yml up --build -d

# View logs
docker-compose -f docker-compose.prod.yml logs -f
```

## 📚 Documentation

### Adding Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions/classes
- Update API documentation if endpoints change
- Include examples for new features

### Code Comments

- Comment complex logic
- Explain business rules
- Document workarounds or temporary solutions
- Use TODO comments for future improvements

## 🔒 Security

### Security Guidelines

- Never commit API keys or sensitive data
- Use environment variables for configuration
- Validate all user inputs
- Follow OWASP security guidelines
- Report security issues privately

### Environment Variables

Always use environment variables for:
- API keys
- Database credentials
- Service URLs
- Configuration settings

## 🎯 Areas for Contribution

### High Priority
- [ ] Add comprehensive test coverage
- [ ] Implement rate limiting
- [ ] Add user authentication
- [ ] Improve error handling
- [ ] Add logging and monitoring

### Medium Priority
- [ ] Add support for more news sources
- [ ] Implement caching
- [ ] Add export functionality
- [ ] Improve UI/UX
- [ ] Add mobile app

### Low Priority
- [ ] Add internationalization
- [ ] Implement advanced analytics
- [ ] Add plugin system
- [ ] Create API documentation

## 🤝 Code Review Process

1. **Pull Request Requirements**
   - All tests must pass
   - Code must be linted and formatted
   - Documentation must be updated
   - No sensitive data in commits

2. **Review Checklist**
   - [ ] Code follows style guidelines
   - [ ] Tests are included and pass
   - [ ] Documentation is updated
   - [ ] No security issues
   - [ ] Performance impact considered

3. **Review Process**
   - At least one approval required
   - Address all review comments
   - Squash commits before merging
   - Use conventional commit messages

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Email**: Contact maintainers for security issues

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Acknowledgments

Thank you to all contributors who help make this project better!

---

**Happy coding! 🚀** 
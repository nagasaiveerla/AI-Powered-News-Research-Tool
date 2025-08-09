# 🤖 AI News Reader Project

[![CI](https://github.com/nagasaiveerla/AI-powered-News-Research-Tool/actions/workflows/ci.yml/badge.svg)](https://github.com/nagasaiveerla/AI-powered-News-Research-Tool/actions/workflows/ci.yml)
[![Docker](https://github.com/nagasaiveerla/AI-powered-News-Research-Tool/actions/workflows/docker-deploy.yml/badge.svg)](https://github.com/nagasaiveerla/AI-powered-News-Research-Tool/actions/workflows/docker-deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A sophisticated news article analyzer powered by Google's Gemini AI that allows users to load news articles and chat with an AI assistant about the content.

## ✨ Features

- **Article Loading**: Extract content from any news article URL
- **AI-Powered Summaries**: Generate comprehensive summaries using Gemini AI
- **Interactive Chat**: Ask questions about the loaded article and get intelligent responses
- **Session Management**: Maintain conversation context across multiple questions
- **Modern UI**: Beautiful, responsive web interface
- **Real-time Processing**: Fast article analysis and chat responses

## 🚀 Quick Start

### Prerequisites

- **Option 1: Local Development**
  - Python 3.8 or higher
  - Google Gemini API key

- **Option 2: Docker (Recommended)**
  - Docker and Docker Compose
  - Google Gemini API key

### Installation

#### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/nagasaiveerla/AI-powered-News-Research-Tool.git
   cd AI-powered-News-Research-Tool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Copy `env.example` to `.env` and update with your API key:
     ```bash
     # Copy the example file
     cp env.example .env
     
     # Edit .env file and replace with your actual API key
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   
   **Alternative method** - Set environment variable directly:
     ```bash
     # Windows PowerShell
     $env:GEMINI_API_KEY="your-api-key-here"
     
     # Linux/Mac
     export GEMINI_API_KEY="your-api-key-here"
     ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

#### Option 2: Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/nagasaiveerla/AI-powered-News-Research-Tool.git
   cd AI-powered-News-Research-Tool
   ```

2. **Set up your Gemini API key**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```bash
     # Create .env file
     echo GEMINI_API_KEY=your_actual_api_key_here > .env
     ```

3. **Run with Docker**:

   **Development mode:**
   ```bash
   # Using docker-compose
   docker-compose up --build
   
   # Or using the management script (Linux/Mac)
   chmod +x docker-scripts.sh
   ./docker-scripts.sh dev
   
   # Or using the management script (Windows)
   docker-scripts.bat dev
   ```

   **Production mode:**
   ```bash
   # Using docker-compose
   docker-compose -f docker-compose.prod.yml up --build -d
   
   # Or using the management script (Linux/Mac)
   ./docker-scripts.sh prod
   
   # Or using the management script (Windows)
   docker-scripts.bat prod
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

### Docker Management

The project includes convenient management scripts for Docker operations:

**Linux/Mac:**
```bash
./docker-scripts.sh [command]
```

**Windows:**
```cmd
docker-scripts.bat [command]
```

**Available commands:**
- `dev` - Start development environment
- `prod` - Start production environment  
- `stop` - Stop all containers
- `logs` - Show development logs
- `logs-prod` - Show production logs
- `rebuild` - Rebuild development containers
- `rebuild-prod` - Rebuild production containers
- `status` - Show container status
- `clean` - Clean up all Docker resources
- `help` - Show help message

## 📖 How to Use

1. **Load an Article**: Paste a news article URL in the input field and click "Load Article"
2. **Review Summary**: The AI will generate a comprehensive summary of the article
3. **Start Chatting**: Ask questions about the article content, statistics, expert opinions, or any other aspects
4. **Explore Further**: The AI maintains context, so you can ask follow-up questions

## 🛠️ API Endpoints

- `GET /` - Main application interface
- `GET /health` - Health check endpoint
- `GET /test-gemini` - Test Gemini API connectivity
- `POST /load-article` - Load and analyze a news article
- `POST /chat` - Send a message about the loaded article
- `GET /chat-history/<session_id>` - Get chat history for a session
- `GET /sessions` - List all active sessions

## 🏗️ Project Structure

```
AI-powered-News-Research-Tool/
├── main.py                 # Flask application and API endpoints
├── index.html             # Web interface
├── requirements.txt       # Python dependencies
├── requirements-dev.txt   # Development dependencies
├── README.md             # This file
├── CONTRIBUTING.md       # Contributing guidelines
├── LICENSE               # MIT License
├── env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── test_main.py          # Test suite
├── Dockerfile            # Development Docker configuration
├── Dockerfile.prod       # Production Docker configuration
├── docker-compose.yml    # Development Docker Compose
├── docker-compose.prod.yml # Production Docker Compose
├── .dockerignore         # Docker ignore rules
├── docker-scripts.sh     # Docker management script (Linux/Mac)
├── docker-scripts.bat    # Docker management script (Windows)
├── .github/
│   └── workflows/
│       ├── ci.yml        # Continuous Integration workflow
│       └── docker-deploy.yml # Docker deployment workflow
└── utils/
    ├── article_fetcher.py # Web scraping and content extraction
    ├── gemini_api.py      # Gemini AI integration
    └── prompt_manager.py  # AI prompt templates
```

## 🔧 Technical Details

### Backend (Flask)
- **Flask**: Web framework for API endpoints
- **Flask-CORS**: Cross-origin resource sharing
- **BeautifulSoup4**: HTML parsing and content extraction
- **Google Generative AI**: Integration with Gemini models

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Works on desktop and mobile
- **Modern UI**: Gradient backgrounds and smooth animations
- **Real-time Chat**: Dynamic message handling and typing indicators
- **Error Handling**: User-friendly error messages

### AI Integration
- **Gemini 1.5 Flash**: Fast and efficient AI model
- **Contextual Prompts**: Maintains conversation context
- **Safety Settings**: Built-in content filtering
- **Custom Prompts**: Specialized templates for summaries and chat

## 🎯 Example Usage

1. **Load an article**: `https://www.bbc.com/news/technology`
2. **Ask questions like**:
   - "What are the main points of this article?"
   - "What statistics are mentioned?"
   - "What do experts say about this topic?"
   - "What are the key challenges discussed?"

## 🔒 Security Features

- **Input Validation**: URL and content validation
- **Error Handling**: Graceful error responses
- **Session Management**: Isolated conversation contexts
- **Content Filtering**: AI safety settings enabled

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Docker Development
```bash
docker-compose up --build
```

### Production Deployment

#### Option 1: Docker Production (Recommended)
```bash
# Using docker-compose
docker-compose -f docker-compose.prod.yml up --build -d

# Or using management script
./docker-scripts.sh prod  # Linux/Mac
docker-scripts.bat prod   # Windows
```

#### Option 2: Traditional Production
For traditional production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up environment variables properly
- Adding HTTPS/SSL certificates
- Implementing proper session storage (Redis, database)
- Adding rate limiting and authentication

#### Docker Production Features
- **Gunicorn WSGI Server**: Multi-worker process for better performance
- **Health Checks**: Automatic container health monitoring
- **Resource Limits**: Memory and CPU constraints for stability
- **Non-root User**: Enhanced security with app user
- **Logging**: Structured logging with access and error logs
- **Restart Policy**: Automatic restart on failure

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for detailed information on how to contribute to this project.

### Quick Start for Contributors

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/AI-powered-News-Research-Tool.git
   cd AI-powered-News-Research-Tool
   ```

3. **Set up development environment**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   cp env.example .env
   # Edit .env with your API key
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Make your changes and test**
   ```bash
   pytest
   flake8 .
   ```

7. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature"
   git push origin feature/your-feature-name
   ```

8. **Create a pull request**

## 🔄 CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

### Automated Workflows

- **CI Pipeline**: Runs tests on multiple Python versions, linting, and security checks
- **Docker Build**: Automatically builds and tests Docker images
- **Docker Deploy**: Publishes Docker images to GitHub Container Registry

### Quality Gates

- All tests must pass
- Code must pass linting (flake8, black, isort)
- Security checks must pass (bandit)
- Docker images must build successfully

### Environment Variables

For CI/CD to work properly, set up these GitHub Secrets:
- `GEMINI_API_KEY`: Your Google Gemini API key for testing

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY environment variable is required"**
   - Make sure you've set the environment variable correctly
   - Restart your terminal/command prompt after setting it
   - For Docker: Ensure your `.env` file exists and contains the API key

2. **"Failed to fetch article content"**
   - Check if the URL is accessible
   - Some websites may block automated requests
   - Try a different news article URL

3. **"Gemini API error"**
   - Verify your API key is valid
   - Check your internet connection
   - Ensure you have sufficient API quota

### Docker-Specific Issues

4. **"Docker build fails"**
   - Ensure Docker and Docker Compose are installed
   - Check if you have sufficient disk space
   - Try rebuilding with `docker-compose build --no-cache`

5. **"Container won't start"**
   - Check container logs: `docker-compose logs`
   - Verify the `.env` file exists and has correct format
   - Ensure port 5000 is not already in use

6. **"Permission denied" on scripts**
   - Make scripts executable: `chmod +x docker-scripts.sh`
   - On Windows, run as Administrator if needed

7. **"Health check fails"**
   - Wait a few minutes for the application to fully start
   - Check if the application is responding on port 5000
   - Verify the health endpoint: `curl http://localhost:5000/health`

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Test the `/health` and `/test-gemini` endpoints
4. Check the browser's developer console for frontend errors

## 🎉 Success!

Your AI News Reader is now running successfully! You can:
- Load any news article by URL
- Get AI-generated summaries
- Chat intelligently about article content
- Explore the full power of AI-assisted news analysis

Enjoy exploring the future of news reading! 📰🤖 
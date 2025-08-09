from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from utils.article_fetcher import ArticleFetcher
from utils.gemini_api import GeminiAPI
from utils.prompt_manager import PromptManager
import logging
import json
from datetime import datetime

# Load environment variables
load_dotenv()


# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize components
article_fetcher = ArticleFetcher()
gemini_api = None
prompt_manager = PromptManager()

def initialize_gemini():
    global gemini_api
    if gemini_api is None:
        gemini_api = GeminiAPI()

# Store active sessions (in production, use Redis or database)
active_sessions = {}

@app.route('/')
def index():
    """Serve the main application"""
    return send_from_directory('.', 'index.html')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/test-gemini', methods=['GET'])
def test_gemini():
    """Test Gemini API endpoint"""
    try:
        initialize_gemini()
        test_prompt = "Hello! Please respond with 'Gemini API is working correctly' if you can see this message."
        response = gemini_api.generate_response(test_prompt)
        return jsonify({
            "status": "success",
            "response": response,
            "message": "Gemini API is working correctly"
        })
    except Exception as e:
        logger.error(f"Gemini API test failed: {str(e)}")
        return jsonify({"error": f"Gemini API test failed: {str(e)}"}), 500

@app.route('/load-article', methods=['POST'])
def load_article():
    """Load and analyze a news article"""
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        logger.info(f"Loading article from: {url}")
        
        # Fetch article content
        article_data = article_fetcher.fetch_article(url)
        
        if not article_data:
            return jsonify({"error": "Failed to fetch article content"}), 400
        
        # Initialize Gemini API
        initialize_gemini()
        
        # Generate summary using Gemini
        summary_prompt = prompt_manager.create_summary_prompt(article_data['content'])
        summary = gemini_api.generate_response(summary_prompt)
        
        # Create session
        session_id = f"session_{datetime.now().timestamp()}"
        active_sessions[session_id] = {
            'article': article_data,
            'summary': summary,
            'chat_history': [],
            'created_at': datetime.now().isoformat()
        }
        
        response_data = {
            'session_id': session_id,
            'title': article_data['title'],
            'url': article_data['url'],
            'summary': summary,
            'word_count': len(article_data['content'].split()),
            'published_date': article_data.get('published_date'),
            'author': article_data.get('author')
        }
        
        logger.info(f"Article loaded successfully: {article_data['title']}")
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Error loading article: {str(e)}")
        return jsonify({"error": "Failed to load article"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages about the loaded article"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({"error": "Session ID and message are required"}), 400
        
        if session_id not in active_sessions:
            return jsonify({"error": "Invalid session ID"}), 400
        
        session = active_sessions[session_id]
        article_content = session['article']['content']
        chat_history = session['chat_history']
        
        logger.info(f"Processing chat message: {message[:50]}...")
        
        # Create chat prompt with context
        chat_prompt = prompt_manager.create_chat_prompt(
            article_content, 
            message, 
            chat_history
        )
        
        # Initialize Gemini API
        initialize_gemini()
        
        # Generate response using Gemini
        response = gemini_api.generate_response(chat_prompt)
        
        # Update chat history
        chat_entry = {
            'question': message,
            'answer': response,
            'timestamp': datetime.now().isoformat()
        }
        chat_history.append(chat_entry)
        
        return jsonify({
            'response': response,
            'session_id': session_id
        })
        
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        return jsonify({"error": "Failed to process message"}), 500

@app.route('/chat-history/<session_id>', methods=['GET'])
def get_chat_history(session_id):
    """Get chat history for a session"""
    if session_id not in active_sessions:
        return jsonify({"error": "Invalid session ID"}), 400
    
    return jsonify({
        'chat_history': active_sessions[session_id]['chat_history'],
        'article_title': active_sessions[session_id]['article']['title']
    })

@app.route('/sessions', methods=['GET'])
def list_sessions():
    """List all active sessions"""
    sessions = []
    for sid, session in active_sessions.items():
        sessions.append({
            'session_id': sid,
            'title': session['article']['title'],
            'url': session['article']['url'],
            'created_at': session['created_at'],
            'message_count': len(session['chat_history'])
        })
    
    return jsonify({'sessions': sessions})

if __name__ == '__main__':
    # Ensure required environment variables are set
    if not os.getenv('GEMINI_API_KEY'):
        logger.error("GEMINI_API_KEY environment variable is required")
        exit(1)
    
    # Get port from environment variable or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # Set debug mode based on environment
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f"Starting AI News Reader on port {port}")
    app.run(debug=debug_mode, host='0.0.0.0', port=port)


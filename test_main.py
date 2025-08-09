import pytest
import os
import sys
from unittest.mock import patch, MagicMock

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_index_page(client):
    """Test the main index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI News Reader' in response.data

@patch('main.gemini_api')
def test_test_gemini_endpoint(mock_gemini_api, client):
    """Test the Gemini API test endpoint."""
    # Mock the Gemini API response
    mock_gemini_api.generate_response.return_value = "Gemini API is working correctly"
    
    response = client.get('/test-gemini')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'Gemini API is working correctly' in data['response']

def test_load_article_missing_url(client):
    """Test loading article without URL."""
    response = client.post('/load-article', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'URL is required'

def test_chat_missing_parameters(client):
    """Test chat endpoint with missing parameters."""
    response = client.post('/chat', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Session ID and message are required'

def test_chat_invalid_session(client):
    """Test chat endpoint with invalid session ID."""
    response = client.post('/chat', json={
        'session_id': 'invalid_session',
        'message': 'test message'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid session ID'

def test_chat_history_invalid_session(client):
    """Test chat history endpoint with invalid session ID."""
    response = client.get('/chat-history/invalid_session')
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid session ID'

def test_sessions_endpoint(client):
    """Test the sessions endpoint."""
    response = client.get('/sessions')
    assert response.status_code == 200
    data = response.get_json()
    assert 'sessions' in data
    assert isinstance(data['sessions'], list)

if __name__ == '__main__':
    pytest.main([__file__]) 
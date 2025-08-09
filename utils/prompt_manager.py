import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class PromptManager:
    def __init__(self):
        self.summary_template = """
You are an expert news analyst. Please analyze the following news article and provide a comprehensive summary.

ARTICLE CONTENT:
{article_content}

INSTRUCTIONS:
1. Create a clear, concise summary highlighting the key points
2. Include important statistics, quotes, and facts mentioned
3. Identify the main stakeholders and their perspectives
4. Note any significant implications or consequences discussed
5. Maintain objectivity and factual accuracy
6. Use bullet points for easy readability

Please provide your analysis:
"""
        
        self.chat_template = """
You are a helpful AI assistant specialized in analyzing news articles. You have been provided with a news article and should answer questions about it based ONLY on the information contained in the article.

ARTICLE CONTENT:
{article_content}

PREVIOUS CONVERSATION:
{chat_history}

CURRENT QUESTION: {question}

INSTRUCTIONS:
1. Answer based ONLY on information from the provided article
2. If the question cannot be answered from the article, say so clearly
3. Be accurate and specific in your responses
4. Include relevant quotes or statistics when appropriate
5. Maintain a conversational but informative tone
6. If asked for your opinion, clarify that you're providing analysis based on the article content

Your response:
"""
    
    def create_summary_prompt(self, article_content: str) -> str:
        """Create a prompt for article summarization"""
        return self.summary_template.format(article_content=article_content)
    
    def create_chat_prompt(self, article_content: str, question: str, chat_history: List[Dict]) -> str:
        """Create a prompt for chat interaction"""
        # Format chat history
        formatted_history = ""
        for entry in chat_history[-5:]:  # Keep last 5 exchanges for context
            formatted_history += f"Q: {entry['question']}\nA: {entry['answer']}\n\n"
        
        if not formatted_history:
            formatted_history = "No previous conversation."
        
        return self.chat_template.format(
            article_content=article_content,
            chat_history=formatted_history,
            question=question
        )


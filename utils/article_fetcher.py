import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ArticleFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def fetch_article(self, url):
        """Fetch and extract article content from URL"""
        try:
            logger.info(f"Fetching article from: {url}")
            
            # Fetch the webpage
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract article data
            article_data = {
                'url': url,
                'title': self._extract_title(soup),
                'content': self._extract_content(soup),
                'author': self._extract_author(soup),
                'published_date': self._extract_date(soup),
                'meta_description': self._extract_meta_description(soup)
            }
            
            # Validate extracted content
            if not article_data['content'] or len(article_data['content']) < 100:
                raise ValueError("Article content too short or empty")
            
            logger.info(f"Successfully extracted article: {article_data['title']}")
            return article_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error fetching article: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error extracting article: {str(e)}")
            return None
    
    def _extract_title(self, soup):
        """Extract article title"""
        # Try multiple selectors
        selectors = [
            'h1',
            '[class*="title"]',
            '[class*="headline"]',
            'title'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element and element.get_text().strip():
                return element.get_text().strip()
        
        return "Untitled Article"
    
    def _extract_content(self, soup):
        """Extract main article content"""
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'advertisement', 'iframe']):
            element.decompose()
        
        # Try common article selectors
        content_selectors = [
            '[class*="content"]',
            '[class*="article"]',
            '[class*="story"]',
            '[class*="post"]',
            'main',
            '.entry-content',
            '#content',
            'article',
            '.post-content',
            '.story-body',
            '.article-body'
        ]
        
        content = ""
        for selector in content_selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text().strip()
                if len(text) > len(content):
                    content = text
        
        # If no content found, extract from paragraphs
        if not content:
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        
        # If still no content, try body text
        if not content:
            body = soup.find('body')
            if body:
                content = body.get_text().strip()
        
        # Clean up content
        content = re.sub(r'\s+', ' ', content)
        content = re.sub(r'\n+', '\n', content)
        
        return content.strip()
    
    def _extract_author(self, soup):
        """Extract article author"""
        author_selectors = [
            '[class*="author"]',
            '[class*="byline"]',
            '[rel="author"]',
            '.writer',
            '.journalist'
        ]
        
        for selector in author_selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text().strip()
        
        return None
    
    def _extract_date(self, soup):
        """Extract publication date"""
        date_selectors = [
            '[class*="date"]',
            '[class*="time"]',
            'time',
            '[datetime]'
        ]
        
        for selector in date_selectors:
            element = soup.select_one(selector)
            if element:
                # Try to get datetime attribute first
                date_str = element.get('datetime') or element.get_text().strip()
                if date_str:
                    return date_str
        
        return None
    
    def _extract_meta_description(self, soup):
        """Extract meta description"""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            return meta_desc.get('content', '').strip()
        return None
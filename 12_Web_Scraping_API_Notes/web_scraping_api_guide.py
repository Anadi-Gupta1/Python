"""
Web Scraping and API Integration in Python
==========================================

Educational guide to web scraping with BeautifulSoup and requests, plus API integration.
Includes error handling, rate limiting, and best practices for web data extraction.

Author: Python Learning Notes
Date: September 2025
Topic: Web Scraping, API, BeautifulSoup, Requests, Rate Limiting
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import Dict, List, Optional
import logging

# =============================================================================
# WEB SCRAPING WITH BEAUTIFULSOUP
# =============================================================================

class WebScraper:
    """Web scraper with error handling and rate limiting"""
    
    def __init__(self, delay: float = 1.0):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a web page"""
        try:
            time.sleep(self.delay)  # Rate limiting
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def scrape_quotes(self, url: str = "http://quotes.toscrape.com/") -> List[Dict]:
        """Scrape quotes from quotes.toscrape.com"""
        soup = self.get_page(url)
        if not soup:
            return []
        
        quotes = []
        for quote_div in soup.find_all('div', class_='quote'):
            quote_text = quote_div.find('span', class_='text').get_text()
            author = quote_div.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]
            
            quotes.append({
                'text': quote_text,
                'author': author,
                'tags': tags
            })
        
        return quotes

# =============================================================================
# API INTEGRATION
# =============================================================================

class APIClient:
    """REST API client with error handling and retry logic"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
        self.session.headers.update({'Content-Type': 'application/json'})
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """GET request with error handling"""
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API GET error: {e}")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON response")
            return None
    
    def post(self, endpoint: str, data: Dict) -> Optional[Dict]:
        """POST request with error handling"""
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API POST error: {e}")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON response")
            return None

# =============================================================================
# JSONPlaceholder API EXAMPLE
# =============================================================================

def jsonplaceholder_demo():
    """Demonstrate API integration with JSONPlaceholder"""
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # GET posts
    posts = client.get("posts", {"_limit": 3})
    if posts:
        print("Sample Posts:")
        for post in posts:
            print(f"  {post['id']}: {post['title'][:50]}...")
    
    # GET specific post
    post = client.get("posts/1")
    if post:
        print(f"\nPost 1 details: {post['title']}")
    
    # POST new post
    new_post = {
        "title": "Learning Python APIs",
        "body": "This is a test post created via API",
        "userId": 1
    }
    created_post = client.post("posts", new_post)
    if created_post:
        print(f"\nCreated new post with ID: {created_post.get('id')}")

# =============================================================================
# GITHUB API EXAMPLE
# =============================================================================

def github_api_demo():
    """Demonstrate GitHub API integration"""
    client = APIClient("https://api.github.com")
    
    # Get user info
    user = client.get("users/octocat")
    if user:
        print(f"\nGitHub User: {user['login']}")
        print(f"Name: {user['name']}")
        print(f"Followers: {user['followers']}")
        print(f"Public repos: {user['public_repos']}")
    
    # Get repositories
    repos = client.get("users/octocat/repos", {"sort": "updated", "per_page": 3})
    if repos:
        print("\nRecent repositories:")
        for repo in repos:
            print(f"  {repo['name']}: {repo['description'] or 'No description'}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    # Web scraping demo
    print("Web Scraping Demo:")
    scraper = WebScraper(delay=0.5)
    quotes = scraper.scrape_quotes()
    if quotes:
        print(f"Scraped {len(quotes)} quotes:")
        for i, quote in enumerate(quotes[:3]):  # Show first 3
            print(f"  {i+1}. \"{quote['text']}\" - {quote['author']}")
    
    # API integration demos
    print("\nAPI Integration Demos:")
    jsonplaceholder_demo()
    github_api_demo()
    
    print("\nWeb scraping and API integration completed!")

if __name__ == "__main__":
    main()

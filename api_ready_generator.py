#!/usr/bin/env python3
"""
API-Ready AI News Generator
Template for integrating with real search APIs (Google, Bing, etc.)
"""

import datetime
import os
import json
import requests
from typing import Dict, List, Optional
from daily_summary_generator import DailySummaryGenerator

class APIReadyAIGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.generator = DailySummaryGenerator()
        self.api_key = api_key or os.getenv('SEARCH_API_KEY')
        
        # Example search queries for AI news
        self.search_queries = [
            "AI breakthrough 2024 latest news",
            "OpenAI ChatGPT new features announcement",
            "Google Gemini AI updates",
            "artificial intelligence development news",
            "machine learning research breakthrough"
        ]
    
    def search_with_google_api(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Template for Google Custom Search API integration
        Replace with your actual API implementation
        """
        if not self.api_key:
            print("⚠️  No API key found. Using demo results.")
            return self.get_demo_results()
        
        # TODO: Replace with actual Google Custom Search API call
        # Example implementation:
        """
        search_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.api_key,
            'cx': 'YOUR_SEARCH_ENGINE_ID',  # Get from Google Custom Search
            'q': query,
            'num': num_results
        }
        
        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get('items', []):
                results.append({
                    'title': item.get('title', ''),
                    'snippet': item.get('snippet', ''),
                    'link': item.get('link', ''),
                    'date': item.get('pagemap', {}).get('metatags', [{}])[0].get('article:published_time', '')
                })
            
            return results
            
        except Exception as e:
            print(f"API Error: {e}")
            return self.get_demo_results()
        """
        
        return self.get_demo_results()
    
    def search_with_bing_api(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Template for Bing Search API integration
        Replace with your actual API implementation
        """
        if not self.api_key:
            print("⚠️  No API key found. Using demo results.")
            return self.get_demo_results()
        
        # TODO: Replace with actual Bing Search API call
        # Example implementation:
        """
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key
        }
        params = {
            'q': query,
            'count': num_results,
            'responseFilter': 'webpages',
            'freshness': 'day'
        }
        
        try:
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get('webPages', {}).get('value', []):
                results.append({
                    'title': item.get('name', ''),
                    'snippet': item.get('snippet', ''),
                    'link': item.get('url', ''),
                    'date': item.get('datePublished', '')
                })
            
            return results
            
        except Exception as e:
            print(f"API Error: {e}")
            return self.get_demo_results()
        """
        
        return self.get_demo_results()
    
    def search_with_newsapi(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Template for NewsAPI integration
        Replace with your actual API implementation
        """
        if not self.api_key:
            print("⚠️  No API key found. Using demo results.")
            return self.get_demo_results()
        
        # TODO: Replace with actual NewsAPI call
        # Example implementation:
        """
        search_url = "https://newsapi.org/v2/everything"
        headers = {
            'X-API-Key': self.api_key
        }
        params = {
            'q': query,
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': num_results,
            'domains': 'techcrunch.com,wired.com,theverge.com,arstechnica.com'
        }
        
        try:
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for article in data.get('articles', []):
                results.append({
                    'title': article.get('title', ''),
                    'snippet': article.get('description', ''),
                    'link': article.get('url', ''),
                    'date': article.get('publishedAt', ''),
                    'source': article.get('source', {}).get('name', '')
                })
            
            return results
            
        except Exception as e:
            print(f"API Error: {e}")
            return self.get_demo_results()
        """
        
        return self.get_demo_results()
    
    def get_demo_results(self) -> List[Dict]:
        """
        Demo results when no API key is available
        """
        return [
            {
                'title': 'Google Announces Gemini 2.5 Pro with Advanced Reasoning',
                'snippet': 'Google unveils Gemini 2.5 Pro with enhanced reasoning capabilities, multimodal understanding, and improved code generation. The model shows significant improvements in mathematical problem-solving and complex reasoning tasks.',
                'link': 'https://blog.google/technology/ai/gemini-2-5-pro-announcement',
                'date': '2024-12-15',
                'source': 'Google Blog'
            },
            {
                'title': 'OpenAI Releases ChatGPT-5 with Multimodal Capabilities',
                'snippet': 'OpenAI announces ChatGPT-5 featuring native image, audio, and video processing. The new model demonstrates superior performance in creative tasks and can generate multimedia content.',
                'link': 'https://openai.com/blog/chatgpt-5-release',
                'date': '2024-12-14',
                'source': 'OpenAI'
            },
            {
                'title': 'Microsoft Copilot Gets Major Update with AI Agents',
                'snippet': 'Microsoft introduces AI agents in Copilot, allowing users to automate complex workflows across Office applications. The update includes enhanced Excel formulas and PowerPoint design assistance.',
                'link': 'https://blogs.microsoft.com/blog/2024/12/13/copilot-ai-agents-update',
                'date': '2024-12-13',
                'source': 'Microsoft Blog'
            }
        ]
    
    def select_best_story(self, search_results: List[Dict]) -> Dict:
        """
        Select the most interesting story from search results
        """
        if not search_results:
            return self.get_demo_results()[0]
        
        # Simple selection: pick the first result
        # You can enhance this with more sophisticated selection logic
        return search_results[0]
    
    def create_summary_from_story(self, story: Dict) -> Dict[str, str]:
        """
        Create formatted summary from a news story
        """
        title = story.get('title', '')
        snippet = story.get('snippet', '')
        
        # Process the story into summary format
        content = {
            "highlight": self.clean_title(title),
            "description": self.simplify_description(snippet),
            "what": self.extract_what_from_story(snippet),
            "why_matters": self.extract_why_matters(snippet),
            "cool_factor": self.extract_cool_factor(snippet),
            "takeaway": self.generate_takeaway(snippet)
        }
        
        return content
    
    def clean_title(self, title: str) -> str:
        """Clean and format the title"""
        # Remove common prefixes and limit length
        title = title.replace('Breaking:', '').replace('News:', '').strip()
        if len(title) > 60:
            title = title[:57] + "..."
        return title
    
    def simplify_description(self, description: str) -> str:
        """Simplify description for general audience"""
        # Replace technical terms with simpler ones
        description = description.replace('multimodal', 'multi-format')
        description = description.replace('capabilities', 'abilities')
        description = description.replace('enhanced', 'improved')
        
        # Limit to 2 sentences
        sentences = description.split('. ')
        if len(sentences) > 2:
            description = '. '.join(sentences[:2]) + '.'
        
        return description
    
    def extract_what_from_story(self, snippet: str) -> str:
        """Extract 'what' information"""
        snippet_lower = snippet.lower()
        
        if 'gemini' in snippet_lower:
            return "Google's advanced AI model for complex reasoning and multimodal tasks"
        elif 'chatgpt' in snippet_lower or 'gpt' in snippet_lower:
            return "OpenAI's conversational AI with enhanced capabilities"
        elif 'copilot' in snippet_lower:
            return "Microsoft's AI assistant integrated into Office applications"
        else:
            return "New AI technology that improves how computers understand and help humans"
    
    def extract_why_matters(self, snippet: str) -> str:
        """Extract why this matters"""
        snippet_lower = snippet.lower()
        
        if 'reasoning' in snippet_lower:
            return "Makes AI better at solving complex problems and thinking logically"
        elif 'multimodal' in snippet_lower:
            return "Allows AI to work with text, images, audio, and video together"
        elif 'productivity' in snippet_lower:
            return "Helps people work more efficiently and automate routine tasks"
        else:
            return "Advances AI capabilities to be more helpful in daily life"
    
    def extract_cool_factor(self, snippet: str) -> str:
        """Extract interesting detail"""
        snippet_lower = snippet.lower()
        
        if 'performance' in snippet_lower:
            return "Shows significant improvements over previous AI models"
        elif 'multimodal' in snippet_lower:
            return "Can understand and create images, audio, and video content"
        elif 'reasoning' in snippet_lower:
            return "Can think through problems step-by-step like a human"
        else:
            return "Represents a major breakthrough in AI technology"
    
    def generate_takeaway(self, snippet: str) -> str:
        """Generate simple takeaway"""
        snippet_lower = snippet.lower()
        
        if 'google' in snippet_lower:
            return "Google is pushing the boundaries of AI with more intelligent systems that can understand and reason across multiple types of content, making AI more useful for both personal and professional tasks."
        elif 'openai' in snippet_lower:
            return "OpenAI continues to advance conversational AI with more sophisticated capabilities that bring us closer to AI assistants that truly understand and help with complex tasks."
        elif 'microsoft' in snippet_lower:
            return "Microsoft is integrating AI deeper into everyday work tools, making it easier for people to automate tasks and be more productive without technical expertise."
        else:
            return "These AI advances show how technology is becoming more intuitive and helpful, potentially transforming how we work, learn, and solve problems in the coming years."
    
    def generate_automated_summary(self, search_api: str = "demo") -> str:
        """
        Generate automated summary using specified search API
        """
        print(f"🤖 Generating AI news summary using {search_api} API...")
        
        # Select and use the appropriate search API
        if search_api == "google" and self.api_key:
            results = self.search_with_google_api("AI breakthrough news today")
        elif search_api == "bing" and self.api_key:
            results = self.search_with_bing_api("artificial intelligence news")
        elif search_api == "newsapi" and self.api_key:
            results = self.search_with_newsapi("AI technology updates")
        else:
            print("🔍 Using demo results (add your API key for real search)")
            results = self.get_demo_results()
        
        # Select best story
        story = self.select_best_story(results)
        print(f"📰 Selected story: {story['title'][:50]}...")
        
        # Create summary
        content = self.create_summary_from_story(story)
        
        # Ensure word count is reasonable
        total_words = self.generator.count_words(
            content['description'] + content['what'] + 
            content['why_matters'] + content['cool_factor'] + content['takeaway']
        )
        
        if total_words > 100:
            print(f"⚠️  Summary is {total_words} words, trimming to 100...")
            content = self.trim_content(content)
        
        # Generate HTML
        html_content = self.generator.generate_html_email(content)
        
        # Save files
        today = datetime.date.today().strftime("%Y-%m-%d")
        html_filename = f"api_ai_summary_{today}.html"
        md_filename = f"api_ai_summary_{today}.md"
        
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        markdown_content = self.generator.create_summary(content)
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        final_word_count = self.generator.count_words(
            content['description'] + content['what'] + 
            content['why_matters'] + content['cool_factor'] + content['takeaway']
        )
        
        print(f"✅ Generated files:")
        print(f"   - {html_filename}")
        print(f"   - {md_filename}")
        print(f"📊 Final word count: {final_word_count}")
        print(f"📧 Ready for your email newsletter!")
        
        return html_filename
    
    def trim_content(self, content: Dict[str, str]) -> Dict[str, str]:
        """Trim content to fit word limit"""
        # Shorten takeaway first
        takeaway_words = content['takeaway'].split()
        if len(takeaway_words) > 35:
            content['takeaway'] = ' '.join(takeaway_words[:35]) + '...'
        
        # Shorten description if needed
        description_words = content['description'].split()
        if len(description_words) > 20:
            content['description'] = ' '.join(description_words[:20]) + '...'
        
        return content

def setup_instructions():
    """
    Instructions for setting up API keys
    """
    print("""
    🔧 API Setup Instructions:
    
    1. Google Custom Search API:
       - Go to: https://developers.google.com/custom-search/v1/introduction
       - Create a project and enable Custom Search API
       - Get your API key and Search Engine ID
       - Set environment variable: export SEARCH_API_KEY=your_key_here
    
    2. Bing Search API:
       - Go to: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
       - Subscribe to get your API key
       - Set environment variable: export SEARCH_API_KEY=your_key_here
    
    3. NewsAPI:
       - Go to: https://newsapi.org/
       - Register for a free API key
       - Set environment variable: export SEARCH_API_KEY=your_key_here
    
    4. Alternative: Use environment variables
       - Create a .env file with: SEARCH_API_KEY=your_key_here
       - Or set it in your shell: export SEARCH_API_KEY=your_key_here
    """)

def main():
    print("🚀 API-Ready AI News Generator")
    
    # Check for API key
    api_key = os.getenv('SEARCH_API_KEY')
    if not api_key:
        print("⚠️  No API key found. Using demo mode.")
        print("💡 Add your API key to use real search results.")
        setup_instructions()
    
    # Initialize generator
    generator = APIReadyAIGenerator(api_key)
    
    # Generate summary
    html_file = generator.generate_automated_summary()
    
    print(f"\n🎉 Daily AI summary generated!")
    print(f"📂 Open: {html_file}")
    print(f"📧 Copy content into your email editor and send!")

if __name__ == "__main__":
    main()
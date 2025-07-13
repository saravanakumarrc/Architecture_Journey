#!/usr/bin/env python3
"""
Automated AI News Generator
Searches the web for latest AI/cloud news and generates formatted summaries
"""

import datetime
import json
import re
import requests
from typing import Dict, List, Optional
from daily_summary_generator import DailySummaryGenerator

class AutomatedNewsGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.generator = DailySummaryGenerator()
        self.search_terms = [
            "AI breakthrough 2024",
            "OpenAI ChatGPT new features",
            "Google Gemini updates",
            "Claude AI improvements",
            "AWS cloud services announcement",
            "Microsoft Azure AI tools",
            "machine learning development",
            "AI industry news today",
            "cloud computing updates",
            "artificial intelligence trends"
        ]
    
    def search_web_news(self, query: str, num_results: int = 3) -> List[Dict]:
        """
        Search for AI/cloud news using web search
        Returns a list of news articles with title, snippet, and URL
        """
        try:
            # For now, I'll create a mock search function
            # You can replace this with your preferred API (Google, Bing, etc.)
            print(f"🔍 Searching for: {query}")
            
            # Mock results - replace with actual API call
            mock_results = [
                {
                    "title": "OpenAI Releases GPT-4 Turbo with Vision Capabilities",
                    "snippet": "OpenAI has announced GPT-4 Turbo, featuring enhanced vision capabilities that allow the AI to process and understand images alongside text inputs. This update significantly improves multimodal AI interactions.",
                    "url": "https://openai.com/blog/gpt-4-turbo-vision",
                    "date": "2024-01-15"
                },
                {
                    "title": "Google Cloud Announces New AI Infrastructure",
                    "snippet": "Google Cloud has unveiled new AI infrastructure designed to support large-scale machine learning workloads. The new TPU v5 chips promise 2x better performance for AI training.",
                    "url": "https://cloud.google.com/blog/ai-infrastructure",
                    "date": "2024-01-14"
                },
                {
                    "title": "Microsoft Copilot Gets Memory Enhancement",
                    "snippet": "Microsoft has enhanced Copilot with memory capabilities, allowing it to remember user preferences and conversation history across sessions. This makes the AI assistant more personalized and efficient.",
                    "url": "https://microsoft.com/copilot-memory",
                    "date": "2024-01-13"
                }
            ]
            
            return mock_results
            
        except Exception as e:
            print(f"❌ Error searching web: {e}")
            return []
    
    def analyze_news_for_summary(self, news_articles: List[Dict]) -> Dict[str, str]:
        """
        Analyze news articles and extract key information for summary
        """
        if not news_articles:
            return self.get_fallback_content()
        
        # Select the most interesting/recent article
        selected_article = news_articles[0]
        
        # Extract and format information
        title = selected_article.get("title", "")
        snippet = selected_article.get("snippet", "")
        
        # Generate summary content
        content = {
            "highlight": self.clean_title(title),
            "description": self.simplify_description(snippet),
            "what": self.extract_what(snippet),
            "why_matters": self.extract_why_matters(snippet),
            "cool_factor": self.extract_cool_factor(snippet),
            "takeaway": self.generate_takeaway(snippet)
        }
        
        return content
    
    def clean_title(self, title: str) -> str:
        """Clean and format the title"""
        # Remove common news prefixes
        title = re.sub(r'^(Breaking:|BREAKING:|News:|NEW:)\s*', '', title)
        # Limit length
        if len(title) > 60:
            title = title[:57] + "..."
        return title
    
    def simplify_description(self, snippet: str) -> str:
        """Simplify technical description for general audience"""
        # Remove technical jargon and simplify
        description = snippet.replace("infrastructure", "computer systems")
        description = description.replace("multimodal", "multi-format")
        description = description.replace("workloads", "tasks")
        
        # Limit to 2 sentences
        sentences = description.split('. ')
        if len(sentences) > 2:
            description = '. '.join(sentences[:2]) + '.'
        
        return description
    
    def extract_what(self, snippet: str) -> str:
        """Extract 'what' information in simple terms"""
        # Look for key technology terms
        if "GPT" in snippet or "language model" in snippet:
            return "Advanced AI that can understand and generate human-like text"
        elif "cloud" in snippet.lower():
            return "Internet-based computing services for businesses"
        elif "vision" in snippet.lower() or "image" in snippet.lower():
            return "AI that can see and understand pictures"
        elif "memory" in snippet.lower():
            return "AI system that remembers past conversations"
        else:
            return "New AI technology that helps people work more efficiently"
    
    def extract_why_matters(self, snippet: str) -> str:
        """Extract why this matters to regular people"""
        if "performance" in snippet.lower():
            return "Makes AI tools faster and more reliable for daily use"
        elif "personalized" in snippet.lower():
            return "Creates more helpful and customized AI experiences"
        elif "vision" in snippet.lower() or "image" in snippet.lower():
            return "Allows AI to help with visual tasks like photo editing"
        elif "infrastructure" in snippet.lower():
            return "Improves the foundation that powers AI applications"
        else:
            return "Makes AI more accessible and useful for everyone"
    
    def extract_cool_factor(self, snippet: str) -> str:
        """Extract an interesting detail"""
        if "2x" in snippet or "twice" in snippet:
            return "Delivers twice the performance of previous versions"
        elif "vision" in snippet.lower():
            return "Can analyze photos and understand what's in them"
        elif "memory" in snippet.lower():
            return "Remembers your preferences even after weeks"
        elif "multimodal" in snippet:
            return "Works with text, images, and audio all at once"
        else:
            return "Uses cutting-edge technology that wasn't possible last year"
    
    def generate_takeaway(self, snippet: str) -> str:
        """Generate a simple takeaway paragraph"""
        if "GPT" in snippet or "language" in snippet:
            return "Think of this as your AI assistant getting smarter and more helpful. It's like having a research partner who can understand complex documents and help you write better emails, reports, and creative content."
        elif "cloud" in snippet.lower():
            return "This is like upgrading the engine that powers your favorite apps. Companies can now build faster, smarter AI tools that work better on your phone and computer."
        elif "vision" in snippet.lower():
            return "Imagine showing your AI assistant a photo and having it explain what's happening or help you edit it. This brings us closer to AI that truly understands our visual world."
        elif "memory" in snippet.lower():
            return "This is like your AI assistant finally getting a good memory. Instead of starting fresh every time, it remembers you prefer bullet points or that you're working on a specific project."
        else:
            return "This advancement makes AI more practical for everyday tasks. Whether you're a student, professional, or just curious about technology, these improvements make AI tools more helpful and easier to use."
    
    def get_fallback_content(self) -> Dict[str, str]:
        """Fallback content if web search fails"""
        return {
            "highlight": "AI Development Continues at Rapid Pace",
            "description": "The AI industry keeps advancing with new models, tools, and capabilities being released regularly. Companies are focusing on making AI more accessible and useful for everyday tasks.",
            "what": "Ongoing improvements to AI technology and applications",
            "why_matters": "Makes AI tools more helpful and accessible to everyone",
            "cool_factor": "New AI capabilities emerge almost weekly",
            "takeaway": "AI technology is evolving so quickly that what seemed impossible last year is becoming normal today. This rapid progress means more helpful AI tools for work, creativity, and daily life are constantly being developed."
        }
    
    def generate_daily_summary(self, search_query: Optional[str] = None) -> Dict[str, str]:
        """
        Generate a complete daily summary from web search
        """
        print("🤖 Starting automated AI news generation...")
        
        # Use provided query or pick a random one
        if not search_query:
            import random
            search_query = random.choice(self.search_terms)
        
        # Search for news
        news_results = self.search_web_news(search_query)
        
        # Analyze and format
        content = self.analyze_news_for_summary(news_results)
        
        # Ensure word count is under 100
        total_words = self.generator.count_words(
            content['description'] + content['what'] + 
            content['why_matters'] + content['cool_factor'] + content['takeaway']
        )
        
        print(f"📊 Generated summary with {total_words} words")
        
        if total_words > 100:
            print("⚠️  Summary is over 100 words, trimming...")
            content = self.trim_content(content)
        
        return content
    
    def trim_content(self, content: Dict[str, str]) -> Dict[str, str]:
        """Trim content to stay under 100 words"""
        # Shorten the takeaway paragraph first
        takeaway_words = content['takeaway'].split()
        if len(takeaway_words) > 40:
            content['takeaway'] = ' '.join(takeaway_words[:40]) + '...'
        
        # Shorten description if still too long
        description_words = content['description'].split()
        if len(description_words) > 25:
            content['description'] = ' '.join(description_words[:25]) + '...'
        
        return content
    
    def save_daily_summary(self, content: Dict[str, str]) -> str:
        """Save the daily summary as HTML"""
        # Generate HTML
        html_content = self.generator.generate_html_email(content)
        
        # Save with timestamp
        today = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"automated_daily_summary_{today}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Also save markdown version
        markdown_content = self.generator.create_summary(content)
        md_filename = f"automated_daily_summary_{today}.md"
        
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Saved files:")
        print(f"   - {filename}")
        print(f"   - {md_filename}")
        
        return filename

# Example usage with API integration placeholder
def main():
    # Initialize generator
    generator = AutomatedNewsGenerator()
    
    # You can specify a search query or let it choose randomly
    search_query = "latest AI developments 2024"  # or None for random
    
    # Generate summary
    content = generator.generate_daily_summary(search_query)
    
    # Save as HTML
    html_file = generator.save_daily_summary(content)
    
    print(f"\n🎉 Daily AI summary ready!")
    print(f"📧 Copy content from: {html_file}")
    print(f"📊 Word count: {generator.generator.count_words(content['description'] + content['what'] + content['why_matters'] + content['cool_factor'] + content['takeaway'])}")

if __name__ == "__main__":
    main()
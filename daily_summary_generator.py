#!/usr/bin/env python3
"""
Daily AI & Cloud Summary Generator
Creates concise, readable summaries for email newsletters
"""

import datetime
import re
from typing import Dict, List

class DailySummaryGenerator:
    def __init__(self):
        self.word_limit = 100
        self.template_structure = {
            "highlight": "",
            "description": "",
            "what": "",
            "why_matters": "",
            "cool_factor": "",
            "takeaway": ""
        }
    
    def count_words(self, text: str) -> int:
        """Count words in text, excluding markdown and HTML"""
        # Remove markdown and HTML tags
        clean_text = re.sub(r'<[^>]+>', '', text)
        clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean_text)
        clean_text = re.sub(r'\*([^*]+)\*', r'\1', clean_text)
        
        # Count words
        words = clean_text.split()
        return len(words)
    
    def create_summary(self, content: Dict[str, str]) -> str:
        """Generate markdown summary from content dictionary"""
        today = datetime.date.today().strftime("%B %d, %Y")
        
        summary = f"""# Daily AI & Cloud Snapshot 📡

## Today's Highlight

**{content['highlight']}**
{content['description']}

## Quick Facts 🔍

• **What**: {content['what']}
• **Why it matters**: {content['why_matters']}
• **Cool factor**: {content['cool_factor']}

## One-Minute Takeaway 💡

{content['takeaway']}

---

**Word Count**: {self.count_words(content['description'] + content['what'] + content['why_matters'] + content['cool_factor'] + content['takeaway'])} words
**Read Time**: 1 minute
**Date**: {today}

---"""
        
        return summary
    
    def generate_html_email(self, content: Dict[str, str]) -> str:
        """Generate HTML email version"""
        today = datetime.date.today().strftime("%B %d, %Y")
        word_count = self.count_words(content['description'] + content['what'] + content['why_matters'] + content['cool_factor'] + content['takeaway'])
        
        html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily AI & Cloud Snapshot</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f8fafc; }}
        .container {{ max-width: 600px; margin: 0 auto; background-color: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
        .header {{ background-color: #3B82F6; color: white; padding: 20px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; }}
        .header p {{ margin: 5px 0 0 0; font-size: 14px; opacity: 0.9; }}
        .content {{ padding: 30px; }}
        .highlight {{ color: #1e293b; font-size: 20px; font-weight: bold; margin-bottom: 15px; }}
        .description {{ color: #475569; font-size: 14px; line-height: 1.5; margin-bottom: 25px; }}
        .facts {{ margin-bottom: 25px; }}
        .facts h3 {{ color: #10B981; font-size: 16px; margin-bottom: 15px; }}
        .fact {{ display: flex; align-items: flex-start; margin-bottom: 10px; }}
        .fact-dot {{ width: 6px; height: 6px; background-color: #3B82F6; border-radius: 50%; margin-right: 15px; margin-top: 8px; }}
        .fact-label {{ font-weight: bold; color: #1e293b; margin-right: 10px; }}
        .fact-text {{ color: #475569; flex: 1; }}
        .takeaway {{ margin-bottom: 25px; }}
        .takeaway h3 {{ color: #F59E0B; font-size: 16px; margin-bottom: 15px; }}
        .takeaway p {{ color: #475569; font-size: 14px; line-height: 1.6; margin: 0; }}
        .footer {{ background-color: #f1f5f9; padding: 15px; text-align: center; font-size: 12px; color: #64748b; }}
        .footer span {{ margin: 0 15px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📡 Daily AI & Cloud Snapshot</h1>
            <p>{today}</p>
        </div>
        
        <div class="content">
            <div class="highlight">{content['highlight']}</div>
            
            <div class="description">
                {content['description']}
            </div>
            
            <div class="facts">
                <h3>🔍 Quick Facts</h3>
                <div class="fact">
                    <div class="fact-dot"></div>
                    <div class="fact-label">What:</div>
                    <div class="fact-text">{content['what']}</div>
                </div>
                <div class="fact">
                    <div class="fact-dot"></div>
                    <div class="fact-label">Why it matters:</div>
                    <div class="fact-text">{content['why_matters']}</div>
                </div>
                <div class="fact">
                    <div class="fact-dot"></div>
                    <div class="fact-label">Cool factor:</div>
                    <div class="fact-text">{content['cool_factor']}</div>
                </div>
            </div>
            
            <div class="takeaway">
                <h3>💡 One-Minute Takeaway</h3>
                <p>{content['takeaway']}</p>
            </div>
        </div>
        
        <div class="footer">
            <span>📊 {word_count} words</span>
            <span>⏱️ 1 minute read</span>
            <span>🤖 Daily AI Snapshot</span>
        </div>
    </div>
</body>
</html>"""
        
        return html_template
    
    def get_example_topics(self) -> List[str]:
        """Return list of example AI/Cloud topics for inspiration"""
        return [
            "New AI model releases (GPT, Claude, Gemini)",
            "Cloud service updates (AWS, Azure, Google Cloud)",
            "AI tool launches (productivity, coding, creative)",
            "Machine learning breakthroughs",
            "AI ethics and policy news",
            "Cloud security updates",
            "AI hardware developments",
            "Open source AI projects",
            "AI in specific industries (healthcare, finance, etc.)",
            "Cloud cost optimization tools",
            "AI developer tools and frameworks",
            "Edge computing advances"
        ]

# Example usage
if __name__ == "__main__":
    generator = DailySummaryGenerator()
    
    # Example content
    example_content = {
        "highlight": "OpenAI's ChatGPT Gets Memory Feature",
        "description": "ChatGPT can now remember details from your conversations across different chats. This means it won't forget your preferences, work style, or personal details you've shared before.",
        "what": "AI assistant that remembers past conversations and user preferences",
        "why_matters": "Makes AI interactions more personal and efficient for daily use",
        "cool_factor": "It can remember your coffee preference and writing style for months",
        "takeaway": "Think of it like having a personal assistant who actually remembers what you told them last week. Instead of repeating yourself every time, ChatGPT will know you're a teacher who needs simple explanations or a developer who prefers code examples. This makes AI more helpful for regular tasks."
    }
    
    # Generate summary
    markdown_summary = generator.create_summary(example_content)
    html_email = generator.generate_html_email(example_content)
    
    print("Markdown Summary:")
    print(markdown_summary)
    print("\n" + "="*50 + "\n")
    
    # Save files
    with open("daily_summary.md", "w") as f:
        f.write(markdown_summary)
    
    with open("daily_email.html", "w") as f:
        f.write(html_email)
    
    print("Files saved:")
    print("- daily_summary.md")
    print("- daily_email.html")
    
    print("\nTopic ideas for future summaries:")
    for topic in generator.get_example_topics():
        print(f"• {topic}")
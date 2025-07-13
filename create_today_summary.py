#!/usr/bin/env python3
"""
Quick Daily Summary Creator
Edit the content below and run this script to generate your daily summary
"""

from daily_summary_generator import DailySummaryGenerator

def create_todays_summary():
    # 🔧 EDIT THIS SECTION WITH TODAY'S CONTENT
    content = {
        "highlight": "Claude 3.5 Sonnet Gets Computer Control",
        "description": "Anthropic's latest AI can now see and interact with computer screens, clicking buttons and typing text just like a human user. This breakthrough makes AI capable of using any software application.",
        "what": "AI that can control computers by seeing screens and clicking like humans",
        "why_matters": "Could automate repetitive computer tasks for millions of workers",
        "cool_factor": "Can play video games and fill out forms without special programming",
        "takeaway": "Imagine having an AI assistant that can actually use your computer programs for you. Instead of just chatting, it can open apps, fill spreadsheets, and handle boring tasks while you focus on creative work. This is like having a super-smart intern who never gets tired."
    }
    
    # Generate the summary
    generator = DailySummaryGenerator()
    
    # Create both versions
    markdown_summary = generator.create_summary(content)
    html_email = generator.generate_html_email(content)
    
    # Save files with today's date
    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    with open(f"daily_summary_{today}.md", "w") as f:
        f.write(markdown_summary)
    
    with open(f"daily_email_{today}.html", "w") as f:
        f.write(html_email)
    
    print(f"✅ Created files:")
    print(f"   - daily_summary_{today}.md")
    print(f"   - daily_email_{today}.html")
    print(f"\n📊 Word count: {generator.count_words(content['description'] + content['what'] + content['why_matters'] + content['cool_factor'] + content['takeaway'])}")
    print(f"📧 Ready to copy into your email!")

if __name__ == "__main__":
    create_todays_summary()
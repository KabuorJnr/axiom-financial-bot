"""
Vercel serverless function handler for AXIOM Streamlit app
"""

import subprocess
import sys
import os
from urllib.parse import urlparse, parse_qs

def handler(request):
    """
    Vercel serverless function handler for Streamlit app
    """
    
    # Set environment variables for Streamlit
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'
    os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
    os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'true'
    
    try:
        # Run streamlit as subprocess
        cmd = [sys.executable, '-m', 'streamlit', 'run', 'axiom_bot.py', '--server.port', '8501', '--server.headless', 'true']
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/html',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': '''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>AXIOM Financial Markets Bot</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; background: #0e1117; color: #fafafa; }
                        .container { max-width: 800px; margin: 0 auto; text-align: center; }
                        .title { color: #00ff88; font-size: 2em; margin-bottom: 20px; }
                        .subtitle { color: #888; margin-bottom: 30px; }
                        .button { background: #00ff88; color: #000; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }
                        .features { margin: 30px 0; }
                        .feature { margin: 10px 0; padding: 10px; background: #1a1a1a; border-radius: 5px; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1 class="title">🤖 AXIOM Financial Markets Bot</h1>
                        <p class="subtitle">"Part mentor, part sparring partner, all market brain"</p>
                        
                        <div class="features">
                            <div class="feature">📊 Real-time Treasury Yields & USD Data</div>
                            <div class="feature">🤖 Dual AI System (OpenAI + Gemini)</div>
                            <div class="feature">📈 Interactive Bond Yields vs USD Analysis</div>
                            <div class="feature">🎯 Professional Trading Terminal UI</div>
                        </div>
                        
                        <p><strong>Note:</strong> Streamlit apps require a different deployment approach on Vercel.</p>
                        <p>For best performance, deploy AXIOM on:</p>
                        <ul style="text-align: left; display: inline-block;">
                            <li><strong>Streamlit Community Cloud</strong> (Recommended)</li>
                            <li><strong>Heroku</strong></li>
                            <li><strong>Railway</strong></li>
                            <li><strong>Google Cloud Run</strong></li>
                        </ul>
                        
                        <p style="margin-top: 30px;">
                            <a href="https://github.com/KabuorJnr/axiom-financial-bot" class="button">
                                View Source Code on GitHub
                            </a>
                        </p>
                    </div>
                </body>
                </html>
                '''
            }
        else:
            return {
                'statusCode': 500,
                'body': f'Error running Streamlit: {result.stderr}'
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Server error: {str(e)}'
        }

# For Vercel
app = handler
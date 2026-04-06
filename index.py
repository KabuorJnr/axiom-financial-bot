"""
Vercel deployment wrapper for AXIOM Streamlit app
"""

from axiom_bot import main
import os

# Set environment for production
os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
os.environ.setdefault('STREAMLIT_SERVER_PORT', '8080')

if __name__ == "__main__":
    main()
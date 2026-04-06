"""Configuration settings for the Financial Markets Bot."""

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
FRED_API_KEY = os.getenv("FRED_API_KEY")

# App Settings
APP_TITLE = os.getenv("APP_TITLE", "AXIOM - Financial Markets AI")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4")
ENABLE_CHARTS = os.getenv("ENABLE_CHARTS", "True").lower() == "true"
ENABLE_REAL_TIME_DATA = os.getenv("ENABLE_REAL_TIME_DATA", "True").lower() == "true"

# Market Data Settings
BOND_YIELD_SYMBOL = "^TNX"  # 10-Year Treasury Yield
USD_INDEX_SYMBOL = "DX-Y.NYB"  # US Dollar Index
EUR_USD_SYMBOL = "EURUSD=X"
GBP_USD_SYMBOL = "GBPUSD=X"

# FRED Economic Data Series
FRED_SERIES = {
    "10_year_yield": "DGS10",
    "2_year_yield": "DGS2", 
    "fed_rate": "FEDFUNDS",
    "inflation": "CPIAUCSL",
    "gdp": "GDP"
}

# Personality Settings
BOT_NAME = "AXIOM"
BOT_DESCRIPTION = "Part mentor, part sparring partner, all market brain"
BOT_PERSONALITY = "direct, analytical, no-nonsense market expert"
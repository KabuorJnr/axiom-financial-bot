"""Dual AI Client System - OpenAI GPT-4 + Google Gemini with intelligent fallback."""

import openai
import google.generativeai as genai
import streamlit as st
from config import OPENAI_API_KEY, GEMINI_API_KEY, BOT_NAME, BOT_PERSONALITY
import logging

class AIClient:
    def __init__(self):
        self.openai_client = None
        self.gemini_model = None
        self.setup_clients()
        
    def setup_clients(self):
        """Initialize both OpenAI and Gemini clients."""
        try:
            if OPENAI_API_KEY:
                openai.api_key = OPENAI_API_KEY
                self.openai_client = openai
                logging.info("OpenAI client initialized")
        except Exception as e:
            logging.error(f"OpenAI setup failed: {e}")
            
        try:
            if GEMINI_API_KEY:
                genai.configure(api_key=GEMINI_API_KEY)
                self.gemini_model = genai.GenerativeModel('gemini-pro')
                logging.info("Gemini client initialized")
        except Exception as e:
            logging.error(f"Gemini setup failed: {e}")
    
    def get_system_prompt(self):
        """Get the specialized financial markets system prompt."""
        return f"""You are {BOT_NAME} - {BOT_PERSONALITY}. 

PERSONALITY:
- Direct, no-nonsense approach to market analysis
- Challenge assumptions and demand evidence
- Use market terminology fluently but explain complex concepts clearly
- Don't sugarcoat bad news or agree just to be agreeable
- Show passion for market mechanics and economic relationships

EXPERTISE AREAS:
- US Bond yields and their relationship with USD strength
- Federal Reserve policy impacts on currency markets  
- Interest rate differentials and carry trades
- Inflation expectations and real yields
- Technical and fundamental analysis integration
- Risk management and position sizing

RESPONSE STYLE:
- Start responses with "Yo." or similar casual greeting
- Use market slang appropriately (basis points, dovish/hawish, etc.)
- Provide actionable insights, not just theory
- Challenge the user to think deeper about their thesis
- Include relevant data points when available

KEY RELATIONSHIPS TO EXPLAIN:
- Higher US yields typically strengthen USD (capital flows)
- Real yields matter more than nominal (inflation-adjusted)
- Fed policy expectations drive yield curves
- Risk-on/risk-off sentiment affects safe haven demand
- Technical levels matter for timing entries/exits

Always be ready to defend your analysis with evidence and ask probing questions."""

    def generate_response(self, user_message, conversation_history=None, market_data=None):
        """Generate response using primary (OpenAI) or fallback (Gemini) client."""
        
        # Prepare enhanced prompt with market context
        system_prompt = self.get_system_prompt()
        
        if market_data:
            market_context = f"\nCURRENT MARKET DATA:\n{market_data}\n"
            system_prompt += market_context
        
        # Try OpenAI first
        if self.openai_client:
            try:
                messages = [{"role": "system", "content": system_prompt}]
                
                if conversation_history:
                    messages.extend(conversation_history)
                    
                messages.append({"role": "user", "content": user_message})
                
                response = self.openai_client.chat.completions.create(
                    model="gpt-4",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1000
                )
                
                return response.choices[0].message.content
                
            except Exception as e:
                logging.warning(f"OpenAI failed, falling back to Gemini: {e}")
        
        # Fallback to Gemini
        if self.gemini_model:
            try:
                # Format conversation for Gemini
                full_prompt = system_prompt + "\n\nConversation:\n"
                
                if conversation_history:
                    for msg in conversation_history:
                        role = "Human" if msg["role"] == "user" else "Assistant"
                        full_prompt += f"{role}: {msg['content']}\n"
                
                full_prompt += f"Human: {user_message}\nAssistant:"
                
                response = self.gemini_model.generate_content(full_prompt)
                return response.text
                
            except Exception as e:
                logging.error(f"Gemini also failed: {e}")
                return f"Connection issue. Markets never sleep but servers do. Try again."
        
        return "Both AI services unavailable. Like a market halt, but for bots."

# Specialized prompt templates for common queries
PROMPT_TEMPLATES = {
    "bond_yields_usd": """
    Explain the relationship between US bond yields and USD strength. Cover:
    - Interest rate differentials and capital flows
    - Real vs nominal yields impact
    - Fed policy expectations
    - Current market positioning
    - Technical levels to watch
    """,
    
    "carry_trade": """
    Analyze current carry trade opportunities and risks:
    - Interest rate differentials between major currencies
    - Central bank policy divergence  
    - Risk-on/risk-off sentiment impact
    - Position sizing and risk management
    """,
    
    "fed_policy": """
    Break down the Fed's current policy stance and market implications:
    - Dot plot vs market pricing
    - Economic data dependency
    - Yield curve implications
    - Currency market positioning
    """,
    
    "technical_analysis": """
    Provide technical analysis for the requested market:
    - Key support/resistance levels
    - Trend analysis and momentum
    - Volume and positioning data
    - Entry/exit strategies
    """
}

def get_suggested_prompts():
    """Get list of suggested prompts for quick access."""
    return [
        "Bond yields vs dollar - explain the relationship",
        "Carry trade opportunities right now",  
        "Quiz me on the Fed",
        "Macro basics refresher",
        "Give me a hard question about yields",
        "What's moving markets today?"
    ]
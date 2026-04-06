# AXIOM Financial Markets Chatbot 📈🤖

**"Yo. I'm AXIOM — part mentor, part sparring partner, all market brain. I don't sugarcoat and I don't agree just to be agreeable."**

An impressive financial markets chatbot built with Python, Streamlit, and dual AI integration (OpenAI + Google Gemini). Specialized in explaining complex market relationships, particularly **US bond yields vs USD dynamics**.

## 🚀 Features

### 🧠 Dual AI System
- **Primary**: OpenAI GPT-4 with specialized financial prompts
- **Fallback**: Google Gemini Pro for redundancy 
- **Smart Context**: Real-time market data integration
- **Market Personality**: Direct, no-nonsense analysis style

### 📊 Real-Time Market Data
- Live Treasury yields and major FX rates
- Historical correlation analysis (Yield-USD relationship)
- Economic indicators from FRED API
- Interactive charts with Plotly

### 🎨 Premium UI/UX
- AXIOM-inspired dark theme with green accents
- Real-time market data sidebar
- Suggested prompts for quick starts
- Professional chart visualizations
- Responsive design

### 📈 Advanced Analytics
- Yield curve visualization
- Asset correlation heatmaps
- Volatility analysis charts
- Economic indicators dashboard
- Market sentiment gauges

## 🛠️ Technical Stack

```
Frontend: Streamlit + Custom CSS
AI Models: OpenAI GPT-4, Google Gemini Pro  
Market Data: Yahoo Finance, FRED API
Charts: Plotly Interactive Visualizations
Deployment: Local Streamlit Server
```

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup API Keys
```bash
# Copy and edit environment file
cp .env.example .env

# Add your API keys:
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here  
FRED_API_KEY=your_fred_key_here (optional)
```

### 3. Launch the Bot
```bash
streamlit run axiom_bot.py
```

### 4. Access the Interface
Open your browser to: `http://localhost:8501`

## 🎯 Core Capabilities

### Market Analysis Expertise
- **Bond Yields vs USD**: Deep analysis of interest rate differentials and capital flows
- **Fed Policy Impact**: How central bank decisions affect currency markets
- **Carry Trade Analysis**: Risk-on/risk-off sentiment and positioning
- **Technical Analysis**: Support/resistance levels and momentum indicators

### Interactive Features
- **Live Market Updates**: Real-time data refresh
- **Suggested Prompts**: Quick access to common queries
- **Chart Integration**: Visual confirmation of analysis
- **Conversation Memory**: Context-aware responses

### Sample Queries
```
"US bond yields and the dollar — explain the relationship"
"Carry trade opportunities right now" 
"Quiz me on the Fed"
"Give me a hard question about yields"
"What's moving markets today?"
```

## 📋 API Keys Setup

### OpenAI (Required)
1. Get API key from: https://platform.openai.com/api-keys
2. Add to `.env`: `OPENAI_API_KEY=your_key`

### Google Gemini (Fallback)
1. Get API key from: https://makersuite.google.com/app/apikey
2. Add to `.env`: `GEMINI_API_KEY=your_key`

### FRED API (Optional - for enhanced economic data)
1. Register at: https://fred.stlouisfed.org/docs/api/api_key.html
2. Add to `.env`: `FRED_API_KEY=your_key`

## 🎨 UI Customization

The bot features a custom dark theme inspired by professional trading terminals:

- **Colors**: Matrix green (#00ff88) with dark backgrounds
- **Typography**: Clean, professional fonts with glowing effects
- **Layout**: Sidebar controls + main chat + live charts
- **Responsive**: Works on desktop and mobile

## 🔧 Advanced Configuration

### Market Data Sources
```python
# Customize in config.py
BOND_YIELD_SYMBOL = "^TNX"        # 10-Year Treasury
USD_INDEX_SYMBOL = "DX-Y.NYB"     # Dollar Index  
EUR_USD_SYMBOL = "EURUSD=X"       # EUR/USD Rate
```

### AI Personality Tuning
```python
# Modify prompts in ai_client.py
BOT_PERSONALITY = "direct, analytical, no-nonsense market expert"
```

### Chart Customization
- Edit `advanced_charts.py` for new visualizations
- Modify `axiom_bot.py` chart layouts
- Add new market data sources in `market_data.py`

## 🚨 Error Handling

The bot includes robust error handling:
- **API Failures**: Automatic fallback between AI providers
- **Data Issues**: Graceful degradation when market data unavailable  
- **Network Problems**: User-friendly error messages
- **Logging**: Comprehensive error tracking

## 🎓 Educational Focus

Perfect for learning about:
- **Interest Rate Dynamics**: How yields affect currency values
- **Central Bank Policy**: Fed decisions and market reactions
- **Risk Management**: Position sizing and correlation analysis  
- **Technical Analysis**: Chart patterns and momentum indicators

## 🔄 Real-Time Features

- **Live Data Updates**: Market data refreshes automatically
- **Dynamic Charts**: Interactive Plotly visualizations  
- **Correlation Analysis**: Real-time yield-USD relationship tracking
- **Economic Indicators**: Latest Fed rates, inflation, GDP data

## 📱 Deployment Options

### Local Development
```bash
streamlit run axiom_bot.py --server.port 8501
```

### Production Deployment  
- **Streamlit Community Cloud**: Connect GitHub repo
- **Heroku**: Add Procfile for web dyno
- **AWS/GCP**: Docker containerization
- **DigitalOcean**: App Platform deployment

## 🤝 Contributing

Feel free to enhance the bot:
1. Add new market data sources
2. Implement additional chart types  
3. Enhance AI prompts and personality
4. Improve error handling and UX

## ⚠️ Disclaimers

- **Educational Purpose**: Not investment advice
- **Market Data**: May have delays or inaccuracies
- **AI Responses**: For educational discussion only
- **Risk Warning**: Trading involves substantial risk

## 📄 License

This project is for educational and demonstration purposes.

---

**Built with ❤️ for financial markets education and AI innovation.**

*"Ask me anything — macro, FX, bonds, equities, trading psychology. But come ready to defend your thesis."* - AXIOM
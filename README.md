# AXIOM Financial Markets Bot

🤖 **Professional financial markets AI assistant**

"Yo. I'm AXIOM — part mentor, part sparring partner, all market brain. I don't sugarcoat and I don't agree just to be agreeable."

## 🚀 **Live Demo**
**Coming Soon**: https://axiom-financial-bot.vercel.app

## ⚡ **Features**

### 🧠 **Dual AI System**
- **Primary**: OpenAI GPT-4 with specialized financial prompts
- **Fallback**: Google Gemini Pro for redundancy
- **Smart Context**: Real-time market data integration

### 📊 **Real-Time Market Data**
- Live Treasury yields and USD Index
- Historical correlation analysis
- FRED economic indicators
- Interactive Plotly charts

### 🎨 **Professional UI**
- Dark theme with Matrix-green styling
- Real-time market data sidebar
- Suggested prompts for quick analysis
- Mobile-responsive design

## 🛠️ **Tech Stack**
```
Frontend: Streamlit + Custom CSS
AI: OpenAI GPT-4, Google Gemini Pro
Data: Yahoo Finance, FRED API
Charts: Plotly Interactive
Deploy: Vercel
```

## 📈 **Perfect for Learning**
- **Bond Yields vs USD** relationship analysis
- **Fed Policy Impact** on currency markets
- **Carry Trade** opportunities and risks
- **Technical Analysis** and market timing

## 🚀 **Quick Start**

### 1. Clone & Install
```bash
git clone https://github.com/KabuorJnr/axiom-financial-bot.git
cd axiom-financial-bot
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Launch
```bash
streamlit run axiom_bot.py
# Opens at http://localhost:8501
```

## 🔑 **API Keys Setup**

### OpenAI (Primary)
1. Get key: https://platform.openai.com/api-keys
2. Add to `.env`: `OPENAI_API_KEY=sk-your-key`

### Google Gemini (Fallback)
1. Get key: https://makersuite.google.com/app/apikey
2. Add to `.env`: `GEMINI_API_KEY=your-key`

### FRED API (Optional - Enhanced Data)
1. Register: https://fred.stlouisfed.org/docs/api/api_key.html
2. Add to `.env`: `FRED_API_KEY=your-key`

## 💡 **Sample Questions**
```
"US bond yields and the dollar — explain the relationship"
"Carry trade opportunities right now"
"Quiz me on the Fed"
"Give me a hard question about yields"
"What's moving markets today?"
```

## 🔥 **Key Relationships Explained**
- **Higher US yields** → **Stronger USD** (capital flows)
- **Real yields** matter more than nominal (inflation-adjusted)
- **Fed policy expectations** drive yield curves
- **Risk-on/risk-off** affects safe haven demand

## 🌐 **Deployment**

### Vercel (Recommended)
1. Fork this repository
2. Connect to Vercel
3. Set environment variables
4. Deploy automatically

### Local Development
```bash
streamlit run axiom_bot.py --server.port 8501
```

## ⚠️ **Disclaimers**
- **Educational purpose only** - Not investment advice
- **Market data** may have delays
- **AI responses** for discussion only
- **Trading involves substantial risk**

---

**Built with ❤️ for financial education**

*"Ask me anything — macro, FX, bonds, equities, trading psychology. But come ready to defend your thesis."* - AXIOM
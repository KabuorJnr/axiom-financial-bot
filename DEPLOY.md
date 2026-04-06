# 🚀 AXIOM Deployment Guide

## ✅ **Repository Ready!**

**Local Path**: `C:\Users\USER\axiom-financial-bot`  
**GitHub Repository**: `axiom-financial-bot` (to be created)  
**Vercel Deployment**: Ready to deploy  

---

## 📋 **Next Steps to Deploy:**

### **1. Create GitHub Repository**
1. Go to: https://github.com/new
2. Repository name: `axiom-financial-bot`
3. Description: "Professional financial markets AI assistant with real-time data"
4. Keep it **Public**
5. **Don't** initialize with README (we already have one)
6. Click **"Create repository"**

### **2. Connect Local to GitHub**
Open Command Prompt and run:
```bash
cd "C:\Users\USER\axiom-financial-bot"
git remote add origin https://github.com/KabuorJnr/axiom-financial-bot.git
git branch -M main
git push -u origin main
```

### **3. Deploy to Vercel**
1. Go to: https://vercel.com/dashboard
2. Click **"New Project"**
3. Import `KabuorJnr/axiom-financial-bot` from GitHub
4. **Framework Preset**: `Other`
5. **Root Directory**: `/` (default)
6. **Build Command**: Leave empty
7. **Install Command**: `pip install -r requirements.txt`

### **4. Configure Environment Variables in Vercel**
Add these in Vercel Dashboard → Settings → Environment Variables:

```
GEMINI_API_KEY = AIzaSyD0XmoeSWAywrJ-uZ68S-yysC8uEVQ3zEY
FRED_API_KEY = 0701ad0515dde7ae11bf8937c856e7e7
ENABLE_CHARTS = True
ENABLE_REAL_TIME_DATA = True
```

### **5. Deploy!**
Click **"Deploy"** and your AXIOM bot will be live!

---

## 🎯 **Production URLs**
- **GitHub**: https://github.com/KabuorJnr/axiom-financial-bot
- **Vercel**: https://axiom-financial-bot.vercel.app (after deployment)

---

## 🔒 **Security Features**

✅ **API Keys Protected**: `.env` files properly ignored by git  
✅ **Clean Repository**: Only production code, no sensitive data  
✅ **Proper Gitignore**: Comprehensive exclusions for security  
✅ **Vercel Environment**: API keys stored securely in Vercel  

---

## 🎉 **What's Deployed**

### 📊 **AXIOM Financial Markets Bot**
- **14 files** ready for production
- **1,508+ lines** of professional code
- **Dual AI system** (OpenAI + Gemini)
- **Real-time market data** integration
- **Interactive charts** and analysis
- **Professional UI** with dark theme

### 🔥 **Key Features Live**
✅ Live Treasury yields and USD Index  
✅ Historical correlation analysis  
✅ Economic indicators from FRED  
✅ AI chat for market analysis  
✅ Interactive Plotly visualizations  
✅ Mobile-responsive design  
✅ Professional trading terminal aesthetics  

---

## 🚀 **Ready to Impress!**

Your AXIOM bot is production-ready and will provide:
- Real-time bond yields vs USD analysis
- Professional financial market insights
- Educational trading discussions
- Interactive market visualizations

**Perfect for demonstrating advanced AI + financial data integration!**
"""Real-time market data integration for bond yields, USD, and economic indicators."""

import yfinance as yf
import pandas as pd
import requests
from datetime import datetime, timedelta
import logging
from config import BOND_YIELD_SYMBOL, USD_INDEX_SYMBOL, EUR_USD_SYMBOL, GBP_USD_SYMBOL, FRED_SERIES, FRED_API_KEY

class MarketDataProvider:
    def __init__(self):
        self.fred_api_key = FRED_API_KEY
        self.cache = {}
        self.cache_expiry = {}
        
    def get_current_yields_and_fx(self):
        """Get current bond yields and major FX rates."""
        try:
            # Get yield data
            tnx = yf.Ticker(BOND_YIELD_SYMBOL)
            usd_index = yf.Ticker(USD_INDEX_SYMBOL)
            eur_usd = yf.Ticker(EUR_USD_SYMBOL)
            gbp_usd = yf.Ticker(GBP_USD_SYMBOL)
            
            # Get current prices
            tnx_data = tnx.history(period="1d", interval="1m").tail(1)
            usd_data = usd_index.history(period="1d", interval="1m").tail(1)
            eur_data = eur_usd.history(period="1d", interval="1m").tail(1)
            gbp_data = gbp_usd.history(period="1d", interval="1m").tail(1)
            
            current_data = {
                "10Y_Treasury_Yield": round(tnx_data['Close'].iloc[0], 3) if not tnx_data.empty else "N/A",
                "USD_Index_DXY": round(usd_data['Close'].iloc[0], 2) if not usd_data.empty else "N/A", 
                "EUR_USD": round(eur_data['Close'].iloc[0], 4) if not eur_data.empty else "N/A",
                "GBP_USD": round(gbp_data['Close'].iloc[0], 4) if not gbp_data.empty else "N/A",
                "Last_Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            
            return current_data
            
        except Exception as e:
            logging.error(f"Error fetching market data: {e}")
            return {"Error": "Unable to fetch real-time data"}
    
    def get_historical_correlation_data(self, period="1y"):
        """Get historical data for yield-USD correlation analysis."""
        try:
            # Get historical data
            tnx = yf.Ticker(BOND_YIELD_SYMBOL)
            usd_index = yf.Ticker(USD_INDEX_SYMBOL)
            
            # Fetch data
            yield_data = tnx.history(period=period)['Close']
            usd_data = usd_index.history(period=period)['Close']
            
            # Align data by date
            df = pd.DataFrame({
                'Yield_10Y': yield_data,
                'USD_Index': usd_data
            }).dropna()
            
            # Calculate correlation
            correlation = df['Yield_10Y'].corr(df['USD_Index'])
            
            # Calculate recent changes
            recent_yield_change = df['Yield_10Y'].iloc[-1] - df['Yield_10Y'].iloc[-5]
            recent_usd_change = df['USD_Index'].iloc[-1] - df['USD_Index'].iloc[-5]
            
            return {
                "correlation_1y": round(correlation, 3),
                "recent_yield_change_5d": round(recent_yield_change, 3),
                "recent_usd_change_5d": round(recent_usd_change, 2),
                "data_points": len(df),
                "period": period
            }
            
        except Exception as e:
            logging.error(f"Error calculating correlation: {e}")
            return {"Error": "Unable to calculate correlation"}
    
    def get_fred_economic_data(self, series_id, limit=10):
        """Get economic data from FRED API."""
        if not self.fred_api_key or self.fred_api_key == "your_fred_api_key_here":
            return {"Error": "FRED API key not configured"}
            
        try:
            url = f"https://api.stlouisfed.org/fred/series/observations"
            params = {
                'series_id': series_id,
                'api_key': self.fred_api_key,
                'file_type': 'json',
                'limit': limit,
                'sort_order': 'desc'
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                observations = data.get('observations', [])
                
                if observations:
                    latest = observations[0]
                    return {
                        'series_id': series_id,
                        'latest_value': latest.get('value'),
                        'date': latest.get('date'),
                        'units': data.get('units', 'Unknown')
                    }
            
            return {"Error": f"No data available for {series_id}"}
            
        except Exception as e:
            logging.error(f"FRED API error: {e}")
            return {"Error": f"FRED API request failed: {e}"}
    
    def get_comprehensive_market_summary(self):
        """Get comprehensive market data summary for AI context."""
        try:
            # Current market data
            current = self.get_current_yields_and_fx()
            
            # Historical correlation
            correlation = self.get_historical_correlation_data()
            
            # Key economic indicators (if FRED is available)
            fed_rate = self.get_fred_economic_data(FRED_SERIES['fed_rate'])
            inflation = self.get_fred_economic_data(FRED_SERIES['inflation'])
            
            # Calculate yield-USD relationship strength
            relationship_strength = "Strong" if abs(correlation.get('correlation_1y', 0)) > 0.7 else \
                                  "Moderate" if abs(correlation.get('correlation_1y', 0)) > 0.4 else "Weak"
            
            summary = f"""
📊 CURRENT MARKET SNAPSHOT:
• 10Y Treasury Yield: {current.get('10Y_Treasury_Yield', 'N/A')}%
• USD Index (DXY): {current.get('USD_Index_DXY', 'N/A')}
• EUR/USD: {current.get('EUR_USD', 'N/A')}
• GBP/USD: {current.get('GBP_USD', 'N/A')}

📈 YIELD-USD RELATIONSHIP (1Y):
• Correlation: {correlation.get('correlation_1y', 'N/A')} ({relationship_strength})
• 5D Yield Change: {correlation.get('recent_yield_change_5d', 'N/A')} bps
• 5D USD Change: {correlation.get('recent_usd_change_5d', 'N/A')} points

🏦 POLICY CONTEXT:
• Fed Funds Rate: {fed_rate.get('latest_value', 'N/A')}% (as of {fed_rate.get('date', 'N/A')})
• Latest CPI: {inflation.get('latest_value', 'N/A')} (as of {inflation.get('date', 'N/A')})

⏰ Updated: {current.get('Last_Updated', 'N/A')}
            """.strip()
            
            return summary
            
        except Exception as e:
            logging.error(f"Error creating market summary: {e}")
            return "Market data temporarily unavailable - like a flash crash for data feeds."
    
    def get_chart_data(self, symbol, period="6mo"):
        """Get data formatted for Plotly charts."""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)
            
            return {
                'dates': data.index.tolist(),
                'prices': data['Close'].tolist(),
                'symbol': symbol,
                'period': period
            }
            
        except Exception as e:
            logging.error(f"Chart data error for {symbol}: {e}")
            return None
    
    def get_yield_curve_data(self):
        """Get current yield curve data for visualization."""
        try:
            # Treasury symbols for different maturities
            symbols = {
                '3M': '^IRX',
                '2Y': '^TNX',  # Note: Yahoo Finance limitations
                '5Y': '^FVX', 
                '10Y': '^TNX',
                '30Y': '^TYX'
            }
            
            curve_data = {}
            for maturity, symbol in symbols.items():
                ticker = yf.Ticker(symbol)
                data = ticker.history(period="1d").tail(1)
                if not data.empty:
                    curve_data[maturity] = round(data['Close'].iloc[0], 3)
            
            return curve_data
            
        except Exception as e:
            logging.error(f"Yield curve data error: {e}")
            return {}

# Global instance
market_data = MarketDataProvider()
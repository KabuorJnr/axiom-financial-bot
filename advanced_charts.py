"""
Advanced chart components for financial markets visualization.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf

class AdvancedCharts:
    
    @staticmethod
    def create_yield_curve_chart():
        """Create real-time yield curve visualization."""
        try:
            # Yield curve data points
            maturities = ['3M', '6M', '1Y', '2Y', '5Y', '10Y', '30Y']
            symbols = ['^IRX', '^IRX', '^IRX', '^TNX', '^FVX', '^TNX', '^TYX']  # Approximation
            
            yields = []
            maturity_values = [0.25, 0.5, 1, 2, 5, 10, 30]  # Years
            
            for symbol in symbols:
                try:
                    ticker = yf.Ticker(symbol)
                    data = ticker.history(period="1d").tail(1)
                    if not data.empty:
                        yields.append(data['Close'].iloc[0])
                    else:
                        yields.append(None)
                except:
                    yields.append(None)
            
            # Create yield curve
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=maturity_values,
                y=yields,
                mode='lines+markers',
                name='Current Yield Curve',
                line=dict(color='#00ff88', width=3),
                marker=dict(size=8, color='#00ff88')
            ))
            
            fig.update_layout(
                title='US Treasury Yield Curve',
                xaxis_title='Maturity (Years)',
                yaxis_title='Yield (%)',
                template='plotly_dark',
                height=300,
                showlegend=False
            )
            
            return fig
            
        except Exception as e:
            return None
    
    @staticmethod
    def create_correlation_heatmap():
        """Create correlation heatmap for major assets."""
        try:
            # Get data for major assets
            symbols = ['^TNX', 'DX-Y.NYB', 'EURUSD=X', 'GBPUSD=X', '^GSPC', 'GC=F']
            names = ['10Y Yield', 'USD Index', 'EUR/USD', 'GBP/USD', 'S&P 500', 'Gold']
            
            data = {}
            for symbol, name in zip(symbols, names):
                try:
                    ticker = yf.Ticker(symbol)
                    hist = ticker.history(period="3mo")['Close'].pct_change().dropna()
                    data[name] = hist
                except:
                    continue
            
            if data:
                df = pd.DataFrame(data).dropna()
                corr_matrix = df.corr()
                
                fig = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='RdBu',
                    zmid=0,
                    text=np.round(corr_matrix.values, 2),
                    texttemplate="%{text}",
                    textfont={"size": 10},
                ))
                
                fig.update_layout(
                    title='Asset Correlation Matrix (3M)',
                    template='plotly_dark',
                    height=400,
                    width=400
                )
                
                return fig
            
        except Exception as e:
            return None
    
    @staticmethod 
    def create_volatility_chart(symbol="^TNX", period="6mo"):
        """Create volatility analysis chart."""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)
            
            # Calculate rolling volatility
            returns = data['Close'].pct_change().dropna()
            vol_20d = returns.rolling(window=20).std() * np.sqrt(252) * 100
            vol_60d = returns.rolling(window=60).std() * np.sqrt(252) * 100
            
            fig = go.Figure()
            
            # Price
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data['Close'],
                name=f'{symbol} Price',
                line=dict(color='#00ff88'),
                yaxis='y'
            ))
            
            # Volatility
            fig.add_trace(go.Scatter(
                x=vol_20d.index,
                y=vol_20d,
                name='20D Volatility',
                line=dict(color='#ff6b6b'),
                yaxis='y2'
            ))
            
            fig.add_trace(go.Scatter(
                x=vol_60d.index,
                y=vol_60d,
                name='60D Volatility', 
                line=dict(color='#4ecdc4'),
                yaxis='y2'
            ))
            
            fig.update_layout(
                title=f'{symbol} Price & Volatility Analysis',
                xaxis_title='Date',
                yaxis=dict(
                    title='Price',
                    titlefont=dict(color='#00ff88'),
                    tickfont=dict(color='#00ff88'),
                    side='left'
                ),
                yaxis2=dict(
                    title='Volatility (%)',
                    titlefont=dict(color='#ff6b6b'),
                    tickfont=dict(color='#ff6b6b'),
                    anchor='x',
                    overlaying='y',
                    side='right'
                ),
                template='plotly_dark',
                height=400,
                showlegend=True
            )
            
            return fig
            
        except Exception as e:
            return None
    
    @staticmethod
    def create_economic_dashboard():
        """Create mini economic indicators dashboard."""
        try:
            # Get some basic economic data
            symbols = {
                'VIX': '^VIX',
                'Gold': 'GC=F', 
                'Oil': 'CL=F',
                'Bitcoin': 'BTC-USD'
            }
            
            current_data = {}
            changes = {}
            
            for name, symbol in symbols.items():
                try:
                    ticker = yf.Ticker(symbol)
                    hist = ticker.history(period="5d")
                    if not hist.empty:
                        current = hist['Close'].iloc[-1]
                        prev = hist['Close'].iloc[-2] if len(hist) > 1 else current
                        change = ((current - prev) / prev * 100)
                        
                        current_data[name] = round(current, 2)
                        changes[name] = round(change, 2)
                except:
                    continue
            
            if current_data:
                # Create gauge charts
                fig = go.Figure()
                
                colors = ['#00ff88', '#ff6b6b', '#4ecdc4', '#feca57']
                
                for i, (name, value) in enumerate(current_data.items()):
                    change = changes.get(name, 0)
                    color = colors[i % len(colors)]
                    
                    fig.add_trace(go.Indicator(
                        mode="number+delta",
                        value=value,
                        delta={'reference': value * (1 - change/100), 'relative': True},
                        title={"text": name},
                        domain={'x': [i*0.25, (i+1)*0.25], 'y': [0, 1]},
                        number={'font': {'color': color}}
                    ))
                
                fig.update_layout(
                    template='plotly_dark',
                    height=200,
                    margin=dict(l=0, r=0, t=30, b=0)
                )
                
                return fig
            
        except Exception as e:
            return None
    
    @staticmethod
    def create_sentiment_gauge(sentiment_score=0.5):
        """Create market sentiment gauge."""
        try:
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=sentiment_score * 100,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Market Sentiment"},
                delta={'reference': 50},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#00ff88"},
                    'steps': [
                        {'range': [0, 25], 'color': "#ff4444"},
                        {'range': [25, 50], 'color': "#ffaa00"}, 
                        {'range': [50, 75], 'color': "#ffff00"},
                        {'range': [75, 100], 'color': "#00ff88"}
                    ],
                    'threshold': {
                        'line': {'color': "white", 'width': 4},
                        'thickness': 0.75,
                        'value': 75
                    }
                }
            ))
            
            fig.update_layout(
                template='plotly_dark',
                height=300,
                font={'color': "white", 'family': "Arial"}
            )
            
            return fig
            
        except Exception as e:
            return None
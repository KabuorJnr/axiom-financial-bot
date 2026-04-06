"""
AXIOM Financial Markets Chatbot - Main Streamlit Application
Impressive UI with real-time market data integration and dual AI system.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import logging
from ai_client import AIClient, get_suggested_prompts, PROMPT_TEMPLATES
from market_data import market_data
from config import APP_TITLE, BOT_NAME, BOT_DESCRIPTION, ENABLE_CHARTS, ENABLE_REAL_TIME_DATA

# Configure logging
logging.basicConfig(level=logging.INFO)

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for AXIOM-like styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00ff88;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px #00ff88;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #888888;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #00ff88;
    }
    
    .user-message {
        background-color: #1a1a1a;
        border-left-color: #00aaff;
    }
    
    .bot-message {
        background-color: #0a0a0a;
        border-left-color: #00ff88;
    }
    
    .market-data-box {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #333;
        margin: 0.5rem 0;
    }
    
    .metric-positive {
        color: #00ff88;
        font-weight: bold;
    }
    
    .metric-negative {
        color: #ff4444;
        font-weight: bold;
    }
    
    .suggested-prompt {
        background-color: #2a2a2a;
        border: 1px solid #444;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .suggested-prompt:hover {
        background-color: #3a3a3a;
        border-color: #00ff88;
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-online {
        background-color: #00ff88;
        box-shadow: 0 0 8px #00ff88;
    }
    
    .status-offline {
        background-color: #ff4444;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'ai_client' not in st.session_state:
    st.session_state.ai_client = AIClient()

if 'market_summary' not in st.session_state:
    st.session_state.market_summary = None

if 'last_data_update' not in st.session_state:
    st.session_state.last_data_update = None

def update_market_data():
    """Update market data and cache timestamp."""
    if ENABLE_REAL_TIME_DATA:
        st.session_state.market_summary = market_data.get_comprehensive_market_summary()
        st.session_state.last_data_update = datetime.now()

def display_chat_message(role, content, timestamp=None):
    """Display a formatted chat message."""
    if timestamp is None:
        timestamp = datetime.now().strftime("%H:%M:%S")
    
    css_class = "user-message" if role == "user" else "bot-message"
    icon = "👤" if role == "user" else "🤖"
    name = "You" if role == "user" else BOT_NAME
    
    st.markdown(f"""
    <div class="chat-message {css_class}">
        <strong>{icon} {name}</strong> <small style="color: #666;">{timestamp}</small><br>
        {content}
    </div>
    """, unsafe_allow_html=True)

def create_yield_usd_chart():
    """Create interactive yield vs USD correlation chart."""
    try:
        # Get chart data
        yield_data = market_data.get_chart_data("^TNX", period="3mo")
        usd_data = market_data.get_chart_data("DX-Y.NYB", period="3mo")
        
        if yield_data and usd_data:
            fig = go.Figure()
            
            # Add yield line (left y-axis)
            fig.add_trace(go.Scatter(
                x=yield_data['dates'],
                y=yield_data['prices'],
                name='10Y Treasury Yield (%)',
                line=dict(color='#00ff88', width=2),
                yaxis='y'
            ))
            
            # Add USD line (right y-axis) 
            fig.add_trace(go.Scatter(
                x=usd_data['dates'],
                y=usd_data['prices'],
                name='USD Index (DXY)',
                line=dict(color='#00aaff', width=2),
                yaxis='y2'
            ))
            
            # Update layout
            fig.update_layout(
                title='US Treasury 10Y Yield vs USD Index (3M)',
                xaxis_title='Date',
                yaxis=dict(
                    title='10Y Yield (%)',
                    titlefont=dict(color='#00ff88'),
                    tickfont=dict(color='#00ff88'),
                    side='left'
                ),
                yaxis2=dict(
                    title='USD Index',
                    titlefont=dict(color='#00aaff'),
                    tickfont=dict(color='#00aaff'),
                    anchor='x',
                    overlaying='y',
                    side='right'
                ),
                template='plotly_dark',
                height=400,
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01
                )
            )
            
            return fig
            
    except Exception as e:
        logging.error(f"Chart creation error: {e}")
        
    return None

def main():
    # Header
    st.markdown(f'<div class="main-header">{BOT_NAME}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">• {BOT_DESCRIPTION} • macro mode</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎛️ Controls")
        
        # Market data status
        if ENABLE_REAL_TIME_DATA:
            if st.button("🔄 Refresh Market Data"):
                update_market_data()
                st.rerun()
            
            # Show last update time
            if st.session_state.last_data_update:
                update_time = st.session_state.last_data_update.strftime("%H:%M:%S")
                st.markdown(f'<small>Last update: {update_time}</small>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Suggested prompts
        st.markdown("### 💡 Quick Starts")
        suggested = get_suggested_prompts()
        
        for prompt in suggested:
            if st.button(prompt, key=f"suggest_{prompt}", help="Click to use this prompt"):
                st.session_state.user_input = prompt
                st.rerun()
        
        st.markdown("---")
        
        # Market data display
        if ENABLE_REAL_TIME_DATA and st.session_state.market_summary:
            st.markdown("### 📊 Live Market Data")
            st.markdown('<div class="market-data-box">' + 
                       st.session_state.market_summary.replace('\n', '<br>') + 
                       '</div>', unsafe_allow_html=True)
        
        # Clear conversation
        if st.button("🗑️ Clear Chat"):
            st.session_state.conversation_history = []
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Chat interface
        st.markdown("### 💬 Ask me anything — macro, FX, bonds, equities, trading psychology")
        
        # Display conversation history
        if st.session_state.conversation_history:
            for message in st.session_state.conversation_history:
                display_chat_message(
                    message["role"], 
                    message["content"],
                    message.get("timestamp", "")
                )
        
        # Chat input
        user_input = st.text_input(
            "Type your question or thesis...",
            key="user_input",
            placeholder="e.g., 'US bond yields and the dollar — explain the relationship'"
        )
        
        if user_input:
            # Add user message to history
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.session_state.conversation_history.append({
                "role": "user",
                "content": user_input,
                "timestamp": timestamp
            })
            
            # Get AI response
            with st.spinner(f"{BOT_NAME} is analyzing..."):
                # Update market data if needed
                if ENABLE_REAL_TIME_DATA:
                    update_market_data()
                
                # Generate response with market context
                response = st.session_state.ai_client.generate_response(
                    user_input,
                    conversation_history=st.session_state.conversation_history[:-1],  # Exclude current message
                    market_data=st.session_state.market_summary if ENABLE_REAL_TIME_DATA else None
                )
                
                # Add AI response to history
                st.session_state.conversation_history.append({
                    "role": "assistant", 
                    "content": response,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
            
            # Clear input and rerun
            st.session_state.user_input = ""
            st.rerun()
    
    with col2:
        # Charts and visualizations
        if ENABLE_CHARTS:
            st.markdown("### 📈 Live Charts")
            
            # Yield vs USD chart
            chart = create_yield_usd_chart()
            if chart:
                st.plotly_chart(chart, use_container_width=True)
            else:
                st.info("Chart data loading...")
            
            # Quick stats
            if ENABLE_REAL_TIME_DATA:
                current_data = market_data.get_current_yields_and_fx()
                correlation_data = market_data.get_historical_correlation_data()
                
                st.markdown("### 🔢 Quick Stats")
                
                # Display metrics with color coding
                col_a, col_b = st.columns(2)
                
                with col_a:
                    yield_val = current_data.get('10Y_Treasury_Yield', 'N/A')
                    st.metric("10Y Yield", f"{yield_val}%")
                    
                    eur_usd = current_data.get('EUR_USD', 'N/A')
                    st.metric("EUR/USD", eur_usd)
                
                with col_b:
                    dxy_val = current_data.get('USD_Index_DXY', 'N/A')
                    st.metric("DXY", dxy_val)
                    
                    corr_val = correlation_data.get('correlation_1y', 'N/A')
                    st.metric("Yield-USD Corr", corr_val)

if __name__ == "__main__":
    # Initialize market data on startup
    if st.session_state.market_summary is None and ENABLE_REAL_TIME_DATA:
        update_market_data()
    
    main()
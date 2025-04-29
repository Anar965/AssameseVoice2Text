"""
Background images and styles for the Assamese Voice into Text app.
"""
import streamlit as st

def apply_background_style():
    """
    Apply CSS styles for the background image and app appearance.
    """
    st.markdown("""
    <style>
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    
    .stApp {
        background-color: #f5f5f5;
    }
    
    .header-container {
        background: linear-gradient(to bottom, #1a237e, #3949ab);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
        border-top: 5px solid #D32F2F;
        border-bottom: 5px solid #D32F2F;
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 10px;
        background: #D32F2F;
        background-image: repeating-linear-gradient(90deg, #D32F2F, #D32F2F 40px, #FFFFFF 40px, #FFFFFF 80px);
    }
    
    .header-container::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 10px;
        background: #D32F2F;
        background-image: repeating-linear-gradient(90deg, #D32F2F, #D32F2F 40px, #FFFFFF 40px, #FFFFFF 80px);
    }
    
    .header-title {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .header-subtitle {
        font-size: 1.5rem;
        margin-top: 0;
        opacity: 0.9;
    }
    
    h1, h2, h3 {
        color: #1E3799;
    }
    
    .stSidebar {
        background-color: rgba(240, 240, 245, 0.9);
    }
    
    .css-1aumxhk {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px;
    }
    
    .culture-container {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 20px 0;
    }
    
    .alphabet-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def display_background():
    """Display the background image and header at the top of the app."""
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">অসমীয়া</h1>
        <h2 class="header-subtitle">Assamese Voice into Text</h2>
    </div>
    """, unsafe_allow_html=True)
import streamlit as st
import plotly.express as px
from plots import (
    get_timezone_activity_plot,
    get_market_attraction_plot,
    get_user_activity_duration_plot,
    get_market_growth_plot,
    get_retention_changes_plot
)

st.set_page_config(layout="wide", page_title="Polymarket Analysis")

def read_markdown_file(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    st.title("Polymarket Data Analysis Dashboard")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select Analysis",
        ["Home", "Timezone Activity", "Market Attraction", 
         "User Activity Duration", "Market Growth", "Retention Changes", "Approach Documentation"]
    )
    
    if page == "Home":
        st.header("Welcome to Polymarket Analysis")
        
        # Create two columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Trading Activity by Timezone")
            st.plotly_chart(get_timezone_activity_plot(), use_container_width=True)
                
            st.subheader("Market Growth Analysis")
            st.plotly_chart(get_market_growth_plot(), use_container_width=True)
                
            st.subheader("User Activity Duration")
            st.plotly_chart(get_user_activity_duration_plot(), use_container_width=True)
        
        with col2:
            st.subheader("Market User Attraction")
            st.plotly_chart(get_market_attraction_plot(), use_container_width=True)
                
            st.subheader("Retention Changes Since Election")
            st.plotly_chart(get_retention_changes_plot(), use_container_width=True)

    else:
        if page == "Timezone Activity":
            st.header("Trading Activity by Timezone")
            st.plotly_chart(get_timezone_activity_plot(), use_container_width=True)
            st.markdown(read_markdown_file("analyses/timezone_activity.md"))
            
        elif page == "Market Attraction":
            st.header("Market User Attraction Analysis")
            st.plotly_chart(get_market_attraction_plot(), use_container_width=True)
            st.markdown(read_markdown_file("analyses/market_attraction.md"))
            
        elif page == "User Activity Duration":
            st.header("User Activity Duration Analysis")
            st.plotly_chart(get_user_activity_duration_plot(), use_container_width=True)
            st.markdown(read_markdown_file("analyses/user_activity_duration.md"))
            
        elif page == "Market Growth":
            st.header("Market Growth Analysis")
            st.plotly_chart(get_market_growth_plot(), use_container_width=True)
            st.markdown(read_markdown_file("analyses/market_growth.md"))
            
        elif page == "Retention Changes":
            st.header("Retention Changes Since Election")
            st.plotly_chart(get_retention_changes_plot(), use_container_width=True)
            st.markdown(read_markdown_file("analyses/retention_changes.md"))

        elif page == "Approach Documentation":
            st.header("Technical Approach Documentation")
            st.markdown(read_markdown_file("approach_documentation.md"))

if __name__ == "__main__":
    main()
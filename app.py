import streamlit as st
import requests
import pandas as pd
from textblob import TextBlob
import plotly.express as px

# 1. Page Infrastructure
st.set_page_config(page_title="Market Sentiment Engine", layout="wide", page_icon="📈")
st.title("📊 Real-Time Financial News Sentiment Engine")
st.markdown("This system connects to live web APIs to fetch real-time market articles, executes automated algorithmic text sentiment processing via NLP, and builds responsive market metrics.")

# 2. API Passport Security
API_KEY = "c7500367c3f54d8ebe1680b34167f925" # Put your key back here!

# 3. Interactive Input Sidebar
st.sidebar.header("🎛️ Data Controls")
search_query = st.sidebar.text_input("Enter Company / Asset Ticker:", "NVIDIA")
fetch_button = st.sidebar.button("Execute Live Processing Pipeline")

if fetch_button:
    # Querying the last 20 breaking updates
    url = f"https://newsapi.org/v2/everything?q={search_query}&language=en&sortBy=publishedAt&pageSize=20&apiKey={API_KEY}"
    
    with st.spinner("Executing asynchronous data extraction over web nodes..."):
        try:
            response = requests.get(url)
            data = response.json()
            
            if data.get("status") == "ok" and "articles" in data and len(data["articles"]) > 0:
                
                # Arrays to construct our clean DataFrame rows
                processed_articles = []
                
                for article in data["articles"]:
                    title = article.get("title", "")
                    source = article.get("source", {}).get("name", "Unknown")
                    url_link = article.get("url", "#")
                    
                    if not title or "[Removed]" in title:
                        continue
                        
                    # 🧠 Algorithmic NLP Sentiment Engine Calculations
                    analysis = TextBlob(title)
                    polarity_score = analysis.sentiment.polarity
                    
                    # Mapping scores to standard qualitative categorical buckets
                    if polarity_score > 0.05:
                        sentiment_category = "Positive / Bullish"
                    elif polarity_score < -0.05:
                        sentiment_category = "Negative / Bearish"
                    else:
                        sentiment_category = "Neutral"
                        
                    processed_articles.append({
                        "Title": title,
                        "Source": source,
                        "URL": url_link,
                        "Polarity": polarity_score,
                        "Category": sentiment_category
                    })
                
                # Convert the structured matrix array into a standard DataFrame
                results_df = pd.DataFrame(processed_articles)
                
                # 📊 LAYOUT CREATION: Split screen into columns
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("📈 Aggregated Public Market Sentiment Profile")
                    # Calculate the aggregate metrics
                    avg_polarity = results_df["Polarity"].mean()
                    total_records = len(results_df)
                    
                    # Display metrics inside clean corporate value cards
                    st.metric(label="Overall Market Sentiment Index", value=f"{avg_polarity:.2f}", 
                              delta="Positive/Bullish" if avg_polarity > 0 else "Negative/Bearish")
                    st.caption(f"Based on analysis of {total_records} real-time global publication channels.")
                    
                    # Build an interactive pie distribution chart via Plotly
                    fig = px.pie(results_df, names="Category", 
                                 color="Category",
                                 color_discrete_map={"Positive / Bullish": "#2ecc71", "Neutral": "#95a5a6", "Negative / Bearish": "#e74c3c"},
                                 title="Sentiment Distribution Breakdown")
                    st.plotly_chart(fig, use_container_width=True)
                    
                with col2:
                    st.subheader("📰 Processed Data Feed Logs")
                    # Loop through individual results to print readable, clean cards
                    for _, row in results_df.iterrows():
                        color_indicator = "🟢" if row["Category"] == "Positive / Bullish" else "🔴" if row["Category"] == "Negative / Bearish" else "⚪"
                        st.markdown(f"{color_indicator} **[{row['Source']}]** [{row['Title']}]({row['URL']})")
                        st.caption(f"Calculated Text Polarity Score: `{row['Polarity']:.2f}`")
                        st.write("-" * 20)
                        
            else:
                st.error("No articles found or API limits exceeded. Recheck search parameters.")
                
        except Exception as e:
            st.error(f"Data transmission failed: {e}")
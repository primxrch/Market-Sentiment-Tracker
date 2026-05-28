# Asynchronous Financial News Sentiment Tracker & NLP Pipeline

📌 **Live Data Product Overview:** An enterprise-ready Python web application that establishes real-time client-server communication with global news aggregator networks, executes automated Natural Language Processing (NLP) text tokenization, and renders responsive market volatility metrics within a clean, multi-column browser interface.

## 💼 The Core Business Use Case
Quantitative asset funds and market analyst groups require systematic frameworks to parse thousands of unstructured, highly volatile news stories published across global media channels every hour. This software engine bridges that gap by transforming raw, unstructured text headlines into actionable, numeric data blocks on demand—allowing analysts to instantly detect shifts in public market momentum.

## ⚙️ App Pipeline Architecture
1. **Asynchronous Ingestion Layer:** Dynamically structures parameter-driven HTTP requests via Python's `requests` library to query global news indexes. It safely handles raw JSON payloads, filters out deleted network records (`[Removed]`), and isolates clean string parameters.
2. **Natural Language Processing Engine:** Processes headline string variables using text mining dictionaries. The system extracts adjectives and modifiers to calculate a precise **Text Polarity Score** ranging strictly from `-1.0` (Bearish/Distressed) to `+1.0` (Bullish/Optimistic), where `0.0` represents standard objective reporting.
3. **Categorical Matrix Transformer:** Automatically maps floating-point polarity vectors into three discrete operational business buckets:
   - **Positive / Bullish:** Polarity scores $> 0.05$
   - **Neutral:** Polarity scores between $-0.05$ and $0.05$
   - **Negative / Bearish:** Polarity scores $< -0.05$
4. **Presentation Subsystem:** Compiles the underlying data matrices into a localized client interface featuring interactive **Plotly Express** distribution charts and live-updating hyperlinked log logs.

## 🛠️ Software Stack & System Design
- **Language Environment:** Native Python 3.12+ Path Configurations
- **Asynchronous Data Client:** REST API Client (HTTP GET Request Layer)
- **Algorithmic Text Mining:** TextBlob Natural Language Processing (NLP Engine)
- **Vector Processing Core:** Pandas Data Matrix Structures
- **Interactive Data Visualization:** Plotly Express Rendering Responders
- **Application Web Framework:** Streamlit UI Architecture

## 📊 Dataset & Live API Logistics
- **Primary Data Engine:** [NewsAPI Core Index Services](https://newsapi.org/)
- **Data Ingestion Boundary:** Configured to dynamically stream a trailing window of the **top 20 live global publications** chronologically ordered by publication time stamp.
- **Environment Management:** Local runtime environment configurations (`__pycache__/`, `.streamlit/`) are cleanly filtered out of version control utilizing an explicit `.gitignore` structure to optimize repository health.

## 🚀 Execution Instructions
To initialize your workspace and run this web application locally, execute the following commands in your terminal:

```bash
# 1. Install required packages
pip install streamlit requests textblob pandas plotly

# 2. Fire up the local background server
streamlit run app.py
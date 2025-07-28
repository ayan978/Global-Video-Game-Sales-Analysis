import streamlit as st
import pandas as pd
import joblib
import numpy as np
from PIL import Image

# Load dataset
df = pd.read_csv("vgsales.csv")

# Set page config (title + wide mode)
st.set_page_config(page_title="Global Video Game Sales Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: white;'>🎮 Global Video Game Sales Dashboard</h1>", unsafe_allow_html=True)

# ========== KPI Section ==========
st.markdown("### 📌 Key Metrics")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Games", f"{len(df):,}")
kpi2.metric("Total Global Sales", f"{df['Global_Sales'].sum():,.1f}M")
kpi3.metric("Year Range", f"{int(df['Year'].min())} – {int(df['Year'].max())}")
kpi4.metric("Unique Publishers", f"{df['Publisher'].nunique():,}")

st.markdown("---")

# ========== Row 1: Platform & Genre ==========
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎮 Total Sales by Platform")
    st.image("images/sales_by_platform.png", use_column_width=True)

with col2:
    st.subheader("🧩 Total Sales by Genre")
    st.image("images/sales_by_genre.png", use_column_width=True)

# ========== Row 2: Top Publishers & Sales Over Years ==========
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏢 Top 10 Publishers by Global Sales")
    st.image("images/top_publishers.png", use_column_width=True)

with col4:
    st.subheader("📈 Global Sales Over the Years")
    st.image("images/sales_by_year.png", use_column_width=True)

# ========== Row 3: Full-Width Genre Trend ==========
st.subheader("📉 Genre Trends Over Time")
st.image("images/genre_over_time.png", use_column_width=True)

# Footer
st.markdown("---")
st.caption("Data Source: Kaggle")


# ============================
# 🔮 Sales Prediction Section
# ============================


st.markdown("---")
st.markdown("## 🔮 Predict Global Sales for a New Game")

# Load trained model and column list
model = joblib.load("final_rf_model.pkl")
model_features = joblib.load("model_features.pkl")

# Define rare-category filtering thresholds
top_genres = df['Genre'].value_counts().nlargest(5).index.tolist()
top_platforms = df['Platform'].value_counts().nlargest(10).index.tolist()
top_publishers = df['Publisher'].value_counts().nlargest(10).index.tolist()
years = sorted(df['Year'].dropna().unique())

# Create input form
with st.form("prediction_form"):
    st.write("### Enter Game Info Below:")
    game_name = st.text_input("Enter Game Name")
  
    col1, col2 = st.columns(2)
    with col1:
        genre = st.selectbox("Select Genre", sorted(df['Genre'].dropna().unique()))
        publisher = st.selectbox("Select Publisher", sorted(df['Publisher'].dropna().unique()))
    with col2:
        platform = st.selectbox("Select Platform", sorted(df['Platform'].dropna().unique()))
        year = st.selectbox("Select Release Year", years)

    submitted = st.form_submit_button("Predict Sales")

if submitted:
    # Apply rare category grouping
    genre = genre if genre in top_genres else "Other"
    platform = platform if platform in top_platforms else "Other"
    publisher = publisher if publisher in top_publishers else "Other"

    # Create DataFrame for input
    input_dict = {
        'Genre': genre,
        'Platform': platform,
        'Publisher': publisher,
        'Year': year
    }
    input_df = pd.DataFrame([input_dict])

    # One-hot encode (same as training)
    input_encoded = pd.get_dummies(input_df, drop_first=True)

    # Align columns with training features
    for col in model_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_features]

    # Predict and reverse log scale
    log_pred = model.predict(input_encoded)[0]
    prediction = np.expm1(log_pred)

    # Output
    st.success(f"🎯 Predicted Global Sales: **{prediction:.2f} million units**")
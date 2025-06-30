import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Streamlit page settings
st.set_page_config(page_title="📦 E-Commerce RFM Dashboard", layout="wide")

st.title("📦 E-Commerce RFM Analytics Dashboard")
st.markdown("Analyze customer segments using **Recency, Frequency, Monetary (RFM)** metrics.")

# Dynamically get the correct path to CSV
file_dir = os.path.dirname(os.path.abspath(__file__))  # This file's directory: /app
data_path = os.path.join(file_dir, "..", "data", "rfm_segments.csv")

# Load RFM data
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

try:
    df = load_data(data_path)
except FileNotFoundError:
    st.error("❌ Could not find rfm_segments.csv. Make sure it exists in the /data folder.")
    st.stop()

# Sidebar Filters
st.sidebar.header("🔍 Filter by Segment")
segment_options = df['Segment'].unique().tolist()
selected_segments = st.sidebar.multiselect("Select Customer Segments:", segment_options, default=segment_options)

# Filter the data
filtered_df = df[df['Segment'].isin(selected_segments)]

# Display Key Metrics
st.subheader("📊 Segment Summary")
if filtered_df.empty:
    st.warning("⚠️ No data available for the selected segment(s). Please choose at least one.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(filtered_df))
    col2.metric("Avg Spend (£)", f"{filtered_df['Monetary'].mean():.2f}")
    col3.metric("Avg RFM Score", f"{filtered_df['RFM_Score'].mean():.1f}")

    # Bar Chart: Customer Count by Segment
    st.subheader("👥 Segment Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x='Segment', order=filtered_df['Segment'].value_counts().index, ax=ax1, palette='viridis')
    ax1.set_title("Number of Customers per Segment")
    ax1.set_xlabel("Segment")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    # Bar Chart: Average Spend by Segment
    st.subheader("💰 Average Spend by Segment")
    fig2, ax2 = plt.subplots()
    filtered_df.groupby('Segment')['Monetary'].mean().sort_values(ascending=False).plot(kind='bar', color='orange', ax=ax2)
    ax2.set_title("Average Spend (£) per Segment")
    ax2.set_xlabel("Segment")
    ax2.set_ylabel("Average Monetary Value")
    st.pyplot(fig2)

    # Show raw data
    st.subheader("📄 Raw RFM Data")
    st.dataframe(filtered_df)

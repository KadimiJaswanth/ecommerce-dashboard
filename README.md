# 📦 E-Commerce Analytics Dashboard

A Streamlit web app that analyzes customer purchase behavior using RFM (Recency, Frequency, Monetary) analysis and customer segmentation.

## 🔍 Features

- Cleaned transactional data
- RFM-based customer segmentation
- Interactive Streamlit dashboard
- Visualizations: Segment counts, average spend, etc.

## 📁 Folder Structure

ecommerce-dashboard/
├── app/
│ └── streamlit_app.py # Streamlit dashboard
├── data/
│ ├── ecommerce_data.csv # Raw data
│ ├── cleaned_data.csv # Cleaned version
│ ├── rfm_segments.csv # RFM output
│ └── segment_summary.csv # Segment summaries
├── notebooks/ # Jupyter analysis notebooks
├── requirements.txt # Python dependencies
└── README.md # Project overview

bash
Copy
Edit

## 🚀 Run It Locally

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
🧠 Built With
Python

Pandas, Seaborn, Matplotlib

Streamlit

📢 License
This project is under the MIT License.

yaml
Copy
Edit

---

## ❓ 3. Are There Any API Keys That Can Be Stolen?

**No, you're safe!** ✅  
Your current project (E-Commerce Dashboard) **does not use any API keys** or secrets.

### Here's why:
- All the logic is local: `Pandas`, `Streamlit`, and `CSV` files.
- No use of OpenAI, HuggingFace, Firebase, Supabase, etc.
- If you used those, you'd need `.env` or `secrets.toml` and **never commit them to GitHub**.

---

## ✅ Final To-Do Before Deploy

1. Paste the requirements and README content above into their files.
2. Make sure your folder structure is correct.
3. Push to GitHub.
4. Then go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy.

Let me know when you're ready, and I’ll guide the deploy 👨‍💻✨

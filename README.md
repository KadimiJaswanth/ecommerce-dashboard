# 🛍️ E-Commerce Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-💻-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Made by](https://img.shields.io/badge/Made%20by-Kadimi%20Jaswanth-orange)

> 🚀 A powerful data science and machine learning dashboard to explore customer behavior, segment users, and predict customer churn using Streamlit and Python.

---

## 🌐 Live Website

**Streamlit App**: [https://ecommerce-dashboard-xnfh2umumynaayxn4tbyxx.streamlit.app/](https://ecommerce-dashboard-xnfh2umumynaayxn4tbyxx.streamlit.app/)

---

## 📌 Features

✅ Interactive Dashboard  
✅ RFM (Recency, Frequency, Monetary) Segmentation  
✅ Churn Prediction with Machine Learning  
✅ Visual Data Exploration (Bar plots, KPIs)  
✅ Streamlit Web UI  
✅ Clean & Structured Codebase  

---

## 🧠 Machine Learning

The model is trained using a **Random Forest Classifier** based on:

- 📅 `Recency` → Days since last purchase  
- 🔁 `Frequency` → Total number of purchases  
- 💸 `Monetary` → Total amount spent  

📈 This helps businesses **identify loyal, at-risk, and potential churn customers** effectively.

---

## 📊 RFM Segmentation

Customers are segmented based on their purchasing behavior:

| Segment       | Description                            |
|---------------|----------------------------------------|
| Champions     | Recent, frequent, and high spenders    |
| Loyal         | Frequent purchasers                    |
| At Risk       | Long time since last purchase          |
| Need Attention| Spent once or twice only               |
| Others        | Occasional or inactive buyers          |

🔍 Helps in:
- Smart Marketing
- Retargeting Campaigns
- Customer Retention

---

## 🗂️ Folder Structure

```
ecommerce-dashboard/
├── app/
│   └── streamlit_app.py          # Streamlit Dashboard UI
├── data/
│   ├── ecommerce_data.csv
│   ├── cleaned_data.csv
│   ├── customer_features.csv
│   ├── rfm_segments.csv
│   └── segment_summary.csv
├── models/
│   └── churn_predictor.pkl       # Trained ML model
├── notebooks/
│   └── analysis_and_modeling.ipynb  # Data preprocessing & ML
├── requirements.txt              # Python dependencies
└── README.md                     # Project description
```

---

## ⚙️ Installation Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/KadimiJaswanth/ecommerce-dashboard.git
cd ecommerce-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

## 🛡️ License

This project is licensed under the **MIT License**.  
You are free to use, modify, and share with attribution. 🤝

---

## 🙌 Credits

- 📊 Real-world inspired dataset
- 💻 Built with:  
  Python, Pandas, Scikit-learn, Matplotlib, Streamlit
- 🙋‍♂️ Developed by: **Kadimi Jaswanth**

---

## ⭐ Support

If you liked this project:

🌟 **Star the repo**  
📢 **Share it with others in the community**

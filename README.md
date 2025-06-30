# 🛍️ E-Commerce Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-💻-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Made by](https://img.shields.io/badge/Made%20by-Kadimi%20Jaswanth-orange)

> 🚀 A powerful data science and machine learning dashboard to explore customer behavior, segment users, and predict customer churn using Streamlit and Python.

---

## 🔗 Live Project Links

🌐 **Live Demo**: [View Streamlit App](https://ecommerce-dashboard-xnfh2umumynaayxn4tbyxx.streamlit.app/)  

---

## 📌 Features

✅ Interactive Dashboard  
✅ RFM (Recency, Frequency, Monetary) Segmentation  
✅ Churn Prediction with Machine Learning  
✅ Visual Data Exploration (Bar plots, KPIs)  
✅ Streamlit Web UI  
✅ Clean & structured codebase  

---

## 🧠 Machine Learning

The model is trained using a **Random Forest Classifier** on:
- `Recency`: Days since last purchase
- `Frequency`: Total number of purchases
- `Monetary`: Total money spent

📈 This helps businesses **identify loyal vs at-risk customers** and take smart actions.

---

## 📊 RFM Segmentation

Customers are segmented into groups based on:
- Recency (how recently they purchased)
- Frequency (how often they purchase)
- Monetary (how much they spend)

This enables:
- 🧠 Smart marketing decisions
- 🎯 Customer targeting
- 🔁 Churn reduction

---

## 🗂 Folder Structure

```
ecommerce-dashboard/
├── app/
│   └── streamlit_app.py       # Streamlit dashboard UI
├── data/
│   ├── ecommerce_data.csv
│   ├── cleaned_data.csv
│   ├── customer_features.csv
│   ├── rfm_segments.csv
│   └── segment_summary.csv
├── models/
│   └── churn_predictor.pkl    # Trained churn prediction model
├── notebooks/
│   └── All preprocessing & ML code in Jupyter
├── requirements.txt           # Project dependencies
└── README.md                  # You're reading it!
```

---

## 🚀 Installation Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/KadimiJaswanth/ecommerce-dashboard.git
cd ecommerce-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to fork, use, enhance, and share 

---

## 🙌 Credits

- 📊 Real-world inspired dataset
- 💻 Built with Python, Pandas, Scikit-learn & Streamlit
- 🙋‍♂️ Developed by Kadimi Jaswanth

---

## 💼 About Me

**Kadimi Jaswanth**  
B.Tech | Data Science & ML Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/kadimi-jaswanth-347952289/)

---

⭐ If you liked this project, don’t forget to **star the repo** and connect with me on LinkedIn!

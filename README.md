# Tourism Experience Analytics

## Classification, Rating Prediction and Recommendation System

### 📌 Project Overview

Tourism Experience Analytics is a machine learning project designed to analyze tourism data and provide useful predictions and recommendations.

The project focuses on three major tasks:

* ⭐ Predicting attraction ratings using Regression
* 🧳 Predicting visit mode using Classification
* 🎯 Recommending tourist attractions based on user preferences

---

## 🎯 Objectives

### 1. Rating Prediction

Predict the rating that a user may give to a tourist attraction based on available tourism and user information.

### 2. Visit Mode Classification

Predict the user's visit mode, such as:

* Business
* Family
* Couples
* Friends

### 3. Attraction Recommendation

Recommend tourist attractions using historical ratings and user preferences.

---

## 📊 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Google Colab

---

## 📁 Project Structure

```text
Tourism-Experience-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── notebooks/
│   └── Tourism_Experience_Analytics.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── best_regression_model.joblib
│   ├── best_classification_model.joblib
│   └── user_item_matrix.joblib
│
└── src/
    ├── data_preprocessing.py
    ├── train_models.py
    └── recommendation.py
```

---

## 🤖 Machine Learning Models

### Regression Models

* Linear Regression
* Random Forest Regressor

The models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Classification Models

* Logistic Regression
* Random Forest Classifier

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🎯 Recommendation System

The recommendation system uses user ratings and attraction information to suggest attractions that users may enjoy.

---

## 📊 Exploratory Data Analysis

The project includes:

* Rating distribution
* Visit mode analysis
* Attraction type analysis
* Popular attractions
* Tourism trends

---

## 🚀 Streamlit Application

The Streamlit application allows users to:

* Select tourism-related features
* Predict visit mode
* Predict attraction ratings
* Get attraction recommendations

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Tourism-Experience-Analytics.git
```

Move into the project folder:

```bash
cd Tourism-Experience-Analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Add more tourism datasets
* Improve recommendation algorithms
* Add interactive dashboards
* Deploy the application online
* Implement hybrid recommendation systems

---

## 👩‍💻 Author

Vaishnavi

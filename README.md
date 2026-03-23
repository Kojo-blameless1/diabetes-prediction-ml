# Diabetes Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Project Overview
This project builds and evaluates machine learning models to predict diabetes using an enhanced version of the Pima Indians Diabetes Dataset.

The study applies a complete data mining pipeline, including data preprocessing, model training, evaluation, and deployment through an interactive prediction interface.

---

## 📊 Dataset
- Source: Pima Indians Diabetes Dataset  
- Total records: **1,268 patients**  
- Features: 8 clinical attributes  
- Target: Diabetes outcome (0 = No, 1 = Yes)

### Key Features:
- Glucose level  
- Body Mass Index (BMI)  
- Age  
- Blood Pressure  
- Insulin  
- Pregnancies  
- Skin Thickness  
- Diabetes Pedigree Function  

---

## ⚙️ Models Implemented
- Logistic Regression  
- Decision Tree  
- Support Vector Machine (SVM)  
- Random Forest  

All models were trained using the same preprocessing steps and evaluated using consistent metrics.

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 77.9% | 79.9% | 85.1% | 82.4% |
| Decision Tree | 79.9% | 79.4% | 90.3% | 84.5% |
| SVM | 81.1% | 80.8% | 90.3% | 85.3% |
| **Random Forest** | **83.1%** | **81.4%** | **93.5%** | **87.0%** |

---

## 🏆 Key Findings
- **Best Model:** Random Forest  
  - Recall: **93.5%**  
  - Accuracy: **83.1%**

- **Top Predictive Features:**
  - Glucose (strongest predictor)
  - BMI
  - Age  

- **Clinical Insight:**
  - Random Forest detected **144 out of 154 diabetic patients**
  - Highest recall makes it suitable for medical screening where missing cases is risky  

---

## 🔍 Data Processing
- Replaced invalid zero values with median values  
- Feature scaling using StandardScaler  
- Train-test split: 80% training, 20% testing  
- Stratified sampling to maintain class distribution  

---

## 🚀 Features
- Data preprocessing pipeline  
- Exploratory Data Analysis (EDA)  
- Multiple model training and evaluation  
- ROC curve analysis and comparison  
- Feature importance analysis  
- Interactive prediction system  

---

## 🖥️ Interactive Prediction Tool
Run the interface to predict diabetes risk in real time:

```bash
python src/prediction_interface.py
# Diabetes Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Project Overview
This project develops and compares four machine learning models to predict diabetes using the Pima Indians Diabetes Dataset. The models include Logistic Regression, Decision Tree, Support Vector Machine (SVM), and Random Forest.

## 🎯 Key Findings
- **Best Model:** Decision Tree (76.6% accuracy, 72.2% recall)
- **Most Important Feature:** Glucose (53.2% importance)
- **Clinical Impact:** Catches 39 out of 54 diabetic patients

## 📊 Models Compared
| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 70.1% | 58.7% | 50.0% | 54.0% |
| Decision Tree | 76.6% | 65.0% | 72.2% | 68.4% |
| SVM | 73.4% | 64.4% | 53.7% | 58.6% |
| Random Forest | 74.0% | 66.7% | 51.9% | 58.3% |

## 🚀 Features
- ✅ Data preprocessing and handling missing values
- ✅ Exploratory Data Analysis with visualizations
- ✅ 4 machine learning models implementation
- ✅ Model comparison with ROC curves
- ✅ Feature importance analysis
- ✅ **Interactive Prediction Interface** - Real-time diabetes risk assessment

## 🖥️ Interactive Prediction Tool
Run the interactive interface to get real-time predictions:
```bash
python src/prediction_interface.py
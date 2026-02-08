# 💄 Makeup Product Recommendation System

## 📌 Project Overview
This project is a **content-based recommendation system** for makeup products.  
It recommends **similar makeup products of the same type** (for example, Serum → Serum) from **different brands** within a **similar price range**.

The system helps users explore alternative makeup products based on product similarity rather than user ratings.

---

## 🎯 Objectives
- Build a content-based recommendation system  
- Recommend products of the **same product type only**  
- Ensure recommendations come from **different brands**  
- Maintain **price similarity**  
- Create a simple and clean user interface  

---

## 🛠️ Technologies Used
- **Python**
- **Pandas & NumPy** – data processing
- **Scikit-learn** – TF-IDF and cosine similarity
- **Streamlit** – web application
- **Jupyter Notebook** – data analysis and model building

---


---

## 🔍 What Was Done in This Project
- Loaded and explored the makeup product dataset  
- Checked dataset structure, shape, and missing values  
- Identified inconsistencies in product category labels  
- Performed **feature engineering** by extracting product type from product names  
- Combined relevant features for similarity calculation  
- Applied **TF-IDF vectorization** to convert text data into numerical features  
- Used **cosine similarity** to measure similarity between products  
- Built a recommendation function with conditions:
  - Same product type  
  - Different brand  
  - Similar price range  
- Developed a clean and interactive interface using Streamlit  

---

## ⚠️ Challenges Faced
- The dataset contained **incorrect or inconsistent category labels**  
- Some products were assigned to the wrong category  
- This issue was handled by extracting the correct product type directly from the product name  

These challenges are common in real-world datasets and were addressed through proper preprocessing.

---

## ✅ Final Outcome
- Accurate recommendations based on product similarity  
- Stable and simple user interface  
- Clean and understandable code structure  
- Suitable for academic submission and GitHub portfolio  

---
## 📌 Conclusion

This project demonstrates how content-based filtering can be used to build an effective recommendation system using textual product data.
It also highlights the importance of data preprocessing and feature engineering when working with real-world datasets.

---

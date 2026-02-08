import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset safely (path issue avoid)
df = pd.read_csv("C:\\Users\\AVANTIKA\\Downloads\\recommendent\\most_used_beauty_cosmetics_products_extended.csv")
# -------- Product type extraction from Product_Name --------
def extract_product_type(name):
    name = name.lower()

    if "serum" in name:
        return "Serum"
    elif "lipstick" in name:
        return "Lipstick"
    elif "foundation" in name:
        return "Foundation"
    elif "mask" in name:
        return "Face Mask"
    elif "blush" in name:
        return "Blush"
    elif "highlighter" in name:
        return "Highlighter"
    elif "eyeshadow" in name or "eye shadow" in name:
        return "Eyeshadow"
    elif "mascara" in name:
        return "Mascara"
    elif "powder" in name:
        return "Powder"
    else:
        return "Other"

# Create correct product type column
df["Product_Type"] = df["Product_Name"].apply(extract_product_type)

# Combine features for similarity (category ignored due to wrong labels)
df["combined_features"] = (
    df["Product_Type"].astype(str) + " " +
    df["Brand"].astype(str)
)

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# -------- Recommendation Function --------
def recommend_products(product_name, price_range=10, top_n=5):

    idx = df[
        df["Product_Name"].str.lower().str.strip() ==
        product_name.lower().strip()
    ].index

    if len(idx) == 0:
        return []

    idx = idx[0]

    base_price = df.loc[idx, "Price_USD"]
    base_brand = df.loc[idx, "Brand"]
    base_type = df.loc[idx, "Product_Type"]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    results = []

    for i, score in sim_scores:
        row = df.iloc[i]

        if (
            row["Brand"] != base_brand and
            row["Product_Type"] == base_type and
            abs(row["Price_USD"] - base_price) <= price_range
        ):
            results.append({
                "Product_Name": row["Product_Name"],
                "Brand": row["Brand"],
                "Price_USD": row["Price_USD"],
                "Product_Type": row["Product_Type"],
                "Similarity": round(score, 2)
            })

        if len(results) == top_n:
            break

    return results

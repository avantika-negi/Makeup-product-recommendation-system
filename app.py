import streamlit as st
from model import recommend_products

# Page config
st.set_page_config(
    page_title="Makeup Recommendation System",
    layout="wide"
)

# Title
st.title("💄 Makeup Product Recommendation System")
st.write(
    "Enter a product name to get **same product recommendations from different brands** "
    "with **similar price**."
)

# Input
product_name = st.text_input("🔍 Enter Product Name")

# Button
if st.button("Recommend"):

    if product_name.strip() == "":
        st.warning("Please enter a product name.")

    else:
        recommendations = recommend_products(product_name)

        if len(recommendations) == 0:
            st.error("No recommendations found.")
        else:
            st.success("Recommended Products")

            cols = st.columns(len(recommendations))

            for col, rec in zip(cols, recommendations):
                with col:
                    st.markdown(
                        f"""
                        <div style="
                            border:1px solid #ddd;
                            border-radius:12px;
                            padding:20px;
                            text-align:center;
                            box-shadow:2px 2px 10px #eee;
                        ">
                            <h4>{rec['Product_Name']}</h4>
                            <p><b>Brand:</b> {rec['Brand']}</p>
                            <p><b>Type:</b> {rec['Product_Type']}</p>
                            <p><b>Price:</b> ${rec['Price_USD']}</p>
                            <p><b>Similarity:</b> {rec['Similarity']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

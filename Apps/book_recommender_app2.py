import pandas as pd
import numpy as nu
import pickle
import streamlit as st
from sklearn.cluster import KMeans


import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

def book_recommender():
    keyword = st.text_input("Enter keyword: ")

    sel = books[books["title"].str.contains(keyword, case=False)]
    titles = sel["title"].tolist()
    selected_title = st.selectbox("Select a title:", titles)

    recommendations = [] 
    if selected_title:
        selected_book = sel[sel["title"] == selected_title]
        selected_cluster = books["cluster_kmeans"].iloc[0]
        recommendations = books[books["cluster_kmeans"] == selected_cluster]["title"].tolist()

    # Hide the DataFrame
    st.text("")

    # Display the recommendations
    if recommendations:
        st.subheader("Book Recommendations")
        for recommendation in recommendations[:3]:  # Show only the first 3 recommendations
            st.write(recommendation)
    else:
        st.info("No recommendations found")

def main():
    st.title("Book Recommender App")
    book_recommender()

if __name__ == "__main__":
    # Assume you have loaded your book data and applied k-means clustering beforehand
    books = pd.read_csv("../Data/books_extended.csv") 
    # ...

    main()
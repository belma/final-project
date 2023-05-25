import pandas as pd
import numpy as nu
import pickle
import streamlit as st



st.header ("Book Recommender")

books = pd.read_csv("../Data/books_script.csv") 



books[books["cluster_agglo"] == 3]





def book_recommender():
    keyword = st.text_input("Enter keyword: ")

    sel = books[books["title"].str.contains(keyword, case=False)]
    for i, row in sel.iterrows():
        st.write(row["title"] + " (" + row["category"] + ")")

def main():
    st.title("Book Recommender App")
    book_recommender()

if __name__ == "__main__":
    main()


# ensure all libraries have been imported
import streamlit as st
import pandas as pd
import numpy as np

def generate_random_data(num_rows, num_cols):
    """
    Generates a DataFrame with random data.

    Args:
        num_rows: Number of rows in the DataFrame.
        num_cols: Number of columns in the DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame with random data.
    """
    data = {
        f'Column_{i}': np.random.randn(num_rows) 
        for i in range(1, num_cols + 1)
    }
    return pd.DataFrame(data)

def main():
    st.title("Random Data Generator")

    # User inputs
    num_rows = st.number_input("Number of Rows", min_value=1, step=1, value=10)
    num_cols = st.number_input("Number of Columns", min_value=1, step=1, value=5)

    # Generate data on button click
    if st.button("Generate Data"):
        df = generate_random_data(num_rows, num_cols)
        st.dataframe(df)

if __name__ == "__main__":
    main()
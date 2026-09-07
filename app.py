# lab_eda_gui.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Configuration

st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Exploratory Data Analysis Interface")


# 2. Sidebar: Dataset Ingestion

with st.sidebar:
    st.title("Menu")
    st.header("Upload Files")

    # Create a file uploader in the sidebar for CSV files
    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"]
    )


if uploaded_file is not None:

    # Read dataset
    df = pd.read_csv(uploaded_file)

    # 3. Dataset Overview

    st.subheader("First 5 Rows")
    st.dataframe(df.head())

    # Display data types
    st.subheader("Data Types")
    st.dataframe(df.dtypes.astype(str))

    # Missing value summary
    st.subheader("Missing Values per Column")

    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100

    missing_data = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing Percentage": missing_percentage
    })

    st.dataframe(missing_data)

    # Basic statistics for numerical columns
    st.subheader("Basic Numerical Statistics")
    st.dataframe(df.describe())

    
    # 4. Attribute Selection

    with st.sidebar:
        st.header("Attribute Selection")

        selected_attribute = st.selectbox(
            "Choose an attribute for visualization:",
            df.columns
        )


    # Detect column type

    if pd.api.types.is_numeric_dtype(df[selected_attribute]):
        column_type = "Numerical"
    else:
        column_type = "Categorical"

    st.write("Column Type:", column_type)


    # 5. Visualization Rendering

    

    st.subheader("Visualization")

    # Histogram
    st.write("Histogram")

    fig, ax = plt.subplots()
    sns.histplot(df[selected_attribute], kde=True, ax=ax)

    st.pyplot(fig)


    # Bar Chart
    st.write("Bar Chart")

    value_counts = df[selected_attribute].value_counts()

    st.bar_chart(value_counts)


else:
    st.info("Please upload a CSV file to start EDA.")
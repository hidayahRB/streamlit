# ensure you have install pandas

import pandas as pd 
import plotly.express as px
import streamlit as st
from datetime import datetime

st.set_page_config(page_title='Covid-19 Analysis in Malaysia',
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# assigning url to a variable
url="https://storage.data.gov.my/healthcare/covid_cases.csv"

 
# passing parameter to the function
dataset = pd.read_csv(url)

# ---- MAINPAGE ----
st.title(":bar_chart: Covid-19 Analysis in Malaysia")
st.markdown("**By Hidayah Arbee**")

# About
with st.expander(":orange[About]"):
    st.write('''
    This dashboard provides insights into Covid-19 situation in Malaysia. It is designed to increase public awareness as it visualizes key data points like clear Visual Cards and regional trends. This dashboard is built using Python and deployed on Streamlit. It offers an interactive and user-friendly experience to track the pandemic's progress and inform data-driven decision making.
    ''')

# Data Source
with st.expander(":orange[Data Source]"):
    st.markdown("The dataset is produced by the Crisis Preparedness and Response Centre (CPRC) at the Ministry of Health, published on data.gov.my. [Click here to find out more.](https://data.gov.my/data-catalogue/covid_cases)")

# Dashboard Details
with st.expander(":orange[Dashboard Details]"):
    st.write('''
    - **State Filter** - By default 'Malaysia' is selected in the State filter as to visualize the data of the whole country. State filter also affects the data displayed in this dashboard.
    - **Case Type Filter** - It is to assign the type of Covid-19 cases such as new cases, recovered cases, import cases or active cases. It will only affect the change of data on the trend chart.
    - **Visual Cards** - Display the keypoints of each case type.
    - **Trend Chart** - Displays the trend of respective case type.
    ''')

# display dataframe
# st.dataframe(dataset)

# --- SIDE BAR ---
st.sidebar.header("Filter",divider='rainbow')

# State selection
State = st.sidebar.multiselect(
    "Select the State:",
    options=dataset["state"].unique(),
    default=["Malaysia"]
)

# Case type selection
case_type = st.sidebar.radio(
    "Select the Case Type:",
    options=["New Cases", "Recovered Cases", "Import Cases", "Active Cases"]
)

df_selection = dataset.query(
    "state == @State"
)

# TOP KPI's

total_new_case = int(df_selection["cases_new"].sum())
total_import_case = int(df_selection["cases_import"].sum())
total_recovered = int(df_selection["cases_recovered"].sum())
total_active_case = int(df_selection["cases_active"].sum())

st.subheader("Summary",divider='rainbow')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<h5>Total New Cases:</h5>", unsafe_allow_html=True)
    st.subheader(f"{total_new_case:,}")

with col2:
    st.markdown(f"<h5>Total Import Cases:</h5>", unsafe_allow_html=True)
    st.subheader(f"{total_import_case:,}")

with col3:
    st.markdown(f"<h5>Total Recovered Cases:</h5>", unsafe_allow_html=True)
    st.subheader(f"{total_recovered:,}")

with col4:
    st.markdown(f"<h5>Total Active Cases:</h5>", unsafe_allow_html=True)
    st.subheader(f"{total_active_case:,}")

st.markdown("---")

# Select the column to display based on the selected case type
if case_type == "New Cases":
    selected_column = "cases_new"
    title = "Trend of New Covid-19 Cases"
elif case_type == "Recovered Cases":
    selected_column = "cases_recovered"
    title = 'Trend of Recovered Covid-19 Cases'
elif case_type == "Import Cases":
    selected_column = "cases_import"
    title = 'Trend of Import Covid-19 Cases'
else :
    selected_column = "cases_active"
    title = 'Trend of Active Covid-19 Cases'

# Calculate the total for the selected case type
# case_type_val = df_selection[selected_column]

# Line chart for daily new cases
# fig = px.line(df_selection, x='date', y='cases_new', title='Trend of New Covid-19 Cases', labels={'cases_new': 'New Cases', 'date': 'Date'})

fig = px.line(df_selection, x='date', y=df_selection[selected_column], title=title)

# Customize hover template to show full date in DD/MM/YYYY format
fig.update_traces(
    hovertemplate='Date: %{x|%d/%m/%Y}<br>Cases:%{y:,}<extra></extra>'
)

# Keep x-axis labels as "Month-YY"
fig.update_xaxes(tickformat="%b-%y")

st.plotly_chart(fig)
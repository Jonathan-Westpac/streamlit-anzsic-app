import streamlit as st
import pandas as pd

# Load data
industries = pd.read_csv('industries.csv')

st.set_page_config(page_title='Invoice Finance Suitability', layout='wide')
st.title('Invoice Finance Industry Suitability')

# Sidebar filters
st.sidebar.header('Filters')
search_query = st.sidebar.text_input('Search Industry Description')
code_query = st.sidebar.text_input('Search ANZSIC Code')

# Cascading filters for Division
division_options = sorted(industries['Division'].dropna().unique())
selected_division = st.sidebar.selectbox('Select Division', ['All'] + division_options)

filtered = industries.copy()
if selected_division != 'All':
    filtered = filtered[filtered['Division'] == selected_division]

# Apply description search filter
if search_query:
    filtered = filtered[filtered['Description'].str.contains(search_query, case=False, na=False)]

# Apply ANZSIC code search filter
if code_query:
    filtered = filtered[filtered['ANZSIC_Code'].astype(str).str.contains(code_query, case=False, na=False)]

# Reset button
if st.sidebar.button('Reset Filters'):
    filtered = industries.copy()

# Summary counts
st.subheader('Summary of Suitability')
st.write(filtered['Suitability'].value_counts())

# Display table with color-coded badges
st.subheader('Industry List')
for idx, row in filtered.iterrows():
    color = 'green' if row['Suitability'] == 'Green' else 'orange' if row['Suitability'] == 'Amber' else 'red'
    st.markdown(f"<div style='padding:10px;border:1px solid #ccc;margin-bottom:5px;'>"
                f"<b>{row['Description']}</b> | ANZSIC Code: {row['ANZSIC_Code']} | Division: {row['Division']} "
                f"<span style='color:{color};font-weight:bold;'>[{row['Suitability']}]</span></div>", unsafe_allow_html=True)

# Download filtered results
st.download_button('Download Filtered Results', filtered.to_csv(index=False), 'filtered_industries.csv')

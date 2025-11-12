# Invoice Finance Industry Suitability App (ANZSIC)

This Streamlit app helps users determine if an industry is suitable for invoice finance based on ANZSIC codes.

## Features
- Cascading filters for Division
- Search by Industry Description
- Search by ANZSIC Code
- Color-coded suitability indicators (Green, Amber, Red)
- Summary counts and downloadable filtered results

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud
1. Push this folder to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app, select your repo and branch.
4. Set the main file as `streamlit_app.py`.
5. Click **Deploy**.

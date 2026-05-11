import streamlit as st
import pandas as pd


DATA_PATH = "./data/SGJobData.csv"

df = pd.read_csv(DATA_PATH)
# Sets the page configuration
# You can set the page title and layout here
st.set_page_config(page_title="SG Job Data Dashboard", layout="wide")
#df["month"] = pd.to_datetime(df["month"])




#st.write(f"Rows loaded: {len(df):,} | Columns: {len(df.columns)}")
#st.dataframe(df.head(20), width="stretch")

unique_employer = sorted(df["postedCompany_name"].dropna().unique())
unique_employmenttype = sorted(df["employmentTypes"].dropna().unique())

selected_employer = st.sidebar.multiselect("Employer", unique_employer, default=[])
selected_employmenttype = st.sidebar.multiselect("Employment Type", unique_employmenttype, default=[])

filtered_df = df.copy()


if selected_employer:
    filtered_df = filtered_df[filtered_df["postedCompany_name"].isin(selected_employer)]

if selected_employmenttype:
    filtered_df = filtered_df[filtered_df["employmentTypes"].isin(selected_employmenttype)]




with st.expander("View Filtered Transactions"):
    st.dataframe(filtered_df, width="stretch", height=350)
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download filtered CSV",
        data=csv,
        file_name="filtered_sgjob_data.csv",
        mime="text/csv",
    )

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis Dashboard", layout="wide")
st.title("Windows Firewall Analysis Dashboard")

upload_file = st.file_uploader("Upload CSV File", type=["csv"])

if upload_file:
    df = pd.read_csv(upload_file)
    st.write("Data Preview:")
    st.subheader("Raw firewall data")
    st.dataframe(df)

    st.sidebar.header("Filters")
    directions = st.sidebar.multiselect("Select Direction", df["Direction"].unique(), default=list(df["Direction"].unique()))
    actions = st.sidebar.multiselect("Select Action", df["Action"].unique(), default=list(df["Action"].unique()))

    filtered_df = df[(df["Direction"].isin(directions)) & (df["Action"].isin(actions))]

    st.subheader("Filtered Data")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Filtered Data Table")
        direction_count = filtered_df["Direction"].value_counts()
        fig1, px1 = plt.subplots()
        direction_count.plot(kind='bar', ax=px1, color='skyblue')
        px1.set_ylabel("Count of Directions")
        st.pyplot(fig1)

    with col2:
        st.markdown("### Action Count")
        action_count = filtered_df["Action"].value_counts()
        fig2, px2 = plt.subplots()
        action_count.plot(kind='bar', ax=px2, color='lightgreen')
        px2.set_ylabel("Count of Actions")
        st.pyplot(fig2)

    st.subheader("ℹ️ Rule Details & Explanation")
    selected_row = st.selectbox("Select a rule to view details:", filtered_df["DisplayName"])

    if selected_row:
        rule_info = filtered_df[filtered_df["DisplayName"] == selected_row].iloc[0]
        st.markdown(f"""
        **Name**: {rule_info['Name']}  
        **Direction**: {rule_info['Direction']}  
        **Action**: {rule_info['Action']}  
        **Profile**: {rule_info['Profile']}  
        **Interface Type**: {rule_info['InterfaceType']}  
        **Description**:  
        > {rule_info.get('Description', 'No description available.')}
        """)

else:
    st.info("Please upload a CSV file to start the analysis.")
    st.markdown("""
    **Note:** The CSV file should contain columns named 'Direction' and 'Action'.
    """)
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import mysql.connector

st.set_page_config(page_title="PhonePe Pulse", layout="wide")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "project_2"
)
mycursor = mydb.cursor()

with st.container():
    st.header(":violet[Top 10 States, Districts and Postal codes]")
    col1,col2,col3 = st.columns([1.5,1,2], gap = "large")
    with col1:
        type = st.selectbox("Select A Type",["TRANSACTION","USER"]) 
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    with col2:
        if type == "TRANSACTION":
            type1 = st.selectbox("Select",["STATE","DISTRICT","PINCODE"])
            if type1 == "STATE":
                with col3:
                    mycursor.execute(f"SELECT State, SUM(Transaction_count) AS Total_Transactions_Count, SUM(Transaction_amount) AS Total_Amount FROM aggregated_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY Total_Amount desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
                    fig = px.bar(df,
                                    title='Top 10 - State Wise Bar Chart',
                                    x="State",
                                    y="Transactions_Count",
                                    orientation='v',
                                    color='Total_Amount',
                                    color_continuous_scale=px.colors.sequential.Agsunset)
                    st.plotly_chart(fig,use_container_width=True)  
            if type1 == "DISTRICT":
                with col3:
                    mycursor.execute(f"SELECT District, SUM(Count) AS Total_Transactions_Count, SUM(Amount) AS Total_Amount FROM map_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY District ORDER BY Total_Amount desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])
                    fig = px.bar(df,
                            title='Top 10 - District Wise Bar Chart',
                            x="District",
                            y="Transactions_Count",
                            orientation='v',
                            color='Total_Amount',
                            color_continuous_scale=px.colors.sequential.algae)
                    st.plotly_chart(fig,use_container_width=True)
            if type1 == "PINCODE":
                with col3:
                    mycursor.execute(f"select Pincode, SUM(Transaction_count) AS Total_Transactions_Count, SUM(Transaction_amount) AS Total_Amount FROM top_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY Pincode ORDER BY Total_Amount desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
                    fig = px.pie(df, values='Total_Amount',
                        names='Pincode',
                        title='Top 10 - Pincode Wise Bar Chart',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Transactions_Count'],
                        labels={'Transactions_Count':'Transactions_Count'})
                    fig.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig,use_container_width=True)

        if type == "USER":
            type1 = st.selectbox("Select",["STATE","DISTRICT","PINCODE"])
            if type1 == "STATE":
                with col3:
                    mycursor.execute(f"SELECT State, SUM(Registered_user) AS Total_Users FROM map_user WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY Total_Users desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users'])
                    fig = px.bar(df,
                                    title='Top 10 - State Wise Bar Chart',
                                    x="State",
                                    y="Total_Users",
                                    orientation='v',
                                    color='Total_Users',
                                    color_continuous_scale=px.colors.sequential.Agsunset)
                    st.plotly_chart(fig,use_container_width=True)  
            if type1 == "DISTRICT":
                with col3:
                    mycursor.execute(f"SELECT District, SUM(Registered_User) AS Total_Users FROM map_user WHERE Year = {Year} and Quarter = {Quarter} GROUP BY District ORDER BY Total_Users desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users'])
                    fig = px.bar(df,
                            title='Top 10 - District Wise Bar Chart',
                            x="District",
                            y="Total_Users",
                            orientation='v',
                            color='Total_Users',
                            color_continuous_scale=px.colors.sequential.algae)
                    st.plotly_chart(fig,use_container_width=True)
            if type1 == "PINCODE":
                with col3:
                    mycursor.execute(f"SELECT Pincode, SUM(Registered_Users) as Total_Users FROM top_user WHERE Year = {Year} and Quarter = {Quarter} GROUP BY Pincode ORDER BY Total_Users desc limit 10")
                    df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Users'])
                    fig = px.pie(df, values='Total_Users',
                        names='Pincode',
                        title='Top 10 - Pincode Wise Bar Chart',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Total_Users'],
                        labels={'Total_Users':'Total_Users'})
                    fig.update_traces(textposition='inside', textinfo='percent+label')
                    st.plotly_chart(fig,use_container_width=True)
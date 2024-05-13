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

st.header(":violet[PhonePe Pulse]")

with st.container():
    selected = option_menu("All India",["TRANSACTION","USER"],
                        icons=["house","graph-up-arrow"],
                        menu_icon="menu-button-wide",
                        default_index=0,
                        styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}},
                        orientation="horizontal")
if selected == "TRANSACTION":
    col1,col2 = st.columns(2)
    with col1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
    with col2:
        Quarter = st.slider("Quarter", min_value=1, max_value=4)

    # Total Aggregated transaction amount

    st.markdown("## :violet[Overall State Wise Aggregated Transactions Amount]")
    mycursor.execute(f"SELECT State, SUM(Transaction_amount) AS Total_amount FROM aggregated_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_amount'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_amount',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

    # Total Aggregated transaction transaction

    st.markdown("## :violet[Overall State Wise Aggregated Transactions Count]")
    mycursor.execute(f"SELECT State, SUM(Transaction_count) AS Total_Transactions FROM aggregated_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Transactions',
                        color_continuous_scale='reds')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

    # Total Map transaction amount

    st.markdown("## :violet[Overall State Wise Map Transactions Amount]")
    mycursor.execute(f"SELECT State, SUM(Amount) AS Total_amount FROM map_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_amount'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_amount',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

    # Total Map transaction transaction

    st.markdown("## :violet[Overall State Wise Map Transactions Count]")
    mycursor.execute(f"SELECT State, SUM(Count) AS Total_Transactions FROM map_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Transactions',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

    # Total Top transaction amount

    st.markdown("## :violet[Overall State Wise Top Transactions Count]")
    mycursor.execute(f"SELECT State, SUM(Transaction_amount) AS Total_amount FROM top_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_amount'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_amount',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

    # Total Top transaction transaction

    st.markdown("## :violet[Overall State Wise Top Transactions Count]")
    mycursor.execute(f"SELECT State, SUM(Transaction_count) AS Total_transaction FROM top_transaction WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_transaction'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_transaction',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

if selected == "USER":
    col1,col2 = st.columns(2)
    with col1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
    with col2:
        Quarter = st.slider("Quarter", min_value=1, max_value=4)

    # Total Aggregated User Count

    st.markdown("## :violet[Overall State Wise Map User Registered Count]")
    mycursor.execute(f"SELECT State, SUM(Registered_user) AS Registered_count FROM map_user WHERE Year = {Year} and Quarter = {Quarter} GROUP BY State ORDER BY State")
    df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Registered_count'])
    df2 = pd.read_csv('State_names.csv')
    df1.State = df2
    fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Registered_count',
                        color_continuous_scale='blues')
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
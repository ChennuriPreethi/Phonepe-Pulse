import streamlit as st
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "project_2"
)
mycursor = mydb.cursor()

st.set_page_config(page_title="PhonePe Pulse", layout="wide")

with st.container():
    st.header("VIEW TABLES")
    l_col, r_col= st.columns([3, 1])
    with l_col:
        option = st.selectbox("Select the option to view the tables",("Aggregated Transaction", "Aggregated User", "Map Transaction", "Map User", "Top Transaction", "Top User"),index=None,placeholder="Select a table")

if option == "Aggregated Transaction":
    mycursor.execute("SELECT * FROM aggregated_transaction")
    AT_Table = mycursor.fetchall()
    df1 = pd.DataFrame(AT_Table, columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"))
    st.dataframe(df1)

if option == "Aggregated User":
    mycursor.execute("SELECT * FROM aggregated_user")
    AU_Table = mycursor.fetchall()
    df2 = pd.DataFrame(AU_Table, columns = ("States", "Years", "Quarter", "Brands", "User_count", "User_percentage"))
    st.dataframe(df2)

if option == "Map Transaction":
    mycursor.execute("SELECT * FROM map_transaction")
    MT_Table = mycursor.fetchall()
    df3 = pd.DataFrame(MT_Table, columns = ("States", "Years", "Quarter", "District", "Transaction_count", "Transaction_amount"))
    st.dataframe(df3)

if option == "Map User":
    mycursor.execute("SELECT * FROM map_user")
    MU_Table = mycursor.fetchall()
    df4 = pd.DataFrame(MU_Table, columns = ("States", "Years", "Quarter", "District", "Registered_User"))
    st.dataframe(df4)

if option == "Top Transaction":
    mycursor.execute("SELECT * FROM top_transaction")
    TT_Table = mycursor.fetchall()
    df5 = pd.DataFrame(TT_Table, columns = ("States", "Years", "Quarter", "District_Pincode","Transaction_count", "Transaction_amount"))
    st.dataframe(df5)

if option == "Top User":
    mycursor.execute("SELECT * FROM top_user")
    TU_Table = mycursor.fetchall()
    df6 = pd.DataFrame(TU_Table, columns = ("States", "Years", "Quarter", "District_Pincode", "Registered_User"))
    st.dataframe(df6)
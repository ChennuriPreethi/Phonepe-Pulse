import streamlit as st
import mysql.connector
import pandas as pd
import json
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = ""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS project_2")
mycursor.execute("USE project_2")

st.set_page_config(page_title="Analysis", page_icon=":tada:", layout="wide")

# Data Extraction

# Aggregated - Transaction data

path1 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/aggregated/transaction/country/india/state/"
Agg_tra_state_list=os.listdir(path1)

AT = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in Agg_tra_state_list:
    pi = path1 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            ATD = json.load(Data)
            for l in ATD['data']['transactionData']:
                Name = l['name']
                Count = l['paymentInstruments'][0]['count']
                Amount = l['paymentInstruments'][0]['amount']
                AT['State'].append(i)
                AT['Year'].append(j)
                AT['Quarter'].append(int(k.strip('.json')))
                AT['Transaction_type'].append(Name)
                AT['Transaction_count'].append(Count)
                AT['Transaction_amount'].append(Amount)

df_aggr_trans = pd.DataFrame(AT)

df_aggr_trans["State"] = df_aggr_trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_aggr_trans["State"] = df_aggr_trans["State"].str.replace("-"," ")
df_aggr_trans["State"] = df_aggr_trans["State"].str.title()
df_aggr_trans['State'] = df_aggr_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Aggregated - User data

path2 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(path2)

AU = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_count': [], 'User_percentage': []}

for i in Agg_user_state_list:
    pi = path2 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            AUD = json.load(Data)
            try:
                for l in AUD["data"]["usersByDevice"]:
                    Brand_Name = l["brand"]
                    Count_ = l["count"]
                    ALL_Percentage = l["percentage"]
                    AU["State"].append(i)
                    AU["Year"].append(j)
                    AU["Quarter"].append(int(k.strip('.json')))
                    AU["Brands"].append(Brand_Name)
                    AU["User_count"].append(Count)
                    AU["User_percentage"].append(ALL_Percentage*100)
            except:
                pass

df_aggr_user = pd.DataFrame(AU)

df_aggr_user["State"] = df_aggr_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_aggr_user["State"] = df_aggr_user["State"].str.replace("-"," ")
df_aggr_user["State"] = df_aggr_user["State"].str.title()
df_aggr_user['State'] = df_aggr_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Map - Transaction data

path3 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/map/transaction/hover/country/india/state/"
map_tra_state_list = os.listdir(path3)

MT = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in map_tra_state_list:
    pi = path3 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            MTD = json.load(Data)     
            for l in MTD["data"]["hoverDataList"]:
                District = l["name"]
                Count = l["metric"][0]["count"]
                Amount = l["metric"][0]["amount"]
                MT['State'].append(i)
                MT['Year'].append(j)
                MT['Quarter'].append(int(k.strip('.json')))
                MT["District"].append(District)
                MT["Transaction_count"].append(Count)
                MT["Transaction_amount"].append(Amount)
                
df_map_transaction = pd.DataFrame(MT)

df_map_transaction["State"] = df_map_transaction["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_map_transaction["State"] = df_map_transaction["State"].str.replace("-"," ")
df_map_transaction["State"] = df_map_transaction["State"].str.title()
df_map_transaction['State'] = df_map_transaction['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Map - User data

path4 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(path4)

MU = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": []}

for i in map_user_state_list:
    pi = path4 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            MUD = json.load(Data)
            for l in MUD["data"]["hoverData"].items():
                District = l[0]
                Registereduser = l[1]["registeredUsers"]
                MU['State'].append(i)
                MU['Year'].append(j)
                MU['Quarter'].append(int(k.strip('.json')))
                MU["District"].append(District)
                MU["Registered_User"].append(Registereduser)
                
df_map_user = pd.DataFrame(MU)

df_map_user["State"] = df_map_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_map_user["State"] = df_map_user["State"].str.replace("-"," ")
df_map_user["State"] = df_map_user["State"].str.title()
df_map_user['State'] = df_map_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Top - Transaction data

path5 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/top/transaction/country/india/state/"
top_tra_state_list = os.listdir(path5)

TT = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in top_tra_state_list:
    pi = path5 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            TTD = json.load(Data) 
            for l in TTD['data']['pincodes']:
                Name = l['entityName']
                Count = l['metric']['count']
                Amount = l['metric']['amount']
                TT['State'].append(i)
                TT['Year'].append(j)
                TT['Quarter'].append(int(k.strip('.json')))
                TT['District_Pincode'].append(Name)
                TT['Transaction_count'].append(Count)
                TT['Transaction_amount'].append(Amount)

df_top_transaction = pd.DataFrame(TT)

df_top_transaction["State"] = df_top_transaction["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_top_transaction["State"] = df_top_transaction["State"].str.replace("-"," ")
df_top_transaction["State"] = df_top_transaction["State"].str.title()
df_top_transaction['State'] = df_top_transaction['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# Top - User data

path6 = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse/data/top/user/country/india/state/"
top_user_state_list = os.listdir(path6)

TU = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}

for i in top_user_state_list:
    pi = path6 + i + "/"
    Agg_yr = os.listdir(pi)
    for j in Agg_yr:
        pj = pi + j + "/"
        Agg_yr_list = os.listdir(pj)
        for k in Agg_yr_list:
            pk = pj + k
            Data = open(pk, 'r')
            TUD = json.load(Data)
            for l in TUD['data']['pincodes']:
                Name = l['name']
                RegisteredUser = l['registeredUsers']
                TU['State'].append(i)
                TU['Year'].append(j)
                TU['Quarter'].append(int(k.strip('.json')))
                TU['District_Pincode'].append(Name)
                TU['Registered_User'].append(RegisteredUser)
                
df_top_user = pd.DataFrame(TU)

df_top_user["State"] = df_top_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
df_top_user["State"] = df_top_user["State"].str.replace("-"," ")
df_top_user["State"] = df_top_user["State"].str.title()
df_top_user['State'] = df_top_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

# SQL Queries 

mycursor.execute("CREATE TABLE IF NOT EXISTS aggregated_transaction (State VARCHAR(100), Year INT, Quarter INT, Transaction_type VARCHAR(100), Transaction_count BIGINT, Transaction_amount BIGINT)")

for index,row in df_aggr_trans.iterrows():
    query1 = '''INSERT INTO aggregated_transaction (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
    values = (row["State"],
                row["Year"],
                row["Quarter"],
                row["Transaction_type"],
                row["Transaction_count"],
                row["Transaction_amount"]
            )
    mycursor.execute(query1,values)
    mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS aggregated_user (State VARCHAR(100), Year INT, Quarter INT, Brands VARCHAR(100), Count BIGINT, Percentage FLOAT)")

for index,row in df_aggr_user.iterrows():
    query2 = '''INSERT INTO aggregated_user (State, Year, Quarter, Brands, Count, Percentage)
                                                        values(%s,%s,%s,%s,%s,%s)'''
    values = (
                row["State"],
                row["Year"],
                row["Quarter"],
                row["Brands"],
                row["User_count"],
                row["User_percentage"]
            )
    mycursor.execute(query2,values)
    mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS map_transaction (State VARCHAR(100), Year INT, Quarter INT, District VARCHAR(100), Count BIGINT, Amount FLOAT)")

for index,row in df_map_transaction.iterrows():
    query3 = '''INSERT INTO map_transaction (State, Year, Quarter, District, Count, Amount)
                VALUES (%s, %s, %s, %s, %s, %s)'''
    values = (
                row['State'],
                row['Year'],
                row['Quarter'],
                row['District'],
                row['Transaction_count'],
                row['Transaction_amount']
            )
    mycursor.execute(query3,values)
    mydb.commit() 



mycursor.execute("CREATE TABLE IF NOT EXISTS map_user (State VARCHAR(100), Year INT, Quarter INT, District VARCHAR(100), Registered_user BIGINT)")

for index,row in df_map_user.iterrows():
    query4 = '''INSERT INTO map_user (State, Year, Quarter, District, Registered_user)
                        values(%s,%s,%s,%s,%s)'''
    values = (
                row["State"],
                row["Year"],
                row["Quarter"],
                row["District"],
                row["Registered_User"]
            )
    mycursor.execute(query4,values)
    mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS top_transaction (State VARCHAR(100), Year INT, Quarter INT, Pincode INT, Transaction_count BIGINT, Transaction_amount BIGINT)")

for index,row in df_top_transaction.iterrows():
    query5 = '''INSERT INTO top_transaction (State, Year, Quarter, Pincode, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (
                row["State"],
                row["Year"],
                row["Quarter"],
                row["District_Pincode"],
                row["Transaction_count"],
                row["Transaction_amount"]
            )
    mycursor.execute(query5,values)
    mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS top_user (State VARCHAR(100), Year INT, Quarter INT, Pincode INT, Registered_users BIGINT)")

for index,row in df_top_user.iterrows():
    query6 = '''INSERT INTO top_user (State, Year, Quarter, Pincode, Registered_users)
                                            values(%s,%s,%s,%s,%s)'''
    values = (
                row["State"],
                row["Year"],
                row["Quarter"],
                row["District_Pincode"],
                row["Registered_User"]
            )
    mycursor.execute(query6,values)
    mydb.commit()
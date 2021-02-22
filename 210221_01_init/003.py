import streamlit as st
import numpy as np
import pandas as pd
import geoip2.database
import ipaddress

reader = geoip2.database.Reader('/root/Python_2102210727/pythonStudy/210221_01/GEO/GeoLite2-City.mmdb')

def IPAddressToGeoLocate(TranslateIPAddress):
    location_temp = reader.city(TranslateIPAddress).location
    return pd.Series([location_temp.latitude, location_temp.longitude, location_temp.accuracy_radius])

def DataFrameImport():
    IPAddresssDF = pd.read_csv('IPAddressList.csv', encoding="utf8",  sep=',', header=0, names=['IPAddress','Count'])
    IPAddresssDF[['latitude','longitude', 'accuracy_radius']] = IPAddresssDF['IPAddress'].apply(IPAddressToGeoLocate)
    # print(IPAddresssDF)
    # IPAddresssDF['longitude']
    # input(IPAddresssDF[['latitude','longitude']].values)
    return IPAddresssDF

# streamlit表示
def streamlit_display(ImportDataFrame):
    st.title('streamlit動作確認')
    st.write(ImportDataFrame)
    st.map(data=ImportDataFrame[['latitude','longitude']])

if __name__ == "__main__":
    ImportDataFrame = DataFrameImport()
    streamlit_display(ImportDataFrame)
    # streamlit run 003.py  --server.port 8077

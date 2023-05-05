import streamlit as st
import requests
import urllib.request, urllib.parse, urllib.error
import json
import datetime
ip=request.remote_addr 
serviceurl = 'http://www.geoplugin.net/json.gp?ip='+ip
uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()
js = json.loads(data)
st.write("IP:",ip)
st.write("City:",js["geoplugin_city"])
st.write("Country:",js["geoplugin_countryName"])

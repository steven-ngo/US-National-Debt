import streamlit as st
import json
import requests

# App description
st.markdown('''
# U.S. National Debt

- Author: `Steven Ngo`
- Source Code: https://github.com/steven-ngo/US-National-Debt
- Language: `Python`
- Libraries: `streamlit`
''')
st.write('---')

retrieveDebt= requests.get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?sort=-record_date&format=json&page[number]=1&page[size]=1')

debtInfo = json.loads(retrieveDebt.content)

totalDebt = "${:,}".format(float(debtInfo['data'][0]['tot_pub_debt_out_amt']))

htmlStr = f"""
<h4>Total U.S. National Debt:</h4>
<p style="color:Tomato;font: bold 50px Courier;">{totalDebt}</p>
"""

st.markdown(htmlStr, unsafe_allow_html=True)

st.table(debtInfo['data'][0])

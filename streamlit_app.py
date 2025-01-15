import streamlit as st
import pandas as pd
import numpy as np
from hana_ml.dataframe import ConnectionContext, create_dataframe_from_pandas

st.title('HANA Streamlit Demo01')

cc = ConnectionContext('f20a3b41-4f0f-4c9e-9361-6fb50a589bfe.hana.prod-eu10.hanacloud.ondemand.com', 443, 'DWCDBUSER#GROEND', 'Gnotor_2094!')

q1 = """
SELECT DISTINCT EXP_LOCATION_NAME FROM "DWCDBUSER#GROEND"."EXPORT_DEFINITIONS" ORDER BY EXP_LOCATION_NAME
"""
# print(q1)

df = cc.sql(q1)
df = df.collect()

cc.close()

st.write(df)

# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import sys
import os
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# ---- READ EXCEL ----
#@st.cache

Input_path1 = os.path.join(os.getcwd())

csv_name = '\\MO_Paramater_v1.csv'
df = pd.read_csv(f"{Input_path1}{csv_name}")
print(df)
st.title(":bar_chart: NW MO & Parameter Summary")
st.markdown("##")


# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
mo = st.sidebar.multiselect(
    "Select the MO:",
    options=df["MO"].unique(),
    default= None
)


parameterList = st.sidebar.multiselect(
    "Select the parameter Type:",
    options=df["parameter"].unique(),
    default= None,
)


df_selection = df.query("MO == @mo | parameter == @parameterList")


st.dataframe(df_selection)

import plotly.express as px


h = px.histogram(df_selection, x= "parameter", y="Value",
             color='count', barmode='group',
             histfunc='count',
             height=400,text_auto=True)
st.plotly_chart(h)



c = px.bar(df_selection, x='parameter',
             color='Value', barmode='group',
             height=400,text_auto=True)

st.plotly_chart(c)



#st.bar_chart(df_selection, y = 'count', x='parameter')


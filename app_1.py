# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit

from pathlib import Path
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# ---- READ EXCEL ----
#@st.cache
path = Path("__file__").parent / "MO_Paramater_v1.csv"
print("hshhshshs", path)

df = pd.read_csv(path)

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

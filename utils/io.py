import streamlit as st
import pandas as pd
from vega_datasets import data as vega_data


@st.cache_data
def load_weather() -> pd.DataFrame:
    """Load Seattle weather data and add helper columns."""
    df = vega_data.seattle_weather()
    df["date"] = pd.to_datetime(df["date"])
    df["month_name"] = df["date"].dt.strftime("%b")
    df["year"] = df["date"].dt.year
    return df

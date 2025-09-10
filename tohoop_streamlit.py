import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st




st.title("tohoop Keller Ideen")

st.write(
    "Please use the side menu to select an option (based on Basti's table), then use the sliders to design your optimal basement arrangement"
)

col1, col2, col3 = st.columns((1, 3, 3), gap="medium")
with col1:
    status = st.radio("Select Variant:", [1, 2, 3, 4, 5, 6])
    status = status - 1

df = pd.DataFrame(
    [
        [280, 420, 280, 280, 420, 350],
        [280, 280, 420, 420, 280, 420],
        [30, 15, 50, 30, 30, 5],
        [15, 10, 0, 15, 15, 0],
        [100, 40, 0, 0, 0, 0],
        [20, 10, 20, 20, 20, 5],
        [10, 5, 10, 5, 5, 5],
        [50, 5, 5, 15, 15, 10],
        [50, 50, 50, 50, 50, 50],
    ],
    index=[
        "abstell",
        "fahrrad",
        "werkstatt",
        "waschen",
        "trocknen",
        "food",
        "fair",
        "lastenrad",
        "technik",
    ],
    columns=["1", "2", "3", "4", "5", "6"],
)

with col2:
    # can't show total at the top
    # Create sliders for different sections
    abstell = st.slider(
        "Abstellflaeche", min_value=210, max_value=490, value=df.iat[0, status]
    )
    fahrrad = st.slider(
        "Fahrradstellflaeche", min_value=210, max_value=490, value=df.iat[1, status]
    )
    werkstatt = st.slider(
        "Werkstatt", min_value=0, max_value=50, value=df.iat[2, status]
    )
    waschen = st.slider("Waschen", min_value=0, max_value=20, value=df.iat[3, status])
    trocknen = st.slider(
        "Trocknen", min_value=0, max_value=100, value=df.iat[4, status]
    )
with col3:
    food = st.slider("Food Coop", min_value=0, max_value=30, value=df.iat[5, status])
    fair = st.slider("Fairteiler", min_value=0, max_value=25, value=df.iat[6, status])
    lastenrad = st.slider(
        "Lastenraeder/KiWa/etc", min_value=0, max_value=50, value=df.iat[7, status]
    )
    technik = st.slider("Technik", min_value=49, max_value=51, value=df.iat[8, status])
    total = (
        abstell
        + fahrrad
        + werkstatt
        + waschen
        + trocknen
        + food
        + fair
        + lastenrad
        + technik
    )
    st.write("-> Total square meters: ", total)
    st.write("-> Allowable square meters: ``835``")


# plotme = df.iloc[:, status]
# plotme = plotme.to_dict()
st.subheader("Comparison of Different Uses")
st.bar_chart(data=df, stack=False)

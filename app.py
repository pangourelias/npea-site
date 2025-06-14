import streamlit as st

st.set_page_config(page_title="NPEA | About", layout="centered")

st.image("assets/logo.png", width=120)

st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="margin-top:10px;">Neighborhood Prank Enforcement Authority</h1>
        <h3 style="color:gray;">Division of Snack Security & Lawn Order</h3>
        <hr style="margin-top:30px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    ### 🚨 Official About Page

    The **Neighborhood Prank Enforcement Authority (NPEA)** is a semi-legitimate organization dedicated to the investigation, documentation, and prevention of suspicious prank activity in residential zones.

    **Our jurisdiction includes:**
    - Toilet-papered trees
    - Ding-dong-ditch incidents
    - Snack theft
    - Suspicious garden gnome relocation

    We operate with unverified authority but unwavering commitment to comedic justice.
    """
)

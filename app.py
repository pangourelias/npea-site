import streamlit as st
import time

# ---- Page Setup ----
st.set_page_config(page_title="NPEA | Home", layout="centered")

# ---- Logo Header ----
st.image("assets/logo.png", width=160)

st.markdown(
    """
    <div style='text-align:center;'>
        <h1 style='font-size: 2.2em;'>Neighborhood Prank Enforcement Authority</h1>
        <h3 style='color:gray;'>A division of Unnecessary Oversight and Mirthful Security</h3>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Animated "Terminal"-style Text ----
with st.container():
    st.markdown("### Initializing Secure Portal…")
    with st.spinner("Verifying snack inventory..."):
        time.sleep(1.5)
    st.success("Snack inventory confirmed.")
    time.sleep(0.5)
    st.markdown("#### Access granted: Level 7 Prank Response Unit")

# ---- Welcome Text ----
st.markdown(
    """
    <div style="margin-top:30px;">
    <p style="font-size:1.1em;">
        Welcome to the **NPEA**, the only agency brave enough to tackle backyard buffoonery, mailbox mayhem, and unauthorized glitter deployment.
    </p>
    <p>
        Our mission? To investigate prank-related incidents and report them with excessive bureaucracy and mild amusement.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Buttons to Navigate (future setup) ----
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("app.py", label="Home", icon="🏠")

with col2:
    st.page_link("pages/about.py", label="About", icon="📄")

with col3:
    st.page_link("pages/cases.py", label="Cases", icon="🗂️")

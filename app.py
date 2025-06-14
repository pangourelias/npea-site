import streamlit as st
import os

# Page setup
st.set_page_config(page_title="NPEA | Secure Portal", layout="centered")

# Init session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Logo
st.image("assets/logo.png", width=160)

# --- LOGIN ---
if not st.session_state.logged_in:
    st.title("Neighborhood Prank Enforcement Authority")
    st.subheader("🔐 Secure Access Portal")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "winnie" and password == "ironman":
            st.session_state.logged_in = True
            st.success("Access granted.")
            st.rerun()
        else:
            st.error("Invalid credentials.")
    st.stop()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("📁 NPEA Menu")
    st.session_state.page = st.radio("Navigate to", ["Home", "Cases", "About"])

# --- PAGE CONTENT ---
if st.session_state.page == "Home":
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
    st.markdown("---")
    st.caption("This portal is monitored by the Department of Neighborhood Nonsense. Proceed with snacks.")

elif st.session_state.page == "About":
    st.subheader("📄 About NPEA")
    st.markdown(
        """
        The **Neighborhood Prank Enforcement Authority (NPEA)** is a semi-legitimate organization dedicated to the investigation, documentation, and prevention of suspicious prank activity in residential zones.

        **Our jurisdiction includes:**
        - Toilet-papered trees  
        - Ding-dong-ditch incidents  
        - Snack theft  
        - Suspicious garden gnome relocation  

        We operate with unverified authority but unwavering commitment to comedic justice.

        ### 🕵️ Mission Statement
        To document, discourage, and sometimes participate in neighborhood pranks — all in the name of fun and mild chaos.
        """
    )

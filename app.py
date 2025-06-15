import streamlit as st

st.set_page_config(page_title="NPEA | Home", layout="centered")

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

import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("🚫 Access denied. Please log in from the home page.")
    st.stop()

st.set_page_config(page_title="Cases | NPEA", layout="wide")
st.title("🗂️ Active Case Files")

# --- Helper: Render case card ---
def case_card(case_id, title, description, thumbnail_path, is_openable=False):
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(thumbnail_path, use_container_width=True)
        with cols[1]:
            st.markdown(f"### {title}")
            st.markdown(description)
            if st.button(f"Open Case {case_id}", key=case_id):
if is_openable:
    st.success(f"Access granted to case {case_id}.")

    st.markdown("### 🔍 Officer Report #1")
    st.markdown("NPEA issues video warning. Suspect urged to deliver snacks to victims to avoid further enforcement.")
    st.video("https://youtube.com/shorts/PCLYTv4beTY")

    st.markdown("---")
    st.markdown("### 🔍 Officer Report #2")
    st.markdown("Suspect ignored warning. NPEA responds by toilet-papering suspect’s tree. Further pranks promised if snacks not delivered.")
    st.video("https://www.youtube.com/shorts/NUJPnPf0zTA")

                else:
                    st.error("❌ Invalid credentials for this case.")
        st.markdown("---")


# --- Cases List ---
case_card(
    "BRB404SNAX",
    "🚨 Ding Dong Ditch",
    "A wild boy is making the rounds — ringing doorbells and vanishing into the night like a snack-fueled ninja. Neighbors report rising blood pressure and phantom chimes. Suspect has been seen laughing maniacally while sprinting barefoot across lawns.",
    "assets/Dingdongditch_thumb.png",
    is_openable=True
)

case_card(
    "Z00MGNOME",
    "🧙 Gnome Speed Violation",
    "Garden gnome clocked at 37km/h in a 10 zone. Suspect claims he was 'just enchanted'. Investigation ongoing.",
    "assets/zoomgnome_thumb.png"
)

case_card(
    "TP999999",
    "🧻 TP Incident — Level 3",
    "Multiple trees wrapped. Neighbors report strange laughter and a trail of Charmin Ultra Soft. No leads yet.",
    "assets/tp_incident_thumb.png"
)

case_card(
    "H00PFAIL",
    "🏀 Unauthorized Backboard Dunk",
    "Plastic flamingo used as a launchpad. Dunk successful, rim destroyed. Suspect recorded yelling 'Kobe!'",
    "assets/hoopfail_thumb.png"
)

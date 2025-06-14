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
            st.image(thumbnail_path, use_column_width=True)
        with cols[1]:
            st.markdown(f"### {title}")
            st.markdown(description)
            if st.button(f"Open Case {case_id}", key=case_id):
                if is_openable:
                    st.success(f"Access granted to case {case_id}.")
                    st.markdown("🔍 Officer report: Missing snack tray. Suspect fled on foot. Surveillance shows cookie crumbs at the scene.")
                    st.image("assets/brb404snax_evidence.png", caption="Fig. A — Last known cookie tray visual", use_column_width=True)
                else:
                    st.error("❌ Invalid credentials for this case.")
        st.markdown("---")


# --- Cases List ---
case_card(
    "BRB404SNAX",
    "🚨 Snack Violation + Officer Down",
    "Unauthorized consumption of treats followed by a driveway incident. Suspect escaped. Robot officer sustained minor leg damage.",
    "assets/snack_violation_thumb.png",
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

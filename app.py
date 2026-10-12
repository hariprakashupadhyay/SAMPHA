
import streamlit as st

st.set_page_config(
    page_title="SAMPHA",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 SAMPHA")
st.subheader("Your AI-Powered Wellness Companion")

st.write(
    "Welcome to SAMPHA! We are building a supportive "
    "AI application for mental wellness and general health information."
)

st.info(
    "This is our first prototype. More AI and ML features "
    "will be added step by step."
)

st.divider()

st.header("How are you feeling today?")

mood = st.selectbox(
    "Choose your current mood:",
    ["Select a mood", "Happy", "Calm", "Stressed", "Sad", "Tired"]
)

if st.button("Save my mood"):
    if mood == "Select a mood":
        st.warning("Please select a mood first.")
    else:
        st.success(f"Your selected mood is: {mood}")
        st.write(
            "Thank you for checking in. Remember to take "
            "care of yourself today."
        )

st.caption(
    "SAMPHA is a wellness support prototype, not a medical "
    "diagnostic tool."
)

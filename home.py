
import streamlit as st


# Set an anime-themed background and style
st.markdown(
    """
    <style>
    body, .stApp {
        background: linear-gradient(120deg, #f5e1ff 0%, #d4f5dd 100%);
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif;
    }
    .anime-title {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 1.5rem;
    }
    .anime-title img {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        width: 70px;
        height: 70px;
        object-fit: cover;
    }
    .anime-title h1 {
        font-size: 2.5rem;
        color: #7c3aed;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif;
        margin: 0;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px #fff, 0 2px 4px #b39ddb;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Anime title with Itachi image and title using Streamlit columns
col1, col2 = st.columns([1, 5])
with col1:
    st.image("MyImages/Itachi.png", width=70)
with col2:
    st.markdown(
        "<h1 style='font-size:2.5rem; color:#7c3aed; font-family:Comic Sans MS, Comic Sans, cursive, sans-serif; margin:0; letter-spacing:2px; text-shadow:2px 2px 8px #fff, 0 2px 4px #b39ddb;'>Tutoring Signup Form</h1>",
        unsafe_allow_html=True
    )

# Engaging hook to encourage signups
st.markdown(
    """
    <div style='font-size:1.2rem; color:#444; margin-bottom:1.5rem; background:rgba(255,255,255,0.7); border-radius:10px; padding:12px 18px; box-shadow:0 2px 8px #b39ddb33;'>
        <b>Ready to level up your learning, make new friends, and get help from awesome tutors? <span style='color:#7c3aed;'>Sign up now and join our anime-inspired tutoring adventure!</span></b>
    </div>
    """,
    unsafe_allow_html=True
)

# Display a header image if you have one in MyImages/
# st.image("MyImages/header.png", use_column_width=True)


with st.form("signup_form"):
    st.markdown("**First Name**")
    first_name = st.text_input("")
    st.markdown("**Last Name**")
    last_name = st.text_input("", key="last_name")
    st.markdown("**Background**")
    background = st.text_area("", key="background")
    st.markdown("**List of Courses**")
    courses = st.text_input("", key="courses")
    st.markdown("**Email Address**")
    email = st.text_input("", key="email")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not (first_name and last_name and background and courses and email):
            st.warning("Please fill in all fields before submitting.")
        else:
            st.success(f"Thank you for signing up, {first_name}!")
            st.write("**Here is the information you submitted:**")
            st.write(f"- **First Name:** {first_name}")
            st.write(f"- **Last Name:** {last_name}")
            st.write(f"- **Background:** {background}")
            st.write(f"- **List of Courses:** {courses}")
            st.write(f"- **Email Address:** {email}")
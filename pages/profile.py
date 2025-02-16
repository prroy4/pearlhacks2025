import streamlit as st
from supabase import create_client, Client
import bcrypt # type: ignore
from datetime import datetime
from pages.login import supabase

# Hide Streamlit sidebar
st.set_page_config(layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        .profile-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .profile-container h2 {
            text-align: center;
            color: #333;
        }
        .profile-item {
            font-size: 18px;
            margin: 10px 0;
        }
        .profile-photo {
            display: block;
            margin: 0 auto 20px auto;
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
    </style>
""", unsafe_allow_html=True)




st.title("User Profile")
print(st.session_state["user_info"])
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    if "user_info" in st.session_state:  # Check before accessing
        user_info = st.session_state["user_info"]
if user_info:
        st.markdown("""
        <div class='profile-container'>
            <img class='profile-photo' src='""" + user_info.get("photo", "https://via.placeholder.com/150") + """' alt='Profile Photo'>
            <h2>""" + user_info['first_name'] + " " + user_info['last_name'] + """</h2>
            <p class='profile-item'><strong>User Type:</strong> """ + user_info['user_type'] + """</p>
            <p class='profile-item'><strong>Email:</strong> """ + user_info['email'] + """</p>
            <p class='profile-item'><strong>Job Title:</strong> """ + (user_info.get('job_title', 'N/A')) + """</p>
            <p class='profile-item'><strong>Research Topic:</strong> """ + (user_info.get('research_topic', 'N/A')) + """</p>
            <p class='profile-item'><strong>Tags:</strong> """ + (', '.join(user_info.get('tags', []))) + """</p>
            <p class='profile-item'><strong>Bio:</strong> """ + (user_info.get('bio', 'No bio available')) + """</p>
            <p class='profile-item'><strong>Karma Points:</strong> """ + str(user_info.get('karma_points', 0)) + """</p>
            <p class='profile-item'><strong>Postings:</strong> """ + str(user_info.get('postings', 0)) + """</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.error("User profile not found.")


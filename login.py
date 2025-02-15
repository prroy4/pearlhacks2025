import streamlit as st
from supabase import create_client, Client
import bcrypt

# Supabase credentials
SUPABASE_URL = 'https://yzihcuoecprmoahkmejp.supabase.co'
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aWhjdW9lY3BybW9haGttZWpwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk2NTA3NzEsImV4cCI6MjA1NTIyNjc3MX0.LG7KNDoLGbLKaoFj3DCiX7Dzt25rnPc1vPDoTP0fJV0"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def authenticate(username, password):
    response = supabase.table("users").select("password").eq("username", username).execute()
    if response.data and check_password(password, response.data[0]["password"]):
        return True
    return False

def signup(username, password, email, first_name, last_name):
    hashed_password = hash_password(password)
    response = supabase.table("users").insert({
        "username": username,
        "password": hashed_password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
        "created_at": "now()"
    }).execute()
    return response.error is None

def login_page():
    st.title("Login Page")
    
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    
    if not st.session_state["authenticated"]:
        option = st.radio("Select an option", ["Login", "Sign Up"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if option == "Login":
            if st.button("Login"):
                if authenticate(username, password):
                    st.session_state["authenticated"] = True
                    st.success("Login successful!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid credentials. Please try again.")
        
        elif option == "Sign Up":
            email = st.text_input("Email")
            full_name = st.text_input("Full Name")
            if st.button("Sign Up"):
                if signup(username, password, email, full_name):
                    st.success("Account created successfully! Please log in.")
                else:
                    st.error("Sign-up failed. Username or email may already exist.")
    else:
        st.success("You are logged in!")
        if st.button("Logout"):
            st.session_state["authenticated"] = False
            st.experimental_rerun()

if __name__ == "__main__":
    login_page()
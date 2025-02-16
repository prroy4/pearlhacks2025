import streamlit as st
from supabase import create_client, Client
import bcrypt # type: ignore
from datetime import datetime

# Initialize Supabase client
SUPABASE_URL = "https://yzihcuoecprmoahkmejp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl6aWhjdW9lY3BybW9haGttZWpwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk2NTA3NzEsImV4cCI6MjA1NTIyNjc3MX0.LG7KNDoLGbLKaoFj3DCiX7Dzt25rnPc1vPDoTP0fJV0"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def get_user_info(username):
    response = supabase.table("users").select("username, user_type, first_name, last_name, email, created_at").eq("username", username).execute()
    return response.data[0] if response.data else None

# Validate username and password match
def authenticate(username, password):
    response = supabase.table("users").select("password, user_type").eq("username", username).execute()
    if response.data and check_password(password, response.data[0]["password"]):
        return response.data[0]["user_type"]
    return None

# Login to student or professor view
def redirect(username):
    response = supabase.table("users").select("user_type").eq("username", username).execute()
    print(response.data[0])
    if response.data[0]["user_type"] == "Student":
        st.switch_page("pages/student.py")
    else:
        st.switch_page("pages/professor_view.py")

def login(username, password):
    user_type = authenticate(username, password)
    if user_type:
        user_info = get_user_info(username)
        if user_info:
            st.session_state["authenticated"] = True
            st.session_state["user_type"] = user_type
            st.session_state["user_info"] = user_info
            print(st.session_state["user_info"])
            st.session_state["username"] = username
            st.success("Login successful!")
            redirect(username)
    else:
        st.error("Invalid credentials. Please try again.")


def signup(username, password, user_type, first_name, last_name, email):
    if user_type not in ["Student", "Professor"]:
        st.error("Invalid user type. Please select 'Student' or 'Professor'.")
        return False
    hashed_password = hash_password(password)
    try:
        # Update database with new user
        response = supabase.table("users").insert({
            "username": username,
            "password": hashed_password,
            "user_type": user_type,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "created_at": datetime.utcnow().isoformat()
        }).execute()
        return True
    except Exception as e:
        st.error(f"Sign-up failed: {e}")
        return False


def login_page():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    
    # If not yet logged in
    if not st.session_state["authenticated"]:
        st.title("Login Page")
        option = st.radio("Select an option", ["Login", "Sign Up"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if option == "Login":
            if st.button("Login"):
                login(username, password)
        
        elif option == "Sign Up":
            user_type = st.selectbox("User Type", ["Student", "Professor"])
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            if st.button("Sign Up"):
                if signup(username, password, user_type, first_name, last_name, email):
                    st.success("Account created successfully! Please log in.")
                else:
                    st.error("Sign-up failed. Username or email may already exist.")

if __name__ == "__main__":
    login_page()

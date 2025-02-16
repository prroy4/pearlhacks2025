import streamlit as st
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_header():
    profile_pic = image_to_base64("rachel.png")  # Replace with the actual profile image path
    st.markdown(
        f"""
        <style>
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 2px solid #ddd;
        }}
        .header-left {{
            flex: 1;
        }}
        .header-right {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .profile-photo {{
            width: 40px !important;
            height: 40px !important;
            border-radius: 50%;
            object-fit: cover;
            cursor: pointer;
        }}
        </style>
        <div class="header">
            <div class="header-left">
                <h1>TarHeel Trade</h1>
            </div>
            <div class="header-right">
                <img src="data:image/png;base64,{profile_pic}" class="profile-photo"> 
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def create_post():
    st.title("Create a New Post")
    
    # Input fields for title and role description
    title = st.text_input("Post Title", "")
    role_description = st.text_area("Role Description", "")
    
    if st.button("Submit Post"):
        if title and role_description:
            st.success("Post created successfully!")
            # Here you would typically save the post to a database or storage
        else:
            st.error("Please fill out all fields before submitting.")

# Main function to run the Streamlit app
def main():
    display_header()
    create_post()

if __name__ == "__main__":
    main()

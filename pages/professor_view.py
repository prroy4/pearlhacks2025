import streamlit as st
import base64

# Hide the sidebar

# Function to convert image to base64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Sample data for profiles
students = [
    {"user_type": "student", "name": "Alice Dogwood", "photo": "alice.png", "tags": ["cs", "statistics", "math"], "about": "Hi, my name is Alice! I am an undergraduate student at UNC-Chapel Hill. I'm passionate about data science, analytics, and visualization, and I have experience working on machine learning and data visualization projects via a summer internship.", "major": "Computer Science", "year": "2026", "resume": "Untitled.pdf", "karma": 10},
    {"user_type": "student", "name": "Bob Carpenter", "photo": "bob.png", "tags": ["cs", "physics"], "about": "I am an undergraduate sophomore student at UNC-Chapel Hill. I'm really interested in quantum computing, and I'm especially interested in developing quantum algorithms that are more computationally efficient.", "major": "Computer Science", "year": "2027", "resume": "Bob.pdf", "karma": 100},
]

# Function to display the header with profile photo and messages tab
def display_header():
    # Use custom CSS to position the profile photo and messages button in the top-right corner
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
        }
        .header-left {
            flex: 1;
        }
        .header-right {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .profile-photo {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            object-fit: cover;
            cursor: pointer;
        }
        .messages-button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            text-decoration: none;
        }
        .create-post-button {
            background-color:rgb(185, 100, 177);
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            text-decoration: none;
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 150px;
            text-align: center;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header layout
    st.markdown(
        """
        <div class="header">
            <div class="header-left">
                <h1 style='text-align: left;'>TarHeel Trade</h1>
            </div>
            <div class="header-right">
                <a href="/messages" target="_self">
                    <button class="messages-button">💬 Messages</button>
                </a>
                <a href="/?page=profile" target="_self">
                    <img src="data:image/png;base64,{photo_base64}" class="profile-photo">
                </a>
            </div>
        </div>
        """.format(photo_base64=image_to_base64("rachel.png")),  # Replace "rachel.png" with the logged-in user's photo
        unsafe_allow_html=True,
    )

# Function to display the messaging screen


# Function to display the swipe UI
def swipe_ui():
    if "student_index" not in st.session_state:
        st.session_state.student_index = 0  # Track the current student index

    if st.session_state.student_index < len(students):
        student = students[st.session_state.student_index]  # Get current profile

        # Create container for the profile card, button, and swipe actions
        with st.container():
            # Profile Card Style
            st.markdown(
                """
                <style>
                .card {
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 80%;
                    margin: auto;
                }
                .card .profile-photo {
                    border-radius: 50%;
                    width: 100px;
                    height: 100px;
                    object-fit: cover;
                    margin-bottom: 10px;
                }
                .profile-header {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 20px;
                    margin-bottom: 20px;
                }
                .swipe-btn {
                    padding: 10px 20px;
                    font-size: 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;  /* Make buttons fill the column */
                }
                .swipe-left {
                    background-color: #ff4b4b;
                    color: white;
                }
                .swipe-right {
                    background-color: #4CAF50;
                    color: white;
                }
                .create-post-button {
                    background-color:rgb(185, 100, 177);
                    color: white;
                    padding: 8px 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                    text-decoration: none;
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    width: 150px;
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            # Profile Information (Inside the card)
            photo_base64 = image_to_base64(student["photo"])

            st.markdown(f"""
                <div class='card'>
                    <div class="profile-header">
                        <img src="data:image/png;base64,{photo_base64}" class="profile-photo" width="100" height="100">
                        <h3>{student["name"]}</h3>
                    </div>
                    <p>{student["about"]}</p>
                    <p><b>Interests:</b> 
                        {" ".join([f'<span class="tag">{tag}</span>' for tag in student["tags"]])}
                    </p>
                </div>
                <style>
                    .tag {{
                        display: inline-block;
                        padding: 5px 10px;
                        margin: 2px;
                        background-color: #e0e0e0;
                        border-radius: 15px;
                        font-size: 14px;
                        color: #333;
                    }}
                </style>
            """, unsafe_allow_html=True)

            # Display Download Resume button below profile info, inside the card.
            try:
                with open(student["resume"], "rb") as resume_file:
                    resume_data = resume_file.read()
                    resume_base64 = base64.b64encode(resume_data).decode("utf-8")

                # Streamlit Download Button
                st.markdown(
                    f"""
                    <div class='card'>
                        <a href='data:application/pdf;base64,{resume_base64}' download='{student["name"]}_Resume.pdf'>
                            <button class='download-btn'>📥 Download Resume</button>
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            except FileNotFoundError:
                st.error("Resume file not found!")

            # Swipe buttons below profile and resume
            col1, col2, col3 = st.columns([1, 2, 1])  # Use columns to center the buttons

            with col2:
                col1, col2 = st.columns(2)  # Split the center column into two for the buttons

                with col1:
                    if st.button("❌ Swipe Left", key=f"left_{student['name']}", help="Swipe Left"):
                        st.session_state.student_index += 1  # Move to the next student
                        st.rerun()  # Refresh UI

                with col2:
                    if st.button("✅ Swipe Right", key=f"right_{student['name']}", help="Swipe Right"):
                        st.session_state.student_index += 1  # Move to the next student
                        st.rerun()  # Refresh UI
    else:
        st.markdown("<h3 style='text-align: center;'>No more profiles to show!</h3>", unsafe_allow_html=True)

    st.markdown(
    """
    <a href="/post" target="_self">
        <button class="create-post-button">➕ Create Post</button>
    </a>
    """,
    unsafe_allow_html=True,
    )

# Main app logic
def main():
    # Display the header
    display_header()

    # Check the URL query parameter to determine the current page
    #query_params = st.query_params
    #
    #if page == "messages":
        #messaging_screen()
    #elif page == "profile":
    #    st.write("This is the profile screen. You can implement your profile functionality here.")
    #else:
        
    swipe_ui()

# Run the app
if __name__ == "__main__":
    main()
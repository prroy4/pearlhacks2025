import streamlit as st
import base64

# Function to convert image to base64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Sample data for professors
professors = [
    {
        "user_type": "professor", 
        "name": "Dr. Rachel Smith", 
        "photo": "rachel.png", 
        "research_topic": "AI in Healthcare", 
        "tags": ["cs", "statistics"], 
        "job_title": "Research Assistant for AIHC Lab",
        "bio": "My research focuses on the application of Artificial Intelligence (AI) to solve critical challenges in healthcare. I explore how AI-driven tools, such as machine learning algorithms and natural language processing, can improve clinical decision-making and enhance patient outcomes. Specifically, I am interested in the development of AI models for early disease detection, predictive analytics, and personalized medicine.", 
        "research_opportunity": "We are looking for graduate students to join our team and work on AI-based tools for early disease detection. Experience with machine learning and medical data is a plus.", 
        "karma": 50,
        "posting": "The AIHC Lab is working on developing advanced machine learning models to assist in the early detection of breast cancer using mammogram images. The project aims to create AI-based diagnostic tools that can analyze mammogram images and detect subtle patterns indicative of early-stage breast cancer, which may not be visible to the human eye. The goal is to improve the accuracy and speed of early detection, enabling clinicians to provide timely interventions."
    },
    {
        "user_type": "professor", 
        "name": "Dr. Michael Johnson", 
        "photo": "michael.png", 
        "research_topic": "AI for Medical Robotics", 
        "tags": ["cs", "applied sciences"], 
        "job_title": "Lab Assistant - Robotics Institue",
        "bio": "My research focuses on the integration of Artificial Intelligence (AI) with medical robotics to enhance surgical precision and automate complex medical procedures. I explore how machine learning algorithms and computer vision can improve robotic-assisted surgeries, real-time diagnostics, and patient monitoring.", 
        "research_opportunity": "Looking for talented undergraduate students interested in AI applications in robotics. The role involves working on medical robotics systems and developing algorithms to enhance their accuracy.", 
        "karma": 40,
        "posting": "The Robotics Institude is focused on developing AI-driven robotic systems for spinal surgery. Our goal is to build a robotic-assisted surgical system that can automatically adjust the surgical tools during spinal surgeries with precise movements, minimizing human error and improving patient outcomes. We are using machine learning algorithms combined with real-time imaging to enable robotic systems to visualize the patient's spine in 3D and adjust their movements accordingly during the procedure. This project aims to increase the precision of spinal surgeries, reduce recovery times, and prevent complications such as misalignments."
    }
]

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
            width: 40px !important;
            height: 40px !important;
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

         .profile-button {
            background-color:rgb(76, 157, 175);
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

        .no-professors-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50vh;  /* Full viewport height */
            text-align: center;
            color: #333;
        }
        
        .no-professors-message {
            font-size: 24px;
            font-weight: bold;
            color:rgb(13, 16, 13);  /* Green for emphasis */
            padding: 20px;
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
        """.format(photo_base64=image_to_base64("alice.png")), 
        unsafe_allow_html=True,
    )

if "professor_index" not in st.session_state:
    st.session_state.professor_index = 0  # Track the current professor index

def professor_view():
    if st.session_state.professor_index < len(professors):
        professor = professors[st.session_state.professor_index]  # Get current professor
        
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
                .profile-photo {
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
                .button-container {
                    position: absolute;
                    bottom: 20px;  /* Adjust this value to position it vertically */
                    left: 50%;
                    transform: translateX(-50%);  /* Center the buttons horizontally */
                    display: flex;
                    justify-content: space-between;
                    gap: 20px;
                    width: 300px;  /* Optional: adjust button container width */
                }
                .button-container button {
                    padding: 10px 20px;
                    font-size: 16px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 120px;  /* Added width for consistency */
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

                .no-professors-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;  /* Full viewport height */
                    text-align: center;
                    color: #333;
                }
                .no-professors-message {
                    font-size: 24px;
                    font-weight: bold;
                    color: #4CAF50;  /* Green for emphasis */
                    padding: 20px;
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    background-color: #f4f4f9;  /* Light background for the message */
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            
            photo_base64 = image_to_base64(professor["photo"])

            # Profile Header with Photo and Name
            st.markdown(f"""
                <div class='card'>
                    <div class="profile-header">
                        <h3>{professor["job_title"]}</h3>
                    </div>
                    <img src="data:image/png;base64,{photo_base64}" class="profile-photo" width="100" height="100">
                    <h4>{professor["name"]}</h4>
                    <p><strong>Project Description Topic:</strong> {professor["posting"]}</p>
                    <p><b>Research Opportunity:</b> {professor["research_opportunity"]}</p>
            """, unsafe_allow_html=True)

            # Centered Swipe buttons below professor info
           
            col1, col2, col3 = st.columns([1,2,1])
            with col2:


                col1, col2 = st.columns(2)
                #st.markdown('<div class="button-container">', unsafe_allow_html=True)  # Open button container
                with col1:
                    if st.button("❌ Not Interested", key=f"reject_{professor['name']}", help="Reject the professor's opportunity"):
                       st.session_state.professor_index += 1  # Move to the next professor
                       st.rerun()  # Refresh UI


                with col2:
                    if st.button("✅ Interested", key=f"accept_{professor['name']}", help="Accept the professor's opportunity"):
                       st.session_state.professor_index += 1  # Move to the next professor
                       st.rerun()  # Refresh UI
                st.markdown('</div>', unsafe_allow_html=True)  # Close button container

    else:
        st.markdown('<div class="no-professors-container"><div class="no-professors-message">No more postings to show!</div></div>', unsafe_allow_html=True)



# Main App UI
def main():
    display_header()
    professor_view()

if __name__ == "__main__":
    main()
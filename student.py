import streamlit as st
import base64

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
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            
            # Profile Header with Photo and Name
            st.markdown(f"""
                <div class='card'>
                    <div class="profile-header">
                        <h3>{professor["job_title"]}</h3>
                    </div>
                     <img src="{professor['photo']}" class="profile-photo" alt="{professor['name']}">
                        <h4>{professor["name"]}</h4>
                    <p><strong>Project Description Topic:</strong> {professor["posting"]}</p>
                    <p><b>Research Opportunity:</b> {professor["research_opportunity"]}</p>
            """, unsafe_allow_html=True)

            # Centered Swipe buttons below professor info
            with st.container():
                st.markdown('<div class="button-container">', unsafe_allow_html=True)  # Open button container
                if st.button("❌ Not Interested", key=f"reject_{professor['name']}", help="Reject the professor's opportunity"):
                    st.session_state.professor_index += 1  # Move to the next professor
                    st.rerun()  # Refresh UI

                if st.button("✅ Interested", key=f"accept_{professor['name']}", help="Accept the professor's opportunity"):
                    st.session_state.professor_index += 1  # Move to the next professor
                    st.rerun()  # Refresh UI
                st.markdown('</div>', unsafe_allow_html=True)  # Close button container

    else:
        st.write("No more professors to show!")

# Main App UI
st.markdown("<h1 style='text-align: center;'>TarHeel Research Opportunities</h1>", unsafe_allow_html=True)

menu = ["View Professors"]
choice = st.sidebar.selectbox("Navigation", menu)

professor_view()

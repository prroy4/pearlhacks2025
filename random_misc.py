import streamlit as st
import pandas as pd
import random

# Sample student applications (Would be stored in a real database)
students = [
    {"name": "Alice Dogwood", "photo": "alice.png", "tags": ["cs", "statistics", "math"], "about": "Hi, my name is Alice! I am an undergraduate student at UNC-Chapel Hill. I'm passionate about data science, analytics, and visualization, and I have experience working on machine learning and data visualization projects via a summer internship.", "major": "Computer Science", "year": "2026", "resume": "Lesson 9_GRQs_Mitosis, Development, and Cancer.pdf", "karma": 10},
    {"name": "Bob Carpenter", "photo": "bob.png", "tags": ["cs", "physics"], "about": "I am an undergraduate sophomore student at UNC-Chapel Hill. I'm really interested in quantum computing, and I'm especially interested in developing quantum algorithms that are more computationally efficient.", "major": "Computer Science", "year": "2027", "resume": "Bob.pdf", "karma": 100},
]

professors = [
    {"name": "Dr. Rachel Smith", "photo": "rachel.png", "research-topic": "AI in Healthcare", "tags": ["cs", "statistics"], "description": "My research focuses on the application of Artificial Intelligence (AI) to solve critical challenges in healthcare. I explore how AI-driven tools, such as machine learning algorithms and natural language processing, can improve clinical decision-making and enhance patient outcomes. Specifically, I am interested in the development of AI models for early disease detection, predictive analytics, and personalized medicine. A major component of my work involves designing algorithms that can interpret complex medical data, including medical imaging and electronic health records, to aid in more accurate diagnoses and treatment planning.", "bio": "Dr. Rachel Smith is a professor of Computer Science at the University of North Carolina (UNC), specializing in Artificial Intelligence in healthcare. She earned her Ph.D. in Computer Science from MIT, following a Master’s in Statistics from Harvard University and a Bachelor’s in Computer Science from the University of California, Berkeley."},
    {"name": "Dr. Michael Johnson", "photo": "michael.png", "research-topic": "AI for Medical Robotics", "tags": ["cs", "applied sciences"], "description": "My research focuses on the integration of Artificial Intelligence (AI) with medical robotics to enhance surgical precision and automate complex medical procedures. I explore how machine learning algorithms and computer vision can improve robotic-assisted surgeries, real-time diagnostics, and patient monitoring. Specifically, I am interested in developing AI models that enable robotic systems to interpret sensory data, adapt to dynamic environments, and assist surgeons with increased accuracy and efficiency.", "bio": "Dr. Michael Johnson is a professor of Computer Science at the University of North Carolina at Chapel Hill, specializing in AI-driven medical robotics. He earned his Ph.D. in Computer Science from Stanford University, following a Master’s in Robotics from Carnegie Mellon University and a Bachelor’s in Mechanical Engineering from the University of Illinois at Urbana-Champaign."}
]

# Store student applications in session state for dynamic updates
if "applications" not in st.session_state:
    st.session_state.applications = students.copy()

if "research_posts" not in st.session_state:
    st.session_state.research_posts = []

# Function for professors to view & approve/reject applications
def professor_dashboard():
    st.write("### Pending Applications")
    
    if st.session_state.applications:
        for student in st.session_state.applications:
            with st.container():
                st.subheader(f"🔹 {student['name']}")
                st.write(f"**Major & Year:** {student['major']} ({student['year']})")
                st.write(f"**Research Interests:** {', '.join(student['tags'])}")
                st.write(f"**About:** {student['about']}")
                st.write(f"**Karma Points:** {student['karma']}")
                
                # Download Resume Button
                try:
                    with open(student["resume"], "rb") as resume_file:
                        resume_data = resume_file.read()

                    st.download_button(
                        label="📥 Download Resume",
                        data=resume_data,
                        file_name=f"{student['name']}_Resume.pdf",
                        mime="application/pdf",
                        key=f"download_{student['name']}"  # Unique key
                    )
                except FileNotFoundError:
                    st.error("Resume file not found!")


                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Approve {student['name']}", key=f"approve_{student['name']}"):
                        st.success(f"{student['name']} has been approved!")
                        st.session_state.applications.remove(student)
                        st.experimental_rerun()
                with col2:
                    if st.button(f"Reject {student['name']}", key=f"reject_{student['name']}"):
                        st.warning(f"{student['name']} has been rejected.")
                        st.session_state.applications.remove(student)
                        st.experimental_rerun()
    else:
        st.write("No pending applications!")

# Function to create new research projects
def create_research_post():
    st.write("### 📝 Create a New Research Post")
    
    title = st.text_input("Research Title")
    description = st.text_area("Project Description")
    tags = st.multiselect("Tags", ["AI", "ML", "Math", "Stats", "Data Science", "Engineering"])
    
    if st.button("📢 Post Research"):
        new_post = {"title": title, "description": description, "tags": tags}
        st.session_state.research_posts.append(new_post)
        st.success("Your research post has been created!")

# App Layout
st.title("🔬 TarHeel Trade – Research & Skill Collaboration")

# Sidebar navigation for students and professors
user_type = st.sidebar.radio("Login As:", ["Student", "Professor"])

if user_type == "Professor":
    menu = ["Approve Applications", "Post Research"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Approve Applications":
        professor_dashboard()
    elif choice == "Post Research":
        create_research_post()

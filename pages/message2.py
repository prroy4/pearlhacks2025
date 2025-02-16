import streamlit as st
from datetime import datetime
import base64

# Function to convert image to base64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to display the messaging screen
def messaging_screen():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
        }
        .profile-photo {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            object-fit: cover;
            cursor: pointer;
        }
        .back-button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            text-decoration: none;
        }
        .center {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header with back button and profile photo
    st.markdown(
        """
        <div class="header">
            <a href="/professor_view" target="_self">
                <button class="back-button">← Back</button>
            </a>
            <img src="data:image/png;base64,{photo_base64}" class="profile-photo">
        </div>
        """.format(photo_base64=image_to_base64("alice.png")),  # Replace "alice.png" with Alice's photo
        unsafe_allow_html=True,
    )

    # Centered title and top text
    st.markdown("<h1 style='text-align: center;'>Messages</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>You matched with Dr. Rachel Smith on 2023-10-01.</p>", unsafe_allow_html=True)

    # Simulate a conversation
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"sender": "Dr. Rachel Smith", "message": "Hi Alice! I saw your profile and thought your background in data science would be a great fit for my research.", "time": "2023-10-01 10:00:00"},
            {"sender": "Alice Dogwood", "message": "Hi Dr. Smith! Thank you for reaching out. I'm really interested in your work on AI in healthcare.", "time": "2023-10-01 10:05:00"},
            {"sender": "Dr. Rachel Smith", "message": "That's great to hear! Would you like to discuss potential research opportunities?", "time": "2023-10-01 10:10:00"},
            {"sender": "Alice Dogwood", "message": "Absolutely! When would be a good time for a meeting?", "time": "2023-10-01 10:15:00"},
        ]

    # Display the conversation
    st.markdown("---")
    st.markdown("### Conversation")

    for msg in st.session_state.messages:
        if msg["sender"] == "Dr. Rachel Smith":
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-start; margin-bottom: 10px;">
                    <div style="background-color: #f0f0f0; padding: 10px; border-radius: 10px; max-width: 70%;">
                        <strong>{msg["sender"]}</strong><br>
                        {msg["message"]}<br>
                        <small>{msg["time"]}</small>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
                    <div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 10px; max-width: 70%;">
                        <strong>{msg["sender"]}</strong><br>
                        {msg["message"]}<br>
                        <small>{msg["time"]}</small>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Input for new messages
    st.markdown("---")
    new_message = st.text_input("Type a message...", key="new_message")

    if st.button("Send"):
        if new_message.strip():
            # Add the new message to the conversation
            st.session_state.messages.append({
                "sender": "Alice Dogwood",  # Assuming Alice is the one sending the message
                "message": new_message,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.rerun()  # Refresh the page to display the new message

# Run the messaging screen
if __name__ == "__main__":
    messaging_screen()
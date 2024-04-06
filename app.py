from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from streamlit_option_menu import option_menu

load_dotenv()
api = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-pro')

with st.sidebar:
    selected = option_menu(
        menu_title = "Index",
        options = ["Main Page", "Write an Email", "Reply to an Email","Contact"],
        menu_icon = "cast"
    )

if selected == "Main Page":
    st.image("logo.png", width=100)
    st.title("Welcome to Emaily: The AI-Powered Email Assistant")

    # Introduction to the application
    st.write("""
    Emaily leverages cutting-edge generative AI to help you draft and reply to emails effortlessly. Whether you need to write a formal email to a colleague or craft a friendly note to a friend, Emaily has you covered.
    """)

    # Features overview
    st.header("Features")
    st.write("""
    - **Write an Email:** Generate custom emails based on your specific needs, tone, and relationship with the recipient.
    - **Reply to an Email:** Craft thoughtful and appropriate responses to the emails you receive.
    """)

    # How to use the application
    st.header("How to Use Emaily")
    st.write("""
    1. Navigate using the menu on the left.
    2. Choose between writing a new email or replying to an existing one.
    3. Fill in the required information such as the recipient's name, your relationship with them, the purpose of the email, and the preferred tone.
    4. Hit the "Go" button and let Emaily generate a tailor-made email for you.
    """)

    # Ending note
    st.write("Start crafting your emails with ease and confidence. Choose an option from the sidebar to begin!")
    st.divider()

if selected == "Write an Email":
    st.image("logo.png", width=100)
    st.title("Emaily: The AI-Powered Email Assistant")
    st.markdown("""Use Emaily to craft personalized emails effortlessly. Just fill in the details about the recipient, your relationship, the email's purpose, and the tone you'd like to set. Emaily will then generate a bespoke email that you can send with confidence.""")

    st.divider()

    st.subheader("Email recipient:")
    recipient = st.text_area(label=" ", value="",placeholder="Recipient Name", height=100, key=1)

    st.subheader("Relationship With Recipient:")
    recipient_rel = st.text_area(label=" ", value="", height=100, key=2)

    st.subheader("Purpose:")
    purpose = st.text_area(label=" ", value="", placeholder="Add Details and Context", height=200, key=3)

    st.subheader("Tone of the email:")
    tone_type = ["Formal", "Informal", "Friendly", "Professional", "Persuasive"]
    selected_tone = st.selectbox("Choose an option:", tone_type)

    st.subheader("Length:")
    options = ["Brief", "Descriptive"]
    selected_length = st.radio("Choose an option:", options)

    prompt = f'''
    Given the inputs provided, compose an email that addresses the recipient by name, fulfills the specified purpose, matches the desired tone, and adheres to the requested length. 
    Ensure the email is clear, well-organized, and effectively communicates its message.
    Email Recipient: {recipient}
    Relationship with Recipint: {recipient_rel}
    Purpose: {purpose}
    Tone: {selected_tone}
    Length:{selected_length}
    '''

    if st.button(label="Go"):
        if not recipient or not recipient_rel or not purpose:
            st.error("Please ensure all fields are filled out.")
        else:
            with st.spinner('Generating your email...'):
                try:
                    result = model.generate_content(prompt)

                    if result.text:
                        st.write(result.text)
                        st.success("Email generated successfully!")
                    else:
                        st.error("Failed to generate email content. Please try again.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    st.divider()

if selected == "Reply to an Email":
    st.image("logo.png", width=100)
    st.title("Emaily: The AI-Powered Email Assistant")
    st.markdown("""Responding to emails has never been easier. Provide Emaily with the email you've received, your relationship with the sender, and the details you wish to include in your reply. Choose the tone, and Emaily will generate a thoughtful response for you.""")

    st.divider()

    st.subheader("Email Received:")
    received = st.text_area(label=" ", value="",placeholder="Reply to this email", height=200, key=4)

    st.subheader("Relationship With Sender:")
    sender_rel = st.text_area(label=" ", value="", height=100, key=5)

    st.subheader("Details:")
    details = st.text_area(label=" ", value="", placeholder="Add Details and Context what you what to reply", height=100, key=3)

    st.subheader("Tone of the email:")
    tone_type = ["Formal", "Informal", "Friendly", "Professional", "Persuasive"]
    selected_tone = st.selectbox("Choose an option:", tone_type)

    st.subheader("Length:")
    options = ["Brief", "Descriptive"]
    selected_length = st.radio("Choose an option:", options)

    prompt = f'''
    Given the inputs provided, compose an email replying to the given email that addresses the recipient by name, fulfills the specified purpose, matches the desired tone, and adheres to the requested length. 
    Ensure the email is clear, well-organized, and effectively communicates its message.
    Email Recived: {received}
    Relationship with Recipint: {sender_rel}
    Details: {details}
    Tone: {selected_tone}
    Length:{selected_length}
    '''

    if st.button(label="Go"):
        if not received:
            st.error("Please enter the email received.")
        elif not sender_rel:
            st.error("Please describe your relationship with the recipient.")
        elif not details:
            st.error("Please enter the details about what you what to reply to the email received.")
        else:
            with st.spinner('Generating your email...'):
                try:
                    result = model.generate_content(prompt)
                    if result.text:
                        st.write(result.text)
                    else:
                        st.error("Failed to generate email content. Please try again.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    st.divider()

if selected == "Contact":
    st.image("logo.png", width=100)
    st.title("Contact Me")

    st.write("Feel free to reach out to me through any of the following platforms:")
    st.divider()
    st.write(f"📧 Email: [pnaik7@buffalo.edu](mailto:pnaik7@buffalo.edu)")

    st.write(f"🔗 LinkedIn: [linkedin.com/in/pratiksha-naikk](https://www.linkedin.com/in/pratiksha-naikk/)")

    st.write(f"👨‍💻 GitHub: [github.com/adiimated](https://github.com/adiimated)")

    st.write(f"🌐 Portfolio: [adiimated.github.io/portfolio](https://adiimated.github.io/portfolio/)")

    st.divider()

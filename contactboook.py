import streamlit as st
import time

# Function to display contacts as a table
def display_contact():
    contact_data = []
    for name, phone in session.contact.items():
        contact_data.append({"Name": name, "Contact Number": phone})
    
    if contact_data:
        st.table(contact_data)
    else:
        st.write("No contacts available.")

# Function to handle form submission
def handle_form_submit():
    name = st.session_state.name
    phone = st.session_state.phone
    action = st.session_state.action
    
    if action == "Add new Contact":
        if name not in session.contact:
            session.contact[name] = phone
            st.success("Contact added successfully!")
        else:
            st.error("Contact already exists!")
    elif action == "Edit Contact":
        if name in session.contact:
            session.contact[name] = phone
            st.success("Contact updated successfully!")
        else:
            st.error("Name is not found in contact book")
    elif action == "Delete Contact":
        if name in session.contact:
            del session.contact[name]
            st.success("Contact deleted successfully!")
        else:
            st.error("Name is not found in contact book")

# Function for the home page
def home():
    st.title("Welcome to BanoQabil 2.0 Final Project !")
    st.write("Contact Management Diary ")
    st.markdown(
        """
        <style>
        .logo-container {
            position: fixed;
            top: 80px;
            right: 20px;
            z-index: 1;
        }
        </style>
        <div class="logo-container">
            <img src="https://edunewspk.com/wp-content/uploads/2022/10/Bano-Qabil-Online-Registration-2022-Last-Date.png" width="100">
        </div>
        """,
        unsafe_allow_html=True
    )

# Function for the about page
def about():
    st.title("Contacts Management")
    st.write("Loading:")
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Progress: {i + 1}%")
        time.sleep(0.1)
    display_contact()

    with st.form(key="contact_form"):
        action = st.selectbox("Choose an option:", ["Add new Contact", "Edit Contact", "Delete Contact"], key="action")
        name = st.text_input("Enter the contact name", key="name")
        phone = st.text_input("Enter the Mobile Number", key="phone")
        st.form_submit_button("Submit", on_click=handle_form_submit)

# Function for the contact page
def contact():
    st.title("Contact Page")
    st.write("Made By Muhammad Musaddiq")
    st.write("Helping Patners (Maooz Bin Abdul Moid And Anas Jamal)")
    st.write("If you want to contact with me Kindly Message on This")
    st.write("Gmail muhammadmusaddiq49@gmail.com")
    st.write("Linkedln Id")
    st.write("1-Muhammad Musaddiq https://www.linkedin.com/in/muhammad-musaddiq-b82b192b3?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app")
    st.write("2-Maooz  https://www.linkedin.com/in/maooz-bin-moid-ab6229208/")
    st.write("3-Anas  https://www.linkedin.com/in/anas-bangash-9008512b3")
    st.write("Contact No 03166922805(Muhammad Musaddiq)")
    st.write("Github Id")
    st.write("Muhammad Musaddiq https://github.com/muhammadmusaddiq/Final-Project-.git")
    st.markdown(
        """
        <style>
        .logo-container {
            position: fixed;
            top: 80px;
            right: 20px;
            z-index: 1;
        }
        </style>
        <div class="logo-container">
            <img src="https://edunewspk.com/wp-content/uploads/2022/10/Bano-Qabil-Online-Registration-2022-Last-Date.png" width="100">
        </div>
        """,
        unsafe_allow_html=True
    )

# Function to define the main behavior of the app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "About", "Contact"))

    if page == "Home":
        home()
    elif page == "About":
        about()
    elif page == "Contact":
        contact()

# Use a session state to store the contact dictionary
session = st.session_state
if "contact" not in session:
    session.contact = {}

if __name__ == "__main__":
    main()

    

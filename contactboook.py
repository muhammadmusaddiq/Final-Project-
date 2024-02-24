import streamlit as st
import time

def display_contact():
    st.write("Name\t\t: Contact Number")
    for key in session.contact:
        st.write("{}\t\t{}".format(key, session.contact.get(key)))

def handle_form_submit():
    name = st.session_state.name
    phone = st.session_state.phone
    action = st.session_state.action
    
    if action == "Add new Contact":
        session.contact[name] = phone
        st.success("Contact added successfully!")
    elif action == "Search Contact":
        if name in session.contact:
            st.success(f"{name}'s contact number is {session.contact[name]}")
        else:
            st.error("Name is not found in contact book")
    elif action == "Edit Contact":
        if name in session.contact:
            session.contact[name] = phone
            st.success("Contact updated successfully!")
        else:
            st.error("Name is not found in contact book")
    elif action == "Delete Contact":
        if name in session.contact:
            session.contact.pop(name)
            st.success("Contact deleted successfully!")
        else:
            st.error("Name is not found in contact book")

def home():
    st.title("Welcome to BanoQabil 2.0 Final Project !")
    st.write("Contact Management Diary ")

def about():
    st.title("About Page")
    st.write("Welcome to the About Page!")
    st.write("This is our final Project of BanoQabil.")
    st.write("Loading:")
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Progress: {i + 1}%")
        time.sleep(0.1)
    st.title("Contact Management System")
    with st.form(key="contact_form"):
        action = st.selectbox("Choose an option:", ["Add new Contact", "Search Contact", "Edit Contact", "Delete Contact"], key="action")
        name = st.text_input("Enter the contact name", key="name")
        phone = st.text_input("Enter the Mobile Number", key="phone")
        st.form_submit_button("Submit", on_click=handle_form_submit)
    
    display_contact()

def contact():
    st.title("Contact Page")
    st.write("Welcome (In that Project 3 Members are included Name are mention below) !")
    st.write("Muhammad Musaddiq Maooz Bin Abdul Moid And Anas Bangesh .")

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


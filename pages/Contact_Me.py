import streamlit as st
from send_email.send_email import send_email

st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Write your email address, please: ')
    raw_message = st.text_area('Write your message, please: ', max_chars=250)
    message = f'''\
        Subject : New email from {user_email}
        From: {user_email}
        {raw_message}'''
    button = st.form_submit_button('Submit')
    try:
        if button:
            with st.spinner(text='In progress'):
                st.balloons()
                send_email(message)
                st.info('Your email has been sent successfully.')
    except TimeoutError:
        st.warning('Sorry! The message was not successfully sent.')

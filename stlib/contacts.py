from PIL import Image
import streamlit.components.v1 as stc
import pandas as pd
import requests
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
import streamlit_nested_layout

def contacts_page():
    with st.container():
        def load_lottieurl(url):
            r=requests.get(url)
            if r.status_code!= 200:
                return None
            return r.json()

    # Use local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")

        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        img_contact_form = Image.open("images/yt_contact_form.png")
        img_lottie_animation = Image.open("images/yt_lottie_animation.png")
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/mahadi.din@gmail.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

footer="""
                <style>
                    a:link , a:visited{
                    color: blue;
                    background-color: transparent;
                    text-decoration: underline;
                    }

                    a:hover,  a:active {
                    color: red;
                    background-color: transparent;
                    text-decoration: underline;
                    }

                    .footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-color: white;
                    color: black;
                    text-align: center;
                    }
                </style>
                <div class="footer">
                <p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Md. Al-Mahadi Hasan</a></p>
                </div>
            """
st.markdown(footer,unsafe_allow_html=True)
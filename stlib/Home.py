from PIL import Image
import streamlit.components.v1 as stc
import pandas as pd
import requests
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
import streamlit_nested_layout

def main_page():
    

    with st.container():
        st.write("---")
        #left_column1, right_column2 = st.columns(2)
        st.markdown("<h1 style='text-align: center; color: red;'>Data Science with Python</h1>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: center; color: white;'>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections.</h5>", unsafe_allow_html=True)    
        
            
            

    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center; color: red;'>How to do it?</h1>", unsafe_allow_html=True)
        st.write("##")



    with st.container():
        st.write("---")
        #st.header(":heartpulse:")
        st.write("##")
        column_1, column_2, column_3, column_4= st.columns((1, 1, 1, 1))
        with column_1:
            st.markdown("<h1 style='text-align: center; color: white;'>Upload file </h1>", unsafe_allow_html=True)
            st.write("###")
            st.markdown("<h5 style='text-align: center; color: white;'>Choose a CSV file to upload data and get started.</h5>", unsafe_allow_html=True)

            #if agree:
                #st.write('Great!')
        with column_2:
            st.markdown("<h1 style='text-align: center; color: white;'>Algorithm & Train</h1>", unsafe_allow_html=True)
            st.write("###")
            st.markdown("<h5 style='text-align: center; color: white;'>Train the application using the data file</h5>", unsafe_allow_html=True)

        with column_3:
            st.markdown("<h1 style='text-align: center; color: white;'>Choose other parameters</h1>", unsafe_allow_html=True)
            st.write("###")
            st.markdown("<h5 style='text-align: center; color: white;'>Please choose the country, education and experience</h5>", unsafe_allow_html=True)
        
        with column_4:
            st.markdown("<h1 style='text-align: center; color: white;'>Result</h1>", unsafe_allow_html=True)
            st.write("###")
            st.markdown("<h5 style='text-align: center; color: white;'>See the results</h5>", unsafe_allow_html=True)

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
                <p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.streamlit.com/" target="_blank">Md. Al-Mahadi Hasan</a></p>
                </div>
            """
st.markdown(footer,unsafe_allow_html=True)
    
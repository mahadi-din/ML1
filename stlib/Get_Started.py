from PIL import Image
import streamlit.components.v1 as stc
import pandas as pd
import requests
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
import streamlit_nested_layout
import warnings
warnings.filterwarnings('ignore')

def upload_file():
    
    st.write("---")
    st.markdown("<h1 style='text-align: center; color: red;'>Upload a file</h1>", unsafe_allow_html=True)
    st.write("##")



    #with st.container():
    st.write("---")
        #st.header(":heartpulse:")
    st.write("##")

    
    column_1, column_2= st.columns((2,1))
    with column_1:
            st.markdown("<h1 style='text-align: left; color: white;'>Steps</h1>", unsafe_allow_html=True)
            st.write("###")
            st.markdown("<h5 style='text-align: left; color: red;'>1. Upload a file</h5>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: left; color: white;'>2. Select an Algorithm</h5>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: left; color: white;'>3. Select other parameters</h5>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: left; color: white;'>4. Results</h5>", unsafe_allow_html=True)
            #if agree:
                #st.write('Great!')
    with column_2:
            st.markdown("<h1 style='text-align: center; color: white;'>Upload the file here</h1>", unsafe_allow_html=True)
            st.write("##")
            uploaded_file = st.file_uploader("")
            ok = st.button("Upload file")
            if ok:
                if ok == 'NoneType':
                    st.subheader("Please upload a file first.")
                else:
                    df = pd.read_csv(uploaded_file)
                    
    return df
    #from stlib.algorithm import select_algorithm
    #select_algorithm(df)

with st.container():
            selected1= option_menu(
                menu_title=None,
                options=["Upload file","Algorithm",'Parameters','Result'], 
                icons=['house', 'gear', 'envelope'], 
                menu_icon="cast", 
                default_index=0,
                orientation="horizontal",
                styles={
                "container": {"padding": "0!important", "background-color": "#00172B"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "red"},
                "nav-link-selected": {"background-color": "green"},
                }
            )

if selected1=="Upload file":
    df=upload_file()
#if selected1=="Algorithm":
while df is not None:
        from stlib import algorithm
        algorithm.select_algorithm(df)
        
else:
                #from stlib import Get_Started
                #df=Get_Started.upload_file()
        st.subheader("Please Upload a CSV file first.")
if selected1=='Parameters':
                from stlib import contacts
                contacts.contacts_page()
elif selected1=='Result':
                from stlib import contacts
                contacts.contacts_page()

#@st.experimental_memo(suppress_st_warning=True)
          

                   

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
    
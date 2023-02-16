from PIL import Image
import streamlit.components.v1 as stc
import pandas as pd
import requests
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
import streamlit_nested_layout


#class web_page:

    #def __init__(self) -> None:
       #"""Constructor class to generate a list which will store all our applications as an instance variable."""
        #self.stlib = []
st.set_page_config(page_title="Mahadi's Webpage", page_icon=":fire:", layout="wide")


with st.container():
        left_column, right_column = st.columns((1,2))

        with left_column:
            selected= option_menu(
                menu_title=None,
                options=["Home","Get Started",'Cotacts'], 
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

        with right_column:
            st.markdown("<h1 style='text-align: right; color: white;'>Machine Learning</h1>", unsafe_allow_html=True)

with st.container():
        if selected=="Home":
                from Home import main_page
                main_page()
        elif selected=="Get Started":
                
                from Get_Started import upload_file
                global df
                df=upload_file()
                #from algorithm import select_algorithm
                #select_algorithm(df)
        elif selected=='Cotacts':
                from contacts import contacts_page
                contacts_page()



                
                #selected=st.markdown(buttons, unsafe_allow_html= True)
                
            
    #          if selected == "Home":
    #               st.markdown(show_predict_page, unsafe_allow_html=True)    
            #    else:
            #        url = 'https://www.streamlit.io/'
                    #if st.button('Open browser'):
            #        webbrowser.open_new_tab(url)
                
            #st.markdown("<h1 style='text-align: right; color: red;'>Some title</h1>", unsafe_allow_html=True)
            #url = 'https://www.streamlit.io/'
            #if st.button('Open browser'):
            #  webbrowser.open_new_tab(url)

                #if selected=="Get Started":
                #   show_predict_page()
                #elif selected=="Home":
                #   show_explore_page()

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
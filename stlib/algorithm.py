import streamlit as st
import pandas as pd
from time import time
import sys
import numpy as np
#from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')


def select_algorithm(df):
    #with st.container():
    st.write("---")
    st.write("##")

    st.markdown("<h1 style='text-align: center; color: red;'>Linear Regression</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections.</h5>", unsafe_allow_html=True)    

    st.markdown("<h1 style='text-align: center; color: red;'>Decision Tree Regressor</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections.</h5>", unsafe_allow_html=True) 

    st.markdown("<h1 style='text-align: center; color: red;'>Random Forest Regressor</h1>", unsafe_allow_html=True)
        
    st.markdown("<h5 style='text-align: center; color: white;'>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. </h5>", unsafe_allow_html=True) 

    st.markdown("<h1 style='text-align: center; color: red;'>Grid Search CV</h1>", unsafe_allow_html=True)
     
    st.markdown("<h5 style='text-align: center; color: white;'>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage.</h5>", unsafe_allow_html=True) 

    column_1, column_2= st.columns((2, 1))
    with column_1:
       
        st.markdown("<h1 style='text-align: left; color: white;'>Steps</h1>", unsafe_allow_html=True)
        st.write("###")
        st.markdown("<h5 style='text-align: left; color: white;'>1. Upload a file</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: red;'>2. Select an Algorithm</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: white;'>3. Select other parameters</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: white;'>4. Results</h5>", unsafe_allow_html=True)
            #if agree:
                #st.write('Great!')
    with column_2:
            df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
            df = df.rename({"ConvertedComp": "Salary"}, axis=1)
            df = df[df["Salary"].notnull()]
            #st.write(df.head())

            df = df.dropna()
            #st.write(df.isnull().sum())

            df = df[df["Employment"] == "Employed full-time"]
            df = df.drop("Employment", axis=1)
            #st.write(df.info())
            #st.write(df.head())

            #df["Country"].value_counts()
            def shorten_categories(categories, cutoff):
                categorical_map = {}
                for i in range(len(categories)):
                    if categories.values[i] >= cutoff:
                        categorical_map[categories.index[i]] = categories.index[i]
                    else:
                        categorical_map[categories.index[i]] = 'Other'
                return categorical_map

            country_map = shorten_categories(df.Country.value_counts(), 400)
            df['Country'] = df['Country'].map(country_map)
            #st.write(df.Country.value_counts())

            df = df[df["Salary"] <= 250000]
            df = df[df["Salary"] >= 10000]
            df = df[df['Country'] != 'Other']
            #st.write(df["YearsCodePro"].unique())

            def clean_experience(x):
                if x ==  'More than 50 years':
                    return 50
                if x == 'Less than 1 year':
                    return 0.5
                return float(x)

            df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
            #st.write(df["YearsCodePro"].unique())

            def clean_education(x):
                if 'Bachelor’s degree' in x:
                    return 'Bachelor’s degree'
                if 'Master’s degree' in x:
                    return 'Master’s degree'
                if 'Professional degree' in x or 'Other doctoral' in x:
                    return 'Post grad'
                return 'Less than a Bachelors'

            df['EdLevel'] = df['EdLevel'].apply(clean_education)
            #st.write(df["EdLevel"].unique())

            from sklearn.preprocessing import LabelEncoder
            le_education = LabelEncoder()
            df['EdLevel'] = le_education.fit_transform(df['EdLevel'])
            #st.write(df["EdLevel"].unique())

            le_country = LabelEncoder()
            df["Country"] = le_country.fit_transform(df["Country"])
            #st.write(df["Country"].unique())

            X = df.drop("Salary", axis=1)
            y = df["Salary"]
            #st.write(X)

            
            #from sklearn.metrics import mean_squared_error, mean_absolute_error

            #def show_predict_page():
            #st.title("Software Developer Salary Prediction")

            #st.write("""### We need some information to predict the salary""")
            #with st.form("my_form"):
            model = (
                        "Linear Regression",
                        "Decision Tree Regressor",
                        "RandomForest Regressor",
                        "Grid Search CV",
                    )
            st.markdown("<h1 style='text-align: center; color: white;'>Select an Algorithm</h1>", unsafe_allow_html=True)       
            model = st.radio("",model)
            submit = st.button('Select the algorithm')
    if submit:
        if submit is not None:
            from stlib import parameters
            parameters.other_parameters(model,X,y,le_education,le_country)
        else:
            st.subheader("Select an algorithm first.")
    #show_predict_page()
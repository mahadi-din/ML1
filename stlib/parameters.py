import streamlit as st
import numpy as np

def other_parameters(model,X,y,le_education,le_country):
    st.write("---")
    st.write("##")
    column_1, column_2= st.columns((2, 1))
    with column_1:
       
        st.markdown("<h1 style='text-align: left; color: white;'>Steps</h1>", unsafe_allow_html=True)
        st.write("###")
        st.markdown("<h5 style='text-align: left; color: white;'>1. Upload a file</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: white;'>2. Select an Algorithm</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: red;'>3. Select other parameters</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: white;'>4. Results</h5>", unsafe_allow_html=True)
    
    with column_2:
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        countries = (
                            "United States",
                            "India",
                            "United Kingdom",
                            "Germany",
                            "Canada",
                            "Brazil",
                            "France",
                            "Spain",
                            "Australia",
                            "Netherlands",
                            "Poland",
                            "Italy",
                            "Russian Federation",
                            "Sweden",
                        )

        education = (
                            "Less than a Bachelors",
                            "Bachelor’s degree",
                            "Master’s degree",
                            "Post grad",
                        )

        country = st.selectbox("Country", countries)
        education = st.selectbox("Education Level", education)

        expericence = st.slider("Years of Experience", 0, 50, 3)

        submit = st.form_submit_button('Submit')
        if submit:
                            X = np.array([[country, education, expericence ]])
                            X[:, 0] = le_country.transform(X[:,0])
                            X[:, 1] = le_education.transform(X[:,1])
                            X = X.astype(float)
                            #st.write(X)
    from stlib import print
    print.print_result(model, X, X_train, X_test, y_train, y_test)
import streamlit as st
import pandas as pd
from time import time
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
#from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')


def print_result(model, X, X_train, X_test, y_train, y_test):       
        #with st.container():
    st.write("---")
    st.write("##")
    
    if model=="Linear Regression":
        Linear_Regression(X, X_train, X_test, y_train, y_test)
    elif model=="Decision Tree Regressor":
        Decision_Tree_Regressor(X, X_train, X_test, y_train, y_test)
    elif model=="Random Forest Regressor":
        Random_Forest_Regressor(X, X_train, X_test, y_train, y_test)
    else:
        Grid_Search_CV(X, X_train, X_test, y_train, y_test)

def Linear_Regression(X, X_train, X_test, y_train, y_test):
    from sklearn.linear_model import LinearRegression
    linear_reg = LinearRegression(n_jobs=-1)
    start=time()
    linear_reg.fit(X_train,y_train)
    end = time()
    result= end - start
    #st.subheader(f"The estimated time is {result:.5f} seconds")
    linear_reg.score(X_test,y_test)
    y_pred = linear_reg.predict(X_test)
    #accuracy_score(y_test,y_pred)
    #st.write(X)
    #st.write(linear_reg)
    salary = linear_reg.predict(X)
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
    error = np.sqrt(mean_squared_error(y_test, y_pred))
    st.subheader(f"The error is ${error:.2f}")
    R2_LG= r2_score(y_test, y_pred)
    st.subheader(f"The R2 Score is % {R2_LG:.2f}")

def Decision_Tree_Regressor(X, X_train, X_test, y_train, y_test):
    from sklearn.tree import DecisionTreeRegressor
    dec_tree_reg = DecisionTreeRegressor(random_state=0)
    dec_tree_reg.fit(X_train,y_train)
    st.write(dec_tree_reg.score(X_test,y_test))
    y_pred = dec_tree_reg.predict(X_test)
    error = np.sqrt(mean_squared_error(y_test, y_pred))
    salary = dec_tree_reg.predict(X)
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
    error = np.sqrt(mean_squared_error(y_test, y_pred))
    st.subheader(f"The error is ${error:.2f}")
    R2_DTR= r2_score(y_test, y_pred)
    st.subheader(f"The R2 Score is % {R2_DTR:.2f}")

def Random_Forest_Regressor(X, X_train, X_test, y_train, y_test):
    from sklearn.ensemble import RandomForestRegressor
    random_forest_reg = RandomForestRegressor(random_state=0)
    random_forest_reg.fit(X_train,y_train)
    random_forest_reg.score(X_test,y_test)
    y_pred = random_forest_reg.predict(X_test)
    error = np.sqrt(mean_squared_error(y_test, y_pred))
    salary = random_forest_reg.predict(X)
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
    error = np.sqrt(mean_squared_error(y_test, y_pred))
    st.subheader(f"The error is ${error:.2f}")
    R2_RFG= r2_score(y_test, y_pred)
    st.subheader(f"The R2 Score is % {R2_RFG:.2f}")

def Grid_Search_CV(X, X_train, X_test, y_train, y_test):
                    from sklearn.model_selection import GridSearchCV
                    from sklearn.tree import DecisionTreeRegressor
                    max_depth = [None, 2,4,6,8,10,12]
                    parameters = {"max_depth": max_depth}
                    regressor = DecisionTreeRegressor(random_state=0)
                    gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
                    gs.fit(X_train,y_train)
                    gs.score(X_test,y_test)
                    regressor = gs.best_estimator_
                    regressor.fit(X_train,y_train)
                    y_pred = gs.predict(X_test)
                    error = np.sqrt(mean_squared_error(y_test, y_pred))
                    salary = regressor.predict(X)
                    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
                    error = np.sqrt(mean_squared_error(y_test, y_pred))
                    st.subheader(f"The error is ${error:.2f}")
                    R2_GS_CV= r2_score(y_test, y_pred)
                    st.subheader(f"The R2 Score is % {R2_GS_CV:.2f}")
                #st.write(X_test)

    
            


    
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
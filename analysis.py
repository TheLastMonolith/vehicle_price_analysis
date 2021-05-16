import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

favicon = ':car:'
st.set_page_config(page_title='Vehicle Price Analysis', page_icon = favicon, initial_sidebar_state = 'auto')

#-----Start of Set Up-----#

my_page = st.sidebar.radio('Contents',
                            ['Introduction',
                            'Data Information',
                            'Methodology',
                            'Data Cleaning', 
                            'EDA',
                            'Data Preparation',
                            'Modeling and Evaluation',
                            'Conclusions and Recommendations']) # creates sidebar #

st.markdown("""<style>.css-1aumxhk {background-color: #ebeae3;background-image: none;color: #ebeae3}</style>""", unsafe_allow_html=True) # changes background color of sidebar #

#-----End of Set Up-----#

#-----Start of Page 1 (Introduction)-----#

if my_page == 'Introduction':
    st.markdown("<h1 style='text-align: center;'>Price Prediction of Vehicles in</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Alabama, USA</h1>", unsafe_allow_html=True)
    st.image('figures/cars1.png',use_column_width=True)
    st.write("By: Joseph Figuracion")

#-----End of Page 1 (Introduction)-----#

#-----Start of Page 2 (Data Information)-----#
elif my_page == 'Data Information':
    st.title("Data Overview")
    st.write("The dataset is in csv file format that contains information about used cars and its selling price. \
            Explore the data below:")

    HtmlFile = open("data_profile.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height = 500, scrolling=True)
#-----End of Page 2 (Data Information)-----#

#-----Start of Page 3 (Methodology)-----#
elif my_page == 'Methodology':
     st.title("Data Science Process")
     st.image("figures/cars2.png",use_column_width=True)
#-----End of Page 3 (Methodology)-----#

#-----Start of Page 4 (Data Cleaning)-----#
elif my_page == 'Data Cleaning':
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: large;font-weight: bold;">\
                A. Dealing with Outliers (Numeric Values):\
                </div>',unsafe_allow_html=True)
     st.image("figures/cars3.png",use_column_width=True)
     
     st.write("i. Before removing outliers:")
     HtmlFile_1 = open("figures/image02_3Dscatter.html", 'r', encoding='utf-8')
     source_code_1 = HtmlFile_1.read()
     components.html(source_code_1, height=400)
     st.write("Note: One data point of the price is already in billion US dollars!")
     st.write("ii. After removing outliers:")
     HtmlFile_2 = open("figures/image01_3Dscatter.html", 'r', encoding='utf-8')
     source_code_2 = HtmlFile_2.read()
     components.html(source_code_2, height=400)

     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: large;font-weight: bold;">\
                B. Dealing with Null Values (Categorical Values):\
                </div>',unsafe_allow_html=True)
     st.image("figures/cars4.png",use_column_width=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;font-weight: bold;">\
                1. Drop observations with null values <5%\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;">\
                We drop rows of features with less than 5% missing data.\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;font-weight: bold;">\
                2. Drop whole feature with null values > 50%\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;">\
                If a feature has too many missing values, this becomes less relevant.\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;font-weight: bold;">\
                3. Impute `condition` values using `odometer` values\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;">\
                We can assume that the better condition the car is,  the better the mileage reading of the odometer (i.e. lower mileage).\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;font-weight: bold;">\
                4. Impute using series of common values\
                </div>',unsafe_allow_html=True)
     st.markdown('<div style="text-align: left;color: #2A2C25; font-size: medium;">\
               We propagate last valid observation forward next to a valid.\
                </div>',unsafe_allow_html=True)
#-----End of Page 4 (Data Cleaning)-----#

#-----Start of Page 5 (EDA)-----#
elif my_page == 'EDA':
     st.title("Exploratory Data Analysis")
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     # Item 1
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                Which car manufacturers are commonly listed?\
                </div>',unsafe_allow_html=True)
     st.image("figures/cars5.png",use_column_width=True)
     # Item 2
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                Which car manufacturers are the most expensive?\
                </div>',unsafe_allow_html=True)
     st.image("figures/cars6.png",use_column_width=True)
     # Item 3
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                Where can we find them?\
                </div>',unsafe_allow_html=True)
     HtmlFile_1 = open("figures/mapping.html", 'r', encoding='utf-8')
     source_code_1 = HtmlFile_1.read()
     components.html(source_code_1, height=400)
     # Item 4
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                How are cars priced based on it’s mileage?\
                </div>',unsafe_allow_html=True)
     HtmlFile_2 = open("figures/image03_price_odometer.html", 'r', encoding='utf-8')
     source_code_2 = HtmlFile_2.read()
     components.html(source_code_2, height=500)
    # Item 5
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                How are cars priced based on paint color?\
                </div>',unsafe_allow_html=True)
     HtmlFile_3 = open("figures/image04_2Dcolor_price.html", 'r', encoding='utf-8')
     source_code_3 = HtmlFile_3.read()
     components.html(source_code_3, height=500)
     # Item 6
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown('<div style="text-align: left;color: #283044; font-size: medium;font-weight: bold;">\
                How are the car’s price affected by its age?\
                </div>',unsafe_allow_html=True)
     HtmlFile_4 = open("figures/image05_age_price.html", 'r', encoding='utf-8')
     source_code_4 = HtmlFile_4.read()
     components.html(source_code_4, height=500)
#-----End of Page 5 (EDA)-----#

#-----Start of Page 6 (Data Preparation)-----#
elif my_page == 'Data Preparation':
     st.title("Data Preparation")
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.image("figures/cars7.png",use_column_width=True)
    
#-----End of Page 6 (Data Preparation)-----#

#-----Start of Page 7 (Model Results and Evaluation)-----#
elif my_page == 'Modeling and Evaluation':
     st.title("Regression Analysis Model Results:")
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     
     st.markdown("""
     | Model                   	| RMSE    	| MAE     	| R2     	|
     |-------------------------	|---------	|---------	|--------	|
     | Linear Regression       	| 7292.79 	| 5570.81 	| 0.5962 	|
     | Random Forest Regressor 	| 5304.98 	| 3601.55 	| 0.7863 	|
     | LightGBM Regressor      	| 4868.76 	| 3053.18 	| 0.8201 	|
     | XGBoost Regressor       	| 4781.12 	| 2988.45 	| 0.8264 	|
     """)
     st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
     st.markdown(':bulb:  Boosting algorithms generalizes well with our data.')
     st.markdown(':bulb:  Most important features are odometer, manufacturer, model, and age.')
#-----End of Page 6 (Model Results and Evaluation)-----#
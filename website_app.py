import streamlit as st
#from streamlit_option_menu import option_menu
from streamlit_option_menu import option_menu
#import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
#import streamlit.components.v1 as components
import base64
from streamlit_text_rating.st_text_rater import st_text_rater

# -------------- SETTINGS --------------
page_title = "Welcome To Elhadji Ngom's Personal Webpage"
page_icon = ":earth_africa:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
cv_name = 'CV-Elhadji-Ngom.pdf'
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.markdown(f"<h1 style='text-align: center; color: #000080;'>{page_title}</h1>",
            unsafe_allow_html=True)

def _max_width_():
    max_width_str = f"max-width: 1450px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )
_max_width_()

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#----------- Embed PDF in Streamlit --------
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



with st.sidebar:
    choose = option_menu("Main Menu", ["About", "Projects", "Apps", "Contact"],
                         icons=['house', 'bar-chart-line','app-indicator','person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    )

logo = Image.open(r'./data_science.png')
profile = Image.open(r'./my_in_profile.png')
if choose == "About":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
        job_title = "Data scientist | NLP | Python Engineer"
        st.markdown(f"<h2 class='font'>{job_title}</h2>", unsafe_allow_html=True)
    with col2:               # To display brand log
        st.image(logo, width=130)


    st.markdown(f"<h2 style='text-align: center; font-style: italic;'>About the creator :</h2>",
                unsafe_allow_html=True)
    description = "Elhadji is a data science practitioner, enthusiast, and Python Engineer. He run data science projects with Python or R to deal with NLP applications aand/or Object Detection problems. He works on data visualization, builds Streamlit app, etc. He is also a football amateur who loves pop music.\n\n"
    st.markdown(""" <style> .font_par {
    font-size:20px ; font-family: 'Black'; color: #FFFFF; font-style: oblique;}
    </style> """, unsafe_allow_html=True)
    st.markdown(f'<p class="font_par">{description}</p>',
                unsafe_allow_html=True)

    #------- display my cv -------------
    with st.expander("ℹ️  View & Download Elhadji's CV", expanded=False):
        try:
            show_pdf(f'./{cv_name}')
        except:
            st.warning('File type should pdf !!!')


    st.header('')
    linkedin_p = 'To read more about her profile on the social media.'
    st.markdown(f'<p class="font_par">{linkedin_p}</p>',unsafe_allow_html=True)
    st.image(profile, width=700)
    st.info("Please visit her Linkedin page at :link:: https://www.linkedin.com/in/elhadji-ngom-data-ai")
    st.info("Please visit her Apec page at :link:: https://www.apec.fr/candidat/mon-espace.html#/")
    st.info("Please visit her github page at :link:: https://github.com/engom")
    st.info("Please visit the github of this page at :link:: https://github.com/engom/my_Webpage")











elif choose == "Blog":
        topic = option_menu(None, ["Streamlit", "Pandas", "Plotly", "Folium"],
                         icons=['book', 'book','book','book'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#080000"},
        },orientation='horizontal'
        )

        st.write('')
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        if topic=='Pandas':
            feature_image1 = Image.open(r'C:\Users\13525\Desktop\Insights Bees\streamlit_website\Images\feature_image1.jpg')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image1,caption='Image by Pixabay')
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Clean a ‘Numeric’ ID Column in Pandas Dataframe</p>', unsafe_allow_html=True)
                    st.markdown("By Sharone Li - As a data scientist, you must have encountered this problem at least once in your data science journey: you import your data into a Pandas dataframe... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")

            col1, col2,col3= st.columns(3)
            with col1:
                if st.button('Read PDF Tutorial',key='1'):
                    show_pdf('post1-compressed.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='2')
            with col3:
                with open("post1-compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download PDF Tutorial", key='3',
                        data=PDFbyte,
                        file_name="pandas-clean-id-column.pdf",
                        mime='application/octet-stream')

            for text in ["Is this tutorial helpful?"]:
                    response = st_text_rater(text=text, key='1')

            st.write('---')
            feature_image2 = Image.open(r'C:\Users\13525\Desktop\Insights Bees\streamlit_website\Images\feature_image3.png')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image2,caption='Image by Pixabay')

                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;}
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">How to Batch Rename Columns in Pandas Based on Patterns</p>', unsafe_allow_html=True)
                    st.markdown("By Sharone Li - If you have been following my Medium blog for some time, you may notice that I usually like to share... [Continue to Read on CodeX](https://medium.com/codex/how-to-batch-rename-columns-in-pandas-based-on-patterns-7d2382b5fc9a)")

            col1, col2,col3 = st.columns(3)
            with col1:
                #st.button('Read PDF Tutorial', key='1')

                if st.button('Read PDF Tutorial',key='7'):
                  show_pdf('post3.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='8')
            with col3:
                with open("post3.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(label="Download PDF Tutorial",key='9',
                        data=PDFbyte,
                        file_name="pandas-rename-columns.pdf",
                        mime='application/octet-stream')
            for text in ["Is this tutorial helpful?"]:
                    response = st_text_rater(text=text, key='2')

            st.write('---')
            feature_image3 = Image.open(r'C:\Users\13525\Desktop\Insights Bees\streamlit_website\Images\feature_image2.png')
            with st.container():
                image_col, text_col = st.columns((1,3))
                with image_col:
                    st.image(feature_image3,caption='Image by Pixabay')

                with text_col:
                    st.markdown('<p class="font">Why and How to Reshape a Pandas Dataframe from Wide to Long</p>', unsafe_allow_html=True)
                    st.markdown("By Sharone Li - As data scientists, we know that data does not always come to us with the most desirable format... [Continue to Read on Towards Data Science](https://towardsdatascience.com/clean-a-numeric-id-column-in-pandas-dataframe-fbe03c11e330)")

            col1, col2,col3 = st.columns(3)
            with col1:
                if st.button('Read PDF Tutorial',key='4'):
                    show_pdf('post1-compressed.pdf')
            with col2:
                st.button('Close PDF Tutorial',key='5')
            with col3:
                with open("post1-compressed.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()

                st.download_button(label="Download PDF Tutorial",key='6',
                        data=PDFbyte,
                        file_name="pandas-reshape-dataframe.pdf",
                        mime='application/octet-stream')
            for text in ["Is this tutorial helpful?"]:
                response = st_text_rater(text=text, key='3')

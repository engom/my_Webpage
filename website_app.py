import streamlit as st
from pathlib import Path
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
page_title = "Elhadji Ngom's Webpage\n\n Welcome "
page_icon = ":earth_africa:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
cv_name = 'CV-Elhadji-Ngom.pdf'
layout = "wide" # "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.markdown(f"<h1 style='text-align: center; color: #7D3C98;'>{page_title}</h1>",
            unsafe_allow_html=True) # #000080
st.write('---')

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
            /* #MainMenu {visibility: hidden;} */
            footer {visibility: hidden;}
            /* header {visibility: hidden;} */
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#----------- Embed PDF in Streamlit --------
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# ---------- Load markdown file ------------
@st.cache(allow_output_mutation=True)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# ----------- IMAGE LOADER -----------------
@st.cache(allow_output_mutation=True)
def load_image(image_file):
	img = Image.open(image_file)
	return img


# -------- MENU SIDE BAR ----------
with st.sidebar:
    choose = option_menu("Main Menu", ["About", "Projects", "Contact"],
                         icons=['house', 'bar-chart-line','person lines fill'],
                         menu_icon="list", default_index=0, #,"Apps" ,'app-indicator'
                         styles={
        "container": {"padding": "5!important", "background-color": "#566573"}, # "#fafafa"
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    )

logo = load_image(r'./data_science.png')
profile = load_image(r'./my_in_profile.png')
if choose == "About":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
        job_title = "Data scientist | Python Engineer"
        st.markdown(f"<h2 class='font'>{job_title}</h2>", unsafe_allow_html=True)
    with col2:               # To display brand log
        st.image(logo, width=130)

    # --------- ABOUT ME ------------------
    st.markdown(f"<h2 style='text-align: center; font-style: italic;'>About the creator :</h2>",
                unsafe_allow_html=True)
    description = "Elhadji is a data science practitioner, enthusiast, and Python Engineer. He run data science projects with Python or R to deal with NLP applications aand/or Object Detection problems. He works on data visualization, builds Streamlit app, etc. He is also a football amateur who loves pop music.\n\n"
    st.markdown(""" <style> .font_par {
    font-size:20px ; font-family: 'Black'; color: #FFFFF; font-style: oblique;}
    </style> """, unsafe_allow_html=True)
    st.markdown(f'<p class="font_par">{description}</p>',
                unsafe_allow_html=True)

    #------- DISPLAY MY CV  ----------------
    with st.expander("ℹ️  DISPLAY Elhadji's CV", expanded=False):
        try:
            show_pdf(f'./{cv_name}')
        except:
            st.warning('File type should pdf !!!')

    # ------ CV DOWNLOAD BUTTON ------------
    col1, col2, col3= st.columns(3)

    with col2:
        with open(f'./{cv_name}', "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download CV/Resume", key='1',
                data=PDFbyte,
                file_name="CV-Elhadji-Ngom.pdf",
                mime='application/octet-stream')

    # -------- SOCIAL MEDIA LINKS ----------
    st.header('')
    linkedin_p = 'To read more about her profile on the social media.'
    st.markdown(f'<p class="font_par">{linkedin_p}</p>',unsafe_allow_html=True)
    st.image(profile, width=800)
    st.info("Please visit her Linkedin page at :link:: https://www.linkedin.com/in/elhadji-ngom-data-ai")
    st.info("Please visit her Apec page at :link:: https://www.apec.fr/candidat/mon-espace.html#/")
    st.info("Please visit her github page at :link:: https://github.com/engom")


elif choose == "Projects":
    topic = option_menu(None, ["Konvo", "Web Scraping", "Text Summary"],
                     icons=['gear', 'cloud-arrow-down','journal-text','display'],
                     menu_icon="list", default_index=0,
                     styles={
    "container": {"padding": "5!important", "background-color": "#95A5A6"}, # "#fafafa"
    "icon": {"color": "orange", "font-size": "20px"},
    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "#566573"}, # "#080000"  #586e75
    },orientation='horizontal'
    )

    st.write('')
    if topic=='Konvo':
        feature_image1 = load_image(r'./konvo_app.jpg')
        st.markdown(f"<h4 style='text-align: left; font-style: italic;'>Konvoo Project 2022</h4>",
                    unsafe_allow_html=True)
        with st.container():
            image_col, text_col = st.columns((2,3))
            with image_col:
                st.image(feature_image1,
                         width = 200,
                         caption='Image by Elhadji')
            with text_col:
                st.markdown(""" <style> .font {
                font-size:18px ; font-family: 'Black'; color: #FFFFF;}
                </style> """, unsafe_allow_html=True)
                text = """
                The ETP (Patient Therapeutic Education) aims to help patients acquire or maintain the skills they need to best manage their lives with a chronic disease.
                It takes the form of a personalized appointment between a pharmacist and its patient in the pharmacy.
                The pharmacist has an important role to play in this area, as he is the easiest health professional accessible for any patient.
                """
                st.markdown(f'<p class="font">{text}</p>', unsafe_allow_html=True)
                st.markdown("By Konvoo Team - Sentiments and Emotions Inference.\n [Continue to Read The Presentation here ...](https://docs.google.com/presentation/d/1kzYbUGTWuDo46uSu7_PCcvOsqwIbHhlGuMPR9fAgGi4/edit?usp=sharing)")

        col1, col2,col3= st.columns(3)

        with col1:
            if st.button('Read the presentation',key='2'):
                show_pdf('./KONVO_PROJECT.pdf')

        with col2:
            st.button('Close the presentation',key='3')

        with col3:
            with open("./KONVO_PROJECT.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Download the presentation", key='4',
                    data=PDFbyte,
                    file_name="konvo-presentation.pdf",
                    mime='application/octet-stream')

        c1, ce, c2 = st.columns(3)
        with ce:
            feature_image2 = load_image(r'.//Camembert.png')
            st.image(feature_image2,
                     width = 200)


        for text in ["How do you find this presentation ?"]:
            response = st_text_rater(text=text, key='5')


        st.markdown('---')
        readme = read_markdown_file(r"./README.md")
        st.markdown(readme, unsafe_allow_html=True)



    elif topic == "Web Scraping":
        st.info('TO FILL: Konvoo Web Scraping: doctissimo.fr')

        st.info('TO FILL: World bank data scraping')



    elif topic == "Text Summary":
        st.write('TO DO !')



#elif choose == "Apps":
    # ------- TO DO -----
#    st.write('TO DO !')



elif choose == "Contact":
    # ------ TO DO -------
    st.success("Elhadji's mailbox :")
    st.write(":arrow_lower_right: Please, let's get in touch : :love_letter: ngomel.ehn@gmail.com :love_letter:")
    st.markdown('<a href="ngomel.ehn@gmail.com"> Contact me ! </a>', unsafe_allow_html=True)
    st.write('---')

    st.info("The github repo dedicated to this page :")
    st.write("Please click on :link:: https://github.com/engom/my_Webpage")

    st.write('---')
    thank_you = "Thank you for your time !!!"
    st.markdown(f"<h3 style='text-align: center; color: #7D3C98 ;'>{thank_you}</h3>",
                unsafe_allow_html=True)

    st.markdown('---')
    for text in ["How do you find this page ?"]:
        response = st_text_rater(text=text, key='5')

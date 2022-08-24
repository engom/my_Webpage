#!/usr/bin/python

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_text_rating.st_text_rater import st_text_rater

from pathlib import Path
from  PIL import Image
import numpy as np
import pandas as pd
import base64

################################################################

# -------------- SETTINGS --------------
page_title = "Elhadji Ngom's Webpage \n\n 📍 WELCOME 📍"
page_icon = ":earth_africa:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "wide" # "centered"

# --------------------------------------
cv_name = 'CV-Elhadji-Ngom.pdf'
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.markdown(f"<h1 style='text-align: center; color: #7D3C98;'>{page_title}</h1>",
            unsafe_allow_html=True) # #000080
#st.write('---')

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
            #MainMenu {
                visibility: hidden;
                }
            footer {
                visibility: hidden;
                }
            footer:after {
                visibility: visible;
                content: 'Copyright @2022: Ngom | Streamlit';
                postion: relative;
                diplay: block;
                color: tomato;
                }
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
#@st.cache(allow_output_mutation=True)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# ----------- IMAGE LOADER -----------------
#@st.cache(allow_output_mutation=True)
def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():
    # -------- MENU SIDE BAR ----------
    with st.sidebar:
        choose = option_menu("Main Menu", ["About", "Projects", "Apps", "Contact"],
                             icons=['house', 'bar-chart-line', 'app-indicator', 'person lines fill'],
                             menu_icon="list", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"}, # "#fafafa"
            "icon": {"color": "blue", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#24A608"},
        }
        )

    logo = load_image(r'./images/data_science.png')
    profile = load_image(r"./images/my_in_profile.png")
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
        st.write('---')

        # --------- ABOUT ME ------------------
        st.markdown(f"<h2 style='text-align: center; font-style: italic;'>About the creator :</h2>",
                    unsafe_allow_html=True)
        description = "Elhadji is a Data science practitioner, NLP enthusiast, and Python Engineer. He run data science projects with Python or R to deal with NLP applications and/or Object Detection problems. He works on data visualization, builds Streamlit app, etc. He is also a football amateur who likes pop music.\n\n"
        st.markdown(""" <style> .font_par {
        font-size:24px ; font-family: 'Black'; color: #FFFFF; font-style: oblique;}
        </style> """, unsafe_allow_html=True)
        st.markdown(f'<p class="font_par">{description}</p>',
                    unsafe_allow_html=True)

        #------- DISPLAY MY CV  ----------------
        with st.expander("ℹ️  Read Elhadji's CV", expanded=False):
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
        topic = option_menu(None, ["Overview", "Konvoo", "Web Scraping", "Text Summary"],
                         icons=['gear-fill', 'gear', 'cloud-arrow-down', 'display'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#95A5A6"}, # "#fafafa"
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#566573"}, # "#080000"  #586e75
        },orientation='horizontal'
        )

        st.write('')
        if topic=='Konvoo':
            feature_image1 = load_image(r'./images/konvo_app.jpg')
            feature_image2 = load_image(r'./images/Camembert.png')
            st.markdown(f"<h4 style='text-align: left; font-style: italic;'>Konvoo Project 2022</h4>",
                        unsafe_allow_html=True)
            with st.container():
                image_col, text_col = st.columns((2,3))
                with image_col:
                    st.image(feature_image1,
                             width = 200,
                             caption='Architecture - By Elhadji')

                    st.image(feature_image2,
                             width = 200)
                with text_col:
                    st.markdown(""" <style> .font {
                    font-size:24px ; font-family: 'Black'; color: #FFFFF;}
                    </style> """, unsafe_allow_html=True)
                    text = read_markdown_file(r'./konvo_descrip.md')
                    st.markdown(f'<p class="font">{text}</p>', unsafe_allow_html=True)
                    st.markdown("By Konvoo Team - **Sentiments and Emotions Prediction**.\n\n [Continue to Read The Konvoo here ...](https://docs.google.com/presentation/d/1kzYbUGTWuDo46uSu7_PCcvOsqwIbHhlGuMPR9fAgGi4/edit?usp=sharing)")

            col1, col2,col3= st.columns([3, 3, 1])

            with col1:
                if st.button('Read the presentation',key='2'):
                    show_pdf(r'./KONVO_PROJECT.pdf')

            with col2:
                st.button('Close the presentation',key='3')

            with col3:
                with open(r"./KONVO_PROJECT.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label="Download", key='4',
                        data=PDFbyte,
                        file_name="konvo-presentation.pdf",
                        mime='application/octet-stream')


            for text in ["How do you find this presentation ?"]:
                response = st_text_rater(text=text, key='5')


        elif topic == "Overview":
            # st.markdown('---')
            with st.container():
                left, ce, right = st.columns([0.6, 0.05, 0.35])
                with left:
                    readme = read_markdown_file(r"./README.md")
                    st.markdown(f'<p class="font">{readme}</p>',
                                unsafe_allow_html=True)

                with right:
                    st.text('RROGRAMMING')
                    python = load_image(r'./images/python-logo.jpg')
                    st.image(python, width=130)
                    st.text('')

                    Rlogo = load_image(r'./images/Rlogo.png')
                    st.image(Rlogo, width=100)
                    st.write('---')

                    st.text('DATABASE')
                    sql_logo = load_image(r'./images/sql_logo.png')
                    st.image(sql_logo, width=140, caption='SQL')
                    st.text('')

                    mysql_logo = load_image(r'./images/mysql-logo.png')
                    st.image(mysql_logo, width=140, caption='SQL')
                    st.text('')

                    Neo4j_logo = load_image(r'./images/Neo4j-logo_color.png')
                    st.image(Neo4j_logo, width=140, caption='NoSQL')
                    st.write('---')

                    st.text('CLOUD - DOCKER')
                    aws_logo = load_image(r'./images/aws_logo.png')
                    st.image(aws_logo, width=130, caption="Cloud Computing")
                    st.text('')

                    docker_logo = load_image(r'./images/docker-logo.png')
                    st.image(docker_logo, width=150, caption="Virtualization")
                    st.write('')

                    kuber_logo = load_image(r'./images/kubernetes-logo.png')
                    st.image(kuber_logo,
                             width=160,
                             caption="Container Orchestration")
                    st.write('---')

                    st.text('DL FRAMEWORKS')
                    TensorFlow_logo = load_image(r'./images/TensorFlowLogo.png')
                    st.image(TensorFlow_logo, width=130)
                    st.text('')

                    keras_logo = load_image(r'./images/keras-python.png')
                    st.image(keras_logo, width=150)
                    st.text('')

                    PyTorch_logo = load_image(r'./images/PyTorch_logo.png')
                    st.image(PyTorch_logo, width=150)
                    st.write('---')

                    st.text('ML FRAMEWORKS')
                    MLflow_logo = load_image(r'./images/MLFlow-logo.png')
                    st.image(MLflow_logo, width=150)
                    st.text('')

                    st_logo = load_image(r'./images/streamlit-logo.png')
                    st.image(st_logo, width=160)
                    st.text('')

                    github_logo = load_image(r'./images/github-logo.png')
                    st.image(github_logo, width=150)
                    st.text('')

                    dvc_logo = load_image(r'./images/dvc_logo.png')
                    st.image(dvc_logo, width=150)
                    st.text('')

                    lab_logo = load_image(r'./images/lab_logo.png')
                    st.image(lab_logo, width=150)
                    st.text('')




        elif topic == "Web Scraping":
            proj_img = load_image(r'./images/Web-Scraping.png')
            st.image(proj_img, width=800)
            st.info('Update is coming soon !!')



        elif topic == "Text Summary":
            proj_schema = load_image(r'./images/summarier_pipeline.jpg')
            st.image(proj_schema,
                     width=800,
                     caption='Text Summarizer Pipeline (spaCy + BART) - By Elhadji')

            st.info('Update is coming soon !!')



    elif choose == "Apps":
        # ------- TO DO -----
        # Create and share beautiful images of your source code
        # >>> https://carbon.now.sh/
        st.markdown("""<h3 style='text-align: center; font-style: italic;'>
                    Apps deployed
                    </h3>""",
                    unsafe_allow_html=True)


        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Text Summarizer app: source code header
                    </h5>""",
                    unsafe_allow_html=True)
        with st.container():
            app_img = load_image(r'images/summary_app.png')
            st.image(app_img,
                     width=800,
                     caption="By Elhadji")

        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Profile Webpage: source code header
                    </h5>""",
                    unsafe_allow_html=True)
        with st.container():
            app_img = load_image(r'images/carbon.png')
            st.image(app_img,
                     width=800,
                     caption="By Elhadji")

        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Web Scraping app: source code header
                    </h5>""",
                    unsafe_allow_html=True)
        with st.container():
            app_img = load_image(r'images/scraper_app.png')
            st.image(app_img,
                     width=800,
                     caption="By Elhadji")


    elif choose == "Contact":
        # ------ TO DO -------
        st.success("ELHADJI'S MAILBOX :")
        c1, ce, c2 = st.columns([4, 4, 3])
        with c1:
            st.write(":arrow_lower_right: Please, let's get in touch :")
            st.write("ngomel.ehn@gmail.com ✉️")
        with c2:
            st.markdown('<a href="ngomel.ehn@gmail.com">✉️ Contact me ! ✉️ </a>', unsafe_allow_html=True)
        st.write('---')

        #st.info("The github repo dedicated to this page :")
        #st.write("Please click on :link:: https://github.com/engom/my_Webpage")

        #st.write('---')
        thank_you = "Thank you for your time !!!"
        st.markdown(f"<h3 style='text-align: center; color: #7D3C98 ;'>{thank_you}</h3>",
                    unsafe_allow_html=True)

        st.markdown('---')
        for text in ["How do you find this page ?"]:
            response = st_text_rater(text=text, key='5')

if __name__ == '__main__':
    main()

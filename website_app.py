#!/usr/bin/python

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_text_rating.st_text_rater import st_text_rater
import streamlit.components.v1 as components

from pathlib import Path
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import io
import qrcode

# -------------- SETTINGS --------------
page_title = "Elhadji Ngom's Webpage \n\n 📍 WELCOME 📍"
page_icon = ":earth_africa:"
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "wide" # "centered"

# --------------------------------------
cv_name = 'CV-Elhadji-Ngom.pdf'
# --------------------------------------
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

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

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 2.5rem;
                    padding-left: 2.5rem;
                    padding-right: 2.5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown(f"<h1 style='text-align: center; color: #F39C12;'>{page_title}</h1>",
            unsafe_allow_html=True) # #000080


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
                content: 'Copyright: Ngom | Streamlit 2022';
                postion: relative;
                diplay: block;
                --color: tomato;
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

# ------------ APP BACKGROUND --------------
@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# badge linkedin
embed_component = {'linkedin':"""
<script src="https://platform.linkedin.com/badges/js/profile.js"
 async defer type="text/javascript">
</script>
<div class="badge-base LI-profile-badge" data-locale="fr_FR"
 data-size="large" data-theme="light" data-type="HORIZONTAL"
 data-vanity="elhadji-ngom-data-ai" data-version="v1">
 <a class="badge-base__link LI-simple-link"
 href="https://fr.linkedin.com/in/elhadji-ngom-data-ai?trk=profile-badge">
 </a></div>
""",
'github':"""
<a href="https://github.com/engom"><img
src="https://img.shields.io/static/v1?label=ENGOM&message=GitHub+profile&color=
2ea44f&style=for-the-badge&logo=%23FC6D26" alt="engom - Visit GitHub profile">
</a>
"""}



################## MAIN #####################
def main():
    # -------- MENU SIDE BAR ----------
    with st.sidebar:
        choose = option_menu("Page Menu", ["About", "Projects", "Apps", "Contact"],
                             icons=['house', 'bar-chart-line', 'app-indicator', 'person lines fill'],
                             menu_icon="list", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#1c1c1e"}, # "#fafafa"
            "icon": {"color": "blue", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#24A608"},
        }
        )


    logo = load_image(r'./images/el_00.png')
    #ds_img = load_image(r'./images/data_science.png')
    if choose == "About":
        col1, col2 = st.columns([0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #F39C12;}
            </style> """, unsafe_allow_html=True)
            job_title = "Data scientist | ML Engineer | NLP"
            st.markdown(f"<h2 class='font'>{job_title}</h2>", unsafe_allow_html=True)
        with col2:               # To display brand log
            st.image(logo, width=130)

        #with st.sidebar:
            #st.markdown(embed_component['github'], unsafe_allow_html=True)
        st.write('---')

        # --------- ABOUT ME ------------------
        st.markdown(f"""<h2 style='text-align: center; font-style: normal;'>
                    About the creator :</h2>""",
                    unsafe_allow_html=True)
        description = """
        Elhadji is a junior data scientist, NLP enthusiast and machine learning engineer.
        He runs data science projects with Python, R or SQL to handle NLP applications and
        computer vision subjects. He also works on data visualization with Python (matplotlib,
        seaborn, plotly), and builds beautiful custom front-end web applications with Streamlit
        to make predictions. Elhadji is an amateur footballer with a passion for pop music.
        """
        st.markdown(""" <style> .font_par {
        font-size:21px ; font-family: 'Black'; color: #FFFFF; font-style: normal;}
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
        st.write("---")
        # -------- SOCIAL MEDIA LINKS ----------
        with st.container():
            linkedin_p = "Read more about Elhadji's profile on Linkedin and GitHub."
            st.markdown(f"""<h3 style='text-align: center; font-style: italic;'>
                    {linkedin_p}
                    </h3>""",
                        unsafe_allow_html=True)
            #st.markdown(f'<p class="font_par">{linkedin_p}</p>',unsafe_allow_html=True)
            with st.container():
                col1, ce, col2 = st.columns([0.4, 0.2, 0.4])
                with col1:
                    components.html(embed_component['linkedin'], height=350)

                with col2:
                    url = "https://www.linkedin.com/in/elhadji-ngom-data-ai"
                    linkedin = f'''<a href="{url}">
                                LINKEDIN
                                </a>'''
                    #st.markdown(linkedin, unsafe_allow_html=True)
                    img = qrcode.make(url)
                    virtualfile = io.BytesIO()
                    img.save(virtualfile)
                    st.image(virtualfile,
                            width=260,
                            caption="Please visit his Linkedin: scan me !")


                with col1:
                    url = "https://github.com/engom"
                    github = f'''<a href="{url}">
                                Visit GitHub
                                </a>'''
                    img = qrcode.make(url)
                    virtualfile = io.BytesIO()
                    img.save(virtualfile)
                    st.image(virtualfile,
                             width=270,
                             caption="Please visit his github: scan me !")


                with col2:
                    url = "https://www.apec.fr/candidat/mon-espace.html#/"
                    st.header(" ")
                    st.header(" ")
                    img = qrcode.make(url)
                    virtualfile = io.BytesIO()
                    img.save(virtualfile)
                    st.image(virtualfile,
                             width=260,
                             caption="Please visit his Apec page: scan me!")

                c0, ce, c1 = st.columns([0.35, 0.35, 0.3])
                with ce:
                    #st.markdown(github, unsafe_allow_html=True)
                    st.markdown(embed_component['github'], unsafe_allow_html=True)
                st.write('---')

    elif choose == "Projects":
        topic = option_menu(None, ["Overview", "Konvoo-ETP", "Text Summary", "Web Scraping"],
                         icons=['gear-fill', 'gear', 'display', 'cloud-arrow-down'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#95A5A6"}, # "#fafafa"
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#566573"}, # "#080000"  #586e75
        },orientation='horizontal'
        )
        # add linkedin on sidebar
        with st.sidebar:
            components.html(embed_component['linkedin'],height=300)

        st.write('')
        if topic=='Konvoo-ETP':
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
                    st.text('RROGRAMMING TOOLS')
                    python = load_image(r'./images/Python_logo.png')
                    st.image(python, width=160, caption='Open source')
                    st.text('')

                    Rlogo = load_image(r'./images/Rlogo.png')
                    st.image(Rlogo, width=130, caption='Open source')
                    st.text('')

                    SAS_logo = load_image(r'./images/SAS_logo.png')
                    st.image(SAS_logo, width=150, caption='Under license')
                    st.write('---')

                    st.text('DATABASE SERVICES')
                    sql_logo = load_image(r'./images/sql_logo.png')
                    st.image(sql_logo, width=150, caption='SQL')
                    st.text('')

                    mysql_logo = load_image(r'./images/mysql-logo.png')
                    st.image(mysql_logo, width=150, caption='SQL')
                    st.text('')

                    Neo4j_logo = load_image(r'./images/Neo4j-logo_color.png')
                    st.image(Neo4j_logo, width=150, caption='NoSQL')
                    st.write('---')

                    st.text('CLOUD SERVICES & DOCKER')
                    aws_logo = load_image(r'./images/aws_logo.png')
                    st.image(aws_logo, width=160, caption="Cloud Computing")
                    st.text('')

                    docker_logo = load_image(r'./images/docker-logo.png')
                    st.image(docker_logo, width=160, caption="Virtualization")
                    st.write('')

                    kuber_logo = load_image(r'./images/kubernetes-logo.png')
                    st.image(kuber_logo,
                             width=160,
                             caption="Container Orchestration")
                    st.write('---')

                    st.text('DEEP LEARNING FRAMEWORKS')
                    TensorFlow_logo = load_image(r'./images/TensorFlowLogo.png')
                    st.image(TensorFlow_logo, width=130)
                    st.text('')

                    keras_logo = load_image(r'./images/keras-python.png')
                    st.image(keras_logo, width=150)
                    st.text('')

                    PyTorch_logo = load_image(r'./images/PyTorch_logo.png')
                    st.image(PyTorch_logo, width=150)
                    st.write('---')

                    st.text('MACHINE LEARNING FRAMEWORKS')
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

        elif topic == "Text Summary":
            proj_schema = load_image(r'./images/summarier_pipeline.jpg')
            with st.container():
                col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
                with col2:
                    st.image(proj_schema,
                             width=750,
                             caption='Text Summarizer Pipeline (spaCy + BART) - By Elhadji')

            st.success('Text Summarization')
            description1 = """
            Summarization is the task of producing a shorter version of a document while preserving its important information.
            Some models can extract text from the original input (extractive summary), while other models can generate entirely new text (abstractive summary).
            Some parts of this summary may not even appear in the original text. We combined these two methodologies into one single summarizer pipeline.
            """
            description2 = """
            Hence we used spaCy pipeline in the pre-processing step to extract the most import part the orginal text.
            The pre-processed output goes to the transformers based model that has attention mechanism.
            The attention mechanism uses a weighted sum of all of the encoder hidden states to flexibly
            focus the attention of the decoder to the most relevant parts of the input sequence.
            Thus, we got a final to human-like summary.
            """
            st.markdown(""" <style> .font {
            font-size:20px ; font-family: 'Black'; color: #FFFFF;}
            </style> """, unsafe_allow_html=True)
            st.markdown(f'<p class="font">{description1}</p>',
                        unsafe_allow_html=True)
            st.markdown(f'<p class="font">{description2}</p>',
                        unsafe_allow_html=True)
            st.info('Tools: spaCy - Transformers | BERT | BARThez - Pytorch - Colab - Jupyterlab - Atom - GitHub')

        elif topic == "Web Scraping":
            with st.container():
                col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
                with col2:
                    proj_img = load_image(r'./images/Web-Scraping.png')
                    st.image(proj_img, width=750)
            # st.info('Update is coming soon !!')


    elif choose == "Apps":
        # ------- TO DO -----
        # Create and share beautiful images of your source code
        # >>> https://carbon.now.sh/
        # add linkedin on sidebar
        with st.sidebar:
            components.html(embed_component['linkedin'],height=300)

        st.markdown("""<h3 style='text-align: center; font-style: italic;'>
                    Apps deployed
                    </h3>""",
                    unsafe_allow_html=True)


        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Text Summarizer app: source code header
                    </h5>""",
                    unsafe_allow_html=True)

        with st.container():
            col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
            with col2:
                app_img = load_image(r'images/summary_app.png')
                st.image(app_img,
                         width=750,
                         caption="Image By Elhadji")

        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Profile Webpage: source code header
                    </h5>""",
                    unsafe_allow_html=True)

        with st.container():
            col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
            with col2:
                app_img = load_image(r'images/carbon.png')
                st.image(app_img,
                         width=750,
                         caption="Image By Elhadji")

        st.markdown("""<h5 style='text-align: center; font-style: italic;'>
                    Web Scraping app: source code header
                    </h5>""",
                    unsafe_allow_html=True)

        with st.container():
            col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
            with col2:
                app_img = load_image(r'images/scraper_app.png')
                st.image(app_img,
                         width=750,
                         caption="Image By Elhadji")


    elif choose == "Contact":
        # ------ TO DO -------
        # add linkedin on sidebar
        with st.sidebar:
            components.html(embed_component['linkedin'],height=300)

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

import streamlit as st
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constants import *
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import webbrowser
from PIL import Image

# Page Configuration Starts
st.set_page_config(page_title="Dymasius Yusuf Sitepu - Portfolio", layout="wide")

# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Apply local CSS styles from a file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Apply local CSS styles from the "style.css" file   
local_css("style/style.css")

# Configuration Ends

# Load Lottie animations from various URLs
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
aws_lottie = load_lottieurl("https://lottie.host/6eae8bdc-74d1-4b5d-9eb7-37662274cd19/Nduizk8IOf.json")
coder_lottie = load_lottieurl("https://lottie.host/5abaa94f-8ebc-4e43-9144-aa62c88a3414/1daclZN9b6.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")
# Load lottie ends

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(coder_lottie, height=280, key="data")

#########START OF SIDEBAR 
# Load the image from the specified path
image_path = 'img/dymasius.png'
image = Image.open(image_path)

# Display the image in the sidebar
st.sidebar.image(image, caption='Dymasius Yusuf Sitepu')

# Sidebar Section
with st.sidebar:
    if st.button('LinkedIn'):
        webbrowser.open("https://linkedin.com/in/dymasius/")

    if st.button('GitHub'):
        webbrowser.open("https://github.com/dymasius12")

###########END OF SIDEBAR

########### Education Section

ntu_image = "img/ntu.png"
nus_image = "img/nus.png"
stanford_image = "img/stanford.png"

st.header("🎓 Education")

# NTU Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(ntu_image, width=90)
with col2:
    st.subheader("NANYANG TECHNOLOGICAL UNIVERSITY (NTU), Singapore")
    st.write("Master of Science (MSc)")
    st.write("Financial Technology, Intelligent Process Automation")
with col3:
    st.write("Graduation Date: 2024")

# NUS Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(nus_image, width=90)
with col2:
    st.subheader("NATIONAL UNIVERSITY OF SINGAPORE (NUS), Singapore")
    st.write("Bachelor of Engineering Science (BEng)")
    st.write("Computational Engineering Science")
with col3:
    st.write("Graduation Date: 2021")

# Stanford Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(stanford_image, width=80)
with col2:
    st.subheader("STANFORD UNIVERSITY California, USA")
    st.write("International Honours Program (Summer Exchange)")
    st.write("Organizing for Good, Design Thinking")
with col3:
    st.write("Graduation Date: 2021")

########### END OF EDUCATION

# Create a container to organize content using Streamlit's container feature
with st.container():
    st.header('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie,height=50,width=50, key="js", speed=1)

# Work Experience Section
st.header("🧑‍💼 Work Experience")
st.subheader("GlobalFoundries Inc. Singapore")
st.write("Database & TapeOut Automation Engineer, Full-Time. Mar 2022 - Present")
st.markdown("""
- Implemented advanced machine learning algorithms...
- Streamlined database enablement processes...
""")
st.subheader("GlobalFoundries Inc. Singapore")
st.write("Database & TapeOut Automation Engineer, Full-Time. Mar 2022 - Present")
st.markdown("""
- Implemented advanced machine learning algorithms...
- Streamlined database enablement processes...
""")
st.subheader("GlobalFoundries Inc. Singapore")
st.write("Database & TapeOut Automation Engineer, Full-Time. Mar 2022 - Present")
st.markdown("""
- Implemented advanced machine learning algorithms...
- Streamlined database enablement processes...
""")

# Repeat this pattern for other experiences

# Research Experience Section
st.header("Research Experience")
# Add your research experience details here

# Leadership Experience Section
st.header("Leadership Experience")
# Add your leadership experience details here

# Volunteer Experience Section
st.header("Volunteer Experience")
# Add your volunteer experience details here

# Project Experience Section
st.header("Project Experience")
# Add your project experience details here

# Languages & Skills Section
st.header("Languages & Skills")
# Add your languages and skills details here

# Achievements Section
st.header("Achievements")
# Add your achievements details here

# Interests Section
st.header("Interests")
st.write("My professional interests include financial technology, software engineering, web development, machine learning, business strategy & development, big data & cloud, and quantitative trading.")


# -----------------  contact  ----------------- #
st.subheader("📨 Contact Me")
contact_form = f"""
<form action="https://formsubmit.co/{info["Email"]}" method="POST">
    <input type="hidden" name="_captcha value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer Section
st.markdown("---")
st.markdown("© 2023 Dymasius Yusuf Sitepu | All rights reserved.", unsafe_allow_html=True)


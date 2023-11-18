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

# Interest
with st.sidebar:
    st.header("INTERESTS")
    st.write("My professional interests include financial technology, software engineering, web development, machine learning, business strategy & development, big data & cloud, and quantitative trading.")

with st.sidebar:

    with st.expander("IMPORTANT LINKS & RESUME"):
        st.markdown("[RESUME](https://drive.google.com/file/d/1nCbXB3dLw640BtPMPpmYMHavERgWmggY/view?usp=sharing)")
        st.markdown("[LINKEDIN](https://linkedin.com/in/dymasius/)")
        st.markdown("[GITHUB](https://github.com/dymasius12/)")

    # Languages & Skills
    with st.expander("LANGUAGES"):
        st.write("Indonesian Language (Native)")
        st.write("English Language (Advanced)")
        st.write("Japanese Language (Intermediate)")
        st.write("Malay Language (Advanced)")
        st.write("Mandarin Language (Beginner)")

    # Achievements
    with st.expander("ACHIEVEMENTS"):
        st.write("TOP 1 Percent GLOBAL #164 out of 36,544 Quantitative Traders.")
        st.write("TOP 3 Percent NTU #15 out of 501 Quantitative Traders for 2023 NTU WorldQuant Alphaton")
        st.write("WorldQuant Gold Medal 2023")
        st.write("2nd Place Hackathon 2020+1 University College London Code Club")
        st.write("Top 15 out of 655 teams in Shopee Ultimate Case Competition 2021")
        st.write("First runner-up in NUS Public Art Competition")
        st.write("Finisher at Osim Sundown 21KM 2023 & SCSM 21KM 2022")
        st.write("GlobalFoundries Appreciation Award 2023")
        st.write("GlobalFoundries Appreciation Award 2022")
        st.write("GlobalFoundries Spotlight Award 2023")
        st.write("GlobalFoundries Spotlight Award 2022")
# Sidebar Section
# with st.sidebar:
#     if st.button('LINKEDIN'):
#         webbrowser.open("https://linkedin.com/in/dymasius/")

###########END OF SIDEBAR

##########PROJECT EXPERIENCE
# Project details displayed in main area based on selection
st.header("📁 PROJECT EXPERIENCE")
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "hidden"
    st.session_state.disabled = False
#Dropdown for selecting a project

selected_project = st.selectbox(
    "Select a Project",
    ["Credit-Card-Fraud-Detection", "The Motley S.M.A.R.T", "News_API", "UCL-IHI-Hackathon2021"],
    label_visibility=st.session_state.visibility,
)

if selected_project == "The Motley S.M.A.R.T":
    with st.expander("The Motley S.M.A.R.T", expanded=True):
        st.write("""
        The Motley S.M.A.R.T is a desktop application that provides insights and visualization for stocks, 
        specifically the S&P 500 companies. With an intuitive interface, users can either select a company 
        from a dropdown list or input a stock code directly to view comprehensive stock details or visualize 
        stock price trends.
        """)
        st.markdown("[GitHub Page](https://github.com/dymasius12/TheMotleySMART)")
        st.markdown("""
        - **Company Selection**: Choose a company from the S&P 500 list via a dropdown.
        - **Stock Dashboard**: Get a detailed dashboard view of the selected stock.
        - **Stock Price vs. Time Graph**: Visualize the stock's closing prices over time.
        """)

elif selected_project == "News_API":
    with st.expander("News_API", expanded=True):
        st.write("""
        News_API is a python script that tries to get the latest news.
        """)
        st.markdown("[GitHub Page](https://github.com/dymasius12/News_API)")
        st.write("""
        - This script allows you to fetch the latest news for a given stock company name using the NewsAPI.
        """)

elif selected_project == "UCL-IHI-Hackathon2021":
    with st.expander("UCL-IHI-Hackathon2021", expanded=True):
        st.write("""
        The IHI Code Club Hackathon 2020+1 is a full-day collaborative hacking sprint to solve real-world 
        issues in health data science. As a participant, you had the opportunity to learn from and collaborate 
        with other participants from diverse backgrounds.
        """)
        st.markdown("[GitHub Page](https://github.com/dymasius12/UCL-IHI-Hackathon2021)")
        st.write("""
        - Task: Tackling a public health problem related to air quality and respiratory illness in the US.
        """)

elif selected_project == "Credit-Card-Fraud-Detection":
    with st.expander("Credit-Card-Fraud-Detection", expanded=True):
        st.write("""
        It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase. This app is to help identify the fraudulent credit card transactions.
        """)
        st.markdown("[Web App](https://ntu-msft-mh6804.streamlit.app/)")
        st.write("""
        - Task: Tackling Credit Card Fraud Detection.
        """)

##########END OF PROJECT EXPERIENCE
########### Education Section

ntu_image = "img/ntu.png"
nus_image = "img/nus.png"
stanford_image = "img/stanford.png"

st.header("🎓 EDUCATION")

# NTU Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(ntu_image, width=90)
with col2:
    st.subheader("Nanyang Technological University (NTU) or (南洋理工大学), Singapore")
    st.write("Master of Science (MSc), Financial Technology, Intelligent Process Automation")
with col3:
    st.write("Graduation Date: 2024")

# NUS Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(nus_image, width=90)
with col2:
    st.subheader("National University of Singapore (NUS) or (新加坡國立大學), Singapore ")
    st.write("Bachelor of Engineering Science (BEng), Computational Engineering Science")
with col3:
    st.write("Graduation Date: 2021")

# Stanford Information
col1, col2, col3 = st.columns([1, 4, 2])
with col1:
    st.image(stanford_image, width=80)
with col2:
    st.subheader("Stanford University, California, USA")
    st.write("International Honours Program (Summer Exchange)")
    st.write("Organizing for Good, Design Thinking")
with col3:
    st.write("Graduation Date: 2021")

########### END OF EDUCATION

# Create a container to organize content using Streamlit's container feature
with st.container():
    st.header('⚒️ SKILLS')
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

st.header("🔬 RESEARCH EXPERIENCE")

# Nanyang Technological University Experience
col1, col2, col3 = st.columns([1, 5, 3])
with col1:
    st.image(ntu_image, width=90)
with col2:
    st.subheader("Nanyang Technological University. Singapore, SG")
    st.write("Quantitative AI/ML Researcher, Part-Time")
    st.markdown("""
        - Under NTU School of Computer Science and Engineering. PI Prof Zhang Jie, and Co-PI Dr Li Fang.
        - Quantitative and Machine Learning Researcher for funded project 2023-2025 MOE Tier-1.
        - Utilized Python for Back-End creation of Artificial Intelligence for Quantitative Trading.
    """)
with col3:
    st.write("Aug 2023 - Now")

# Stanford University Experience
col1, col2, col3 = st.columns([1, 5, 3])
with col1:
    st.image(stanford_image, width=80)
with col2:
    st.subheader("Stanford University. California, USA")
    st.write("Research Engineer, Part-Time")
    st.markdown("""
        - Collaborated with Stanford University faculty to co-author a research paper.
        - "Effective Approaches to Disaster Evacuation During a COVID-Like Pandemic".
        - Developed a deterministic SEIR model simulation using R and Python.
    """)
with col3:
    st.write("Jul 2021 - Feb 2022")

# Work Experience Section
st.header("🧑‍💼 WORK EXPERIENCE")
st.subheader("GlobalFoundries Inc. Singapore")
st.write("Database & TapeOut Automation Engineer, Full-Time. Mar 2022 - Present")
st.markdown("""
- Implemented advanced machine learning algorithms, including linear regression and XGBoost, to accurately forecast probe
card tip length and extend its lifetime by 25%, resulting in cost savings of over 1000 SGD per month.
- Streamlined database enablement processes through integration with Python Automation, reducing data processing time
by 50% and improving overall efficiency.
- Developed an internal Website and 24/7 support chatbot using Python, PHP, Bootstrap 5, HTML, CSS and JavaScript to
streamline communication between teams and increase efficiency by providing Self-updating PowerBI Dashboard and
Self-help MySQL Client.
""")
st.subheader("KOOPrime Pte Ltd. Singapore")
st.write("Software Engineer, Intern. Jun 2021 - Jul 2021")
st.markdown("""
- Developed and implemented software solutions in C# .Net and Java Spring Framework to optimize laboratory processes,
resulting in a 30% reduction in errors.
""")
st.subheader("Analog Devices, Inc. Singapore")
st.write("Data Analyst and Business Intelligence, intern. Jan 2020 - Jul 2020")
st.markdown("""
- Created self-updating visualizations in Power BI to analyze survey responses and identify key areas for improvement,
resulting in a 15% increase in overall customer satisfaction scores.
""")


# -----------------  contact  ----------------- #
st.subheader("📨 CONTACT ME")
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


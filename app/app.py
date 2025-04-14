import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the page
st.set_page_config(page_title="Job Settler", page_icon="💼", layout="centered")

# Dark mode toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if st.session_state.dark_mode:
    st.markdown("""<style>body { background-color: #0e1117; color: white; }</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>body { background-color: white; color: black; }</style>""", unsafe_allow_html=True)

# Load logo
logo = Image.open("C:/Users/Main Computer/Downloads/JOB_Settler_Full_Package/assets/logo.png")





# Sidebar and Logo
with st.sidebar:
    st.image(logo, use_container_width=True)
    st.markdown("### YOU SIT COMFORTABLY UNTIL WE FIND A PERFECT JOB FOR YOU")
    dark_toggle = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.dark_mode = dark_toggle

# Title
st.title("👨‍💼 JOB Settler")
st.subheader("Let’s get you hired on autopilot.")

# Step 1: User Info form
st.markdown("### Step 1: Tell us about yourself")
with st.form("user_info_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn Profile URL")
    address = st.text_area("Current Address")
    job_title = st.text_input("Desired Job Title")
    location = st.text_input("Preferred Location")
    job_type = st.selectbox("Job Type", ["Full-time", "Part-time", "Internship", "Contract", "Remote"])
    job_keywords = st.text_input("Keywords to match (comma-separated)")
    resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
    submit_button = st.form_submit_button("Next")
    if submit_button:
        st.session_state.update({
            "name": name,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "address": address,
            "job_title": job_title,
            "location": location,
            "job_type": job_type,
            "job_keywords": job_keywords,
            "resume": resume,
        })

# Step 2: Send email notification
def send_email_notification(to_email):
    sender_email = "your_gmail_address@gmail.com"
    sender_password = "your_gmail_app_password"

    subject = "Job Application Notification"
    body = f"Hi {st.session_state['name']},\n\nYour details have been successfully submitted for job applications.\n\nBest,\nJOB Settler Team"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        st.success("✅ Email notification sent!")
    except Exception as e:
        st.error(f"Email sending failed: {e}")

# Step 3: Display user info and send email
if "name" in st.session_state:
    st.markdown(f"**Name:** {st.session_state['name']}")
    st.markdown(f"**Email:** {st.session_state['email']}")
    st.markdown(f"**Phone:** {st.session_state['phone']}")
    st.markdown(f"**LinkedIn:** {st.session_state['linkedin']}")
    st.markdown(f"**Address:** {st.session_state['address']}")
    st.markdown(f"**Desired Job Title:** {st.session_state['job_title']}")
    st.markdown(f"**Preferred Location:** {st.session_state['location']}")
    st.markdown(f"**Job Type:** {st.session_state['job_type']}")
    st.markdown(f"**Keywords:** {st.session_state['job_keywords']}")
    
    if st.button("Submit Application"):
        send_email_notification(st.session_state["email"])

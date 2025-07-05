import streamlit as st
import json
from datetime import datetime
from data.work_experience import WORK_EXPERIENCE
from data.skills_data import SKILLS_DATA, CERTIFICATIONS
from data.poetry_content import POETRY_CONTENT

st.set_page_config(
    page_title="Portfolio Admin Panel",
    page_icon="⚙️",
    layout="wide"
)

def save_work_experience(data):
    """Save work experience data to file"""
    with open('data/work_experience.py', 'w') as f:
        f.write(f"# Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("from datetime import datetime\n\n")
        f.write(f"WORK_EXPERIENCE = {repr(data)}")

def save_skills_data(skills, certs):
    """Save skills and certifications data to file"""
    with open('data/skills_data.py', 'w') as f:
        f.write(f"# Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"SKILLS_DATA = {repr(skills)}\n\n")
        f.write(f"CERTIFICATIONS = {repr(certs)}")

def save_poetry_content(data):
    """Save poetry content to file"""
    with open('data/poetry_content.py', 'w') as f:
        f.write(f"# Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"POETRY_CONTENT = {repr(data)}")

# Authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 Admin Login")
    password = st.text_input("Enter Admin Password", type="password")
    if st.button("Login"):
        if password == "admin123":
            st.session_state.authenticated = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid password")
    st.stop()

# Main admin interface
st.title("⚙️ Portfolio Admin Panel")
st.markdown("**Manage Akhilesh Singh's Portfolio Content**")

tab1, tab2, tab3, tab4 = st.tabs(["Work Experience", "Skills", "Poetry", "Backup"])

with tab1:
    st.header("💼 Work Experience Management")
    
    st.subheader("Current Jobs")
    for i, job in enumerate(WORK_EXPERIENCE):
        with st.expander(f"{job['title']} at {job['company']}"):
            st.write(f"**Duration:** {job['duration']}")
            st.write(f"**Location:** {job['location']}")
            st.write("**Description:**")
            for desc in job['description']:
                st.write(f"• {desc}")
            st.write(f"**Skills:** {', '.join(job['skills'])}")
    
    st.divider()
    st.subheader("Add New Job")
    
    with st.form("add_job"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Job Title")
            company = st.text_input("Company")
            location = st.text_input("Location")
        with col2:
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date (optional)", value=None)
            duration = st.text_input("Duration Text")
        
        description = st.text_area("Job Description (one point per line)")
        skills = st.text_input("Skills (comma-separated)")
        
        if st.form_submit_button("Add Job"):
            if title and company:
                new_job = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "start_date": datetime.combine(start_date, datetime.min.time()),
                    "end_date": datetime.combine(end_date, datetime.min.time()) if end_date else None,
                    "duration": duration,
                    "description": [d.strip() for d in description.split('\n') if d.strip()],
                    "skills": [s.strip() for s in skills.split(',') if s.strip()]
                }
                
                updated_jobs = [new_job] + WORK_EXPERIENCE
                save_work_experience(updated_jobs)
                st.success("Job added! Please restart the main app to see changes.")

with tab2:
    st.header("🛠️ Skills Management")
    
    st.subheader("Current Skills by Category")
    for category, skills in SKILLS_DATA.items():
        with st.expander(f"{category} ({len(skills)} skills)"):
            for skill, level in skills.items():
                st.write(f"**{skill}:** {level}%")
    
    st.divider()
    st.subheader("Add New Skill")
    
    with st.form("add_skill"):
        category = st.selectbox("Category", list(SKILLS_DATA.keys()))
        skill_name = st.text_input("Skill Name")
        proficiency = st.slider("Proficiency (%)", 0, 100, 50)
        
        if st.form_submit_button("Add Skill"):
            if skill_name:
                updated_skills = SKILLS_DATA.copy()
                updated_skills[category][skill_name] = proficiency
                save_skills_data(updated_skills, CERTIFICATIONS)
                st.success("Skill added! Please restart the main app to see changes.")

with tab3:
    st.header("🎭 Poetry Content Management")
    
    st.subheader("Current Introduction")
    st.write(POETRY_CONTENT['introduction'])
    
    st.subheader("Favorite Quotes")
    for i, quote in enumerate(POETRY_CONTENT['favorite_quotes']):
        with st.expander(f"Quote {i+1}: {quote['author']}"):
            st.write(f"**Quote:** {quote['quote']}")
            st.write(f"**Author:** {quote['author']}")
            st.write(f"**Poem:** {quote['poem']}")
    
    st.divider()
    st.subheader("Add New Quote")
    
    with st.form("add_quote"):
        quote_text = st.text_area("Quote Text")
        author = st.text_input("Author")
        poem = st.text_input("Poem Title")
        
        if st.form_submit_button("Add Quote"):
            if quote_text and author:
                new_quote = {
                    "quote": quote_text,
                    "author": author,
                    "poem": poem
                }
                
                updated_poetry = POETRY_CONTENT.copy()
                updated_poetry['favorite_quotes'].append(new_quote)
                save_poetry_content(updated_poetry)
                st.success("Quote added! Please restart the main app to see changes.")

with tab4:
    st.header("💾 Backup & Settings")
    
    st.subheader("Download Data Backup")
    backup_data = {
        'work_experience': WORK_EXPERIENCE,
        'skills_data': SKILLS_DATA,
        'certifications': CERTIFICATIONS,
        'poetry_content': POETRY_CONTENT,
        'backup_date': datetime.now().isoformat()
    }
    
    st.download_button(
        label="Download Full Backup (JSON)",
        data=json.dumps(backup_data, indent=2, default=str),
        file_name=f"portfolio_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )
    
    st.subheader("Admin Info")
    st.info("Admin password: admin123")
    st.warning("After making changes, restart the main portfolio app to see updates.")
    
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
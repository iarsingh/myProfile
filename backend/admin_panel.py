import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

# Import current data
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from data.work_experience import WORK_EXPERIENCE
    from data.skills_data import SKILLS_DATA, CERTIFICATIONS
    from data.poetry_content import POETRY_CONTENT
except ImportError as e:
    st.error(f"Failed to import data modules: {e}")
    st.info("Please ensure you're running this from the correct directory.")
    st.stop()

def save_data_to_file(data, filename):
    """Save data to Python file"""
    with open(f"../data/{filename}", 'w') as f:
        f.write(f"# Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        if filename == 'work_experience.py':
            f.write("from datetime import datetime\n\n")
            f.write(f"WORK_EXPERIENCE = {repr(data)}")
        elif filename == 'skills_data.py':
            f.write(f"SKILLS_DATA = {repr(data['skills'])}\n\n")
            f.write(f"CERTIFICATIONS = {repr(data['certifications'])}")
        elif filename == 'poetry_content.py':
            f.write(f"POETRY_CONTENT = {repr(data)}")

def admin_main():
    st.set_page_config(
        page_title="Portfolio Admin Panel",
        page_icon="⚙️",
        layout="wide"
    )
    
    st.title("⚙️ Portfolio Admin Panel")
    st.markdown("**Manage Akhilesh Singh's Portfolio Content**")
    
    # Authentication (simple password protection)
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        password = st.text_input("Enter Admin Password", type="password")
        if st.button("Login"):
            if password == "admin123":  # Simple password for demo
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid password")
        return
    
    # Main admin interface
    tab1, tab2, tab3, tab4 = st.tabs(["Work Experience", "Skills & Certifications", "Poetry Content", "Settings"])
    
    with tab1:
        manage_work_experience()
    
    with tab2:
        manage_skills_certifications()
    
    with tab3:
        manage_poetry_content()
    
    with tab4:
        manage_settings()

def manage_work_experience():
    st.header("📼 Manage Work Experience")
    
    # Display current work experience
    st.subheader("Current Work Experience")
    for i, job in enumerate(WORK_EXPERIENCE):
        with st.expander(f"{job['title']} at {job['company']}"):
            st.write(f"**Duration:** {job['duration']}")
            st.write(f"**Location:** {job['location']}")
            st.write("**Description:**")
            for desc in job['description']:
                st.write(f"• {desc}")
            st.write(f"**Skills:** {', '.join(job['skills'])}")
    
    st.divider()
    
    # Add new work experience
    st.subheader("➕ Add New Work Experience")
    with st.form("add_work_experience"):
        col1, col2 = st.columns(2)
        
        with col1:
            new_title = st.text_input("Job Title")
            new_company = st.text_input("Company")
            new_location = st.text_input("Location")
            
        with col2:
            new_start_date = st.date_input("Start Date")
            new_end_date = st.date_input("End Date (leave blank if current)", value=None)
            new_duration = st.text_input("Duration Text (e.g., 'Jan 2023 - Present')")
        
        new_description = st.text_area("Job Description (one point per line)")
        new_skills = st.text_input("Skills (comma-separated)")
        
        submitted = st.form_submit_button("Add Work Experience")
        
        if submitted and new_title and new_company:
            # Add new job to the list
            new_job = {
                "title": new_title,
                "company": new_company,
                "location": new_location,
                "start_date": datetime.combine(new_start_date, datetime.min.time()),
                "end_date": datetime.combine(new_end_date, datetime.min.time()) if new_end_date else None,
                "duration": new_duration,
                "description": [desc.strip() for desc in new_description.split('\n') if desc.strip()],
                "skills": [skill.strip() for skill in new_skills.split(',') if skill.strip()]
            }
            
            updated_experience = [new_job] + WORK_EXPERIENCE
            save_data_to_file(updated_experience, 'work_experience.py')
            st.success("Work experience added successfully!")
            st.info("Please restart the main application to see changes.")

def manage_skills_certifications():
    st.header("🛠️ Manage Skills & Certifications")
    
    # Skills management
    st.subheader("Technical Skills")
    
    for category, skills in SKILLS_DATA.items():
        with st.expander(f"{category} ({len(skills)} skills)"):
            for skill, proficiency in skills.items():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{skill}**")
                with col2:
                    st.write(f"{proficiency}%")
    
    st.divider()
    
    # Add new skill
    st.subheader("➕ Add New Skill")
    with st.form("add_skill"):
        skill_category = st.selectbox("Category", list(SKILLS_DATA.keys()))
        skill_name = st.text_input("Skill Name")
        skill_proficiency = st.slider("Proficiency Level (%)", 0, 100, 50)
        
        if st.form_submit_button("Add Skill"):
            if skill_name:
                updated_skills = SKILLS_DATA.copy()
                updated_skills[skill_category][skill_name] = skill_proficiency
                
                data_to_save = {
                    'skills': updated_skills,
                    'certifications': CERTIFICATIONS
                }
                save_data_to_file(data_to_save, 'skills_data.py')
                st.success("Skill added successfully!")
    
    st.divider()
    
    # Certifications management
    st.subheader("📜 Certifications")
    for cert in CERTIFICATIONS:
        with st.expander(cert['name']):
            st.write(f"**Issuer:** {cert['issuer']}")
            st.write(f"**Year:** {cert['year']}")

def manage_poetry_content():
    st.header("🎭 Manage Poetry Content")
    
    # Display current poetry content
    st.subheader("Current Poetry Introduction")
    st.write(POETRY_CONTENT['introduction'])
    
    st.subheader("Favorite Quotes")
    for i, quote in enumerate(POETRY_CONTENT['favorite_quotes']):
        with st.expander(f"Quote {i+1}: {quote['author']}"):
            st.write(f"**Quote:** {quote['quote']}")
            st.write(f"**Author:** {quote['author']}")
            st.write(f"**Poem:** {quote['poem']}")
    
    st.divider()
    
    # Add new quote
    st.subheader("➕ Add New Favorite Quote")
    with st.form("add_quote"):
        quote_text = st.text_area("Quote Text")
        quote_author = st.text_input("Author")
        quote_poem = st.text_input("Poem Title")
        
        if st.form_submit_button("Add Quote"):
            if quote_text and quote_author:
                new_quote = {
                    "quote": quote_text,
                    "author": quote_author,
                    "poem": quote_poem
                }
                
                updated_poetry = POETRY_CONTENT.copy()
                updated_poetry['favorite_quotes'].append(new_quote)
                
                save_data_to_file(updated_poetry, 'poetry_content.py')
                st.success("Quote added successfully!")

def manage_settings():
    st.header("⚙️ Settings")
    
    st.subheader("Admin Configuration")
    st.info("Admin password: admin123 (Change this in production)")
    
    st.subheader("Data Backup")
    if st.button("📥 Download Data Backup"):
        backup_data = {
            'work_experience': WORK_EXPERIENCE,
            'skills_data': SKILLS_DATA,
            'certifications': CERTIFICATIONS,
            'poetry_content': POETRY_CONTENT,
            'backup_date': datetime.now().isoformat()
        }
        
        st.download_button(
            label="Download Backup JSON",
            data=json.dumps(backup_data, indent=2, default=str),
            file_name=f"portfolio_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    st.subheader("Application Control")
    st.warning("Note: Changes require restarting the main portfolio application to take effect.")
    
    if st.button("🔄 Restart Main Application"):
        st.info("Please manually restart the 'Streamlit Portfolio' workflow to see changes.")

if __name__ == "__main__":
    admin_main()
import streamlit as st
import json
from datetime import datetime
from data.work_experience import WORK_EXPERIENCE
from data.skills_data import SKILLS_DATA, CERTIFICATIONS
from data.poetry_content import POETRY_CONTENT

st.set_page_config(
    page_title="AI Portfolio Assistant",
    page_icon="🤖",
    layout="wide"
)

def get_portfolio_context():
    """Get all portfolio data as context for AI responses"""
    return {
        "work_experience": WORK_EXPERIENCE,
        "skills": SKILLS_DATA,
        "certifications": CERTIFICATIONS,
        "poetry": POETRY_CONTENT,
        "personal_info": {
            "name": "Akhilesh Singh",
            "title": "DevOps Engineer",
            "location": "Mumbai, Maharashtra",
            "email": "akhileshranjan.ks@gmail.com",
            "phone": "+91-8002392976",
            "education": "B.E. Computer Science from RGPV, Bhopal (2019)"
        }
    }

def search_skills(query):
    """Search through skills based on query"""
    results = []
    query_lower = query.lower()
    
    for category, skills in SKILLS_DATA.items():
        for skill, proficiency in skills.items():
            if query_lower in skill.lower() or query_lower in category.lower():
                results.append({
                    "skill": skill,
                    "category": category,
                    "proficiency": proficiency
                })
    
    return results

def search_experience(query):
    """Search through work experience based on query"""
    results = []
    query_lower = query.lower()
    
    for job in WORK_EXPERIENCE:
        # Search in title, company, description, skills
        searchable_text = f"{job['title']} {job['company']} {' '.join(job['description'])} {' '.join(job['skills'])}".lower()
        
        if query_lower in searchable_text:
            results.append(job)
    
    return results

def search_certifications(query):
    """Search through certifications based on query"""
    results = []
    query_lower = query.lower()
    
    for cert in CERTIFICATIONS:
        searchable_text = f"{cert['name']} {cert['issuer']}".lower()
        if query_lower in searchable_text:
            results.append(cert)
    
    return results

def generate_answer(question):
    """Generate intelligent answers based on portfolio data"""
    question_lower = question.lower()
    
    # Experience-related questions
    if any(word in question_lower for word in ['experience', 'work', 'job', 'role', 'position']):
        if 'current' in question_lower or 'present' in question_lower:
            current_job = WORK_EXPERIENCE[0]  # First job is current
            return f"Akhilesh currently works as a {current_job['title']} at {current_job['company']} in {current_job['location']} since {current_job['duration']}. His key responsibilities include: {'; '.join(current_job['description'][:3])}"
        
        elif 'total' in question_lower or 'years' in question_lower:
            return "Akhilesh has 5+ years of professional experience in DevOps and Cloud Engineering, having worked at TCS, Tech Mahindra, and currently at Capgemini."
        
        else:
            return f"Akhilesh has worked at {len(WORK_EXPERIENCE)} companies: " + ", ".join([f"{job['title']} at {job['company']}" for job in WORK_EXPERIENCE])
    
    # Skills-related questions
    elif any(word in question_lower for word in ['skill', 'technology', 'tech', 'tools']):
        if 'cloud' in question_lower:
            cloud_skills = SKILLS_DATA.get('Cloud Platforms', {})
            return f"Akhilesh has expertise in cloud platforms: {', '.join([f'{k} ({v}%)' for k, v in cloud_skills.items()])}"
        
        elif 'devops' in question_lower or 'ci/cd' in question_lower:
            devops_skills = SKILLS_DATA.get('DevOps & CI/CD', {})
            return f"His DevOps expertise includes: {', '.join([f'{k} ({v}%)' for k, v in devops_skills.items()])}"
        
        else:
            total_skills = sum(len(skills) for skills in SKILLS_DATA.values())
            return f"Akhilesh has {total_skills} technical skills across {len(SKILLS_DATA)} categories: {', '.join(SKILLS_DATA.keys())}"
    
    # Certification questions
    elif any(word in question_lower for word in ['certification', 'certified', 'certificate']):
        cert_count = len(CERTIFICATIONS)
        latest_cert = max(CERTIFICATIONS, key=lambda x: x['year'])
        return f"Akhilesh has {cert_count} professional certifications. His latest certification is '{latest_cert['name']}' from {latest_cert['issuer']} in {latest_cert['year']}."
    
    # Poetry/creative questions
    elif any(word in question_lower for word in ['poetry', 'creative', 'passion', 'hobby']):
        return "Beyond technology, Akhilesh is passionate about poetry. He enjoys both writing and listening to poetry, including Classical Urdu Poetry, English Romantic Poetry, and Contemporary Spoken Word. He believes poetry and code share similarities in precision, rhythm, and beauty."
    
    # Contact questions
    elif any(word in question_lower for word in ['contact', 'email', 'phone', 'reach']):
        return "You can reach Akhilesh at akhileshranjan.ks@gmail.com or call him at +91-8002392976. He's based in Mumbai, Maharashtra."
    
    # Education questions
    elif any(word in question_lower for word in ['education', 'degree', 'study', 'college']):
        return "Akhilesh holds a Bachelor of Engineering (B.E.) in Computer Science from Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV), Bhopal, completed in 2019."
    
    else:
        return "I can help you with questions about Akhilesh's work experience, skills, certifications, poetry interests, contact information, or education. What specific information are you looking for?"

# Main app
st.title("🤖 AI Portfolio Assistant")
st.markdown("**Ask me anything about Akhilesh Singh's professional profile!**")

# Search modes
search_mode = st.selectbox(
    "Choose search type:",
    ["Smart Q&A", "Skills Search", "Experience Search", "Certification Search", "Quick Facts"]
)

if search_mode == "Smart Q&A":
    st.subheader("💬 Ask Questions")
    
    # Suggested questions
    st.markdown("**Suggested questions:**")
    suggestions = [
        "What is Akhilesh's current role?",
        "How many years of experience does he have?",
        "What cloud platforms does he work with?",
        "What are his DevOps skills?",
        "What certifications does he have?",
        "Tell me about his poetry interests",
        "How can I contact him?"
    ]
    
    selected_suggestion = st.selectbox("Quick questions:", [""] + suggestions)
    
    # Question input
    user_question = st.text_input("Or ask your own question:", value=selected_suggestion)
    
    if user_question:
        with st.spinner("Thinking..."):
            answer = generate_answer(user_question)
            st.success(answer)

elif search_mode == "Skills Search":
    st.subheader("🔍 Search Skills")
    skill_query = st.text_input("Search for specific skills or technologies:")
    
    if skill_query:
        results = search_skills(skill_query)
        if results:
            st.write(f"Found {len(results)} matching skills:")
            for result in results:
                st.write(f"**{result['skill']}** ({result['category']}) - {result['proficiency']}%")
        else:
            st.warning("No matching skills found.")

elif search_mode == "Experience Search":
    st.subheader("💼 Search Work Experience")
    exp_query = st.text_input("Search in job descriptions, companies, or technologies:")
    
    if exp_query:
        results = search_experience(exp_query)
        if results:
            st.write(f"Found {len(results)} matching positions:")
            for job in results:
                with st.expander(f"{job['title']} at {job['company']}"):
                    st.write(f"**Duration:** {job['duration']}")
                    st.write(f"**Key skills:** {', '.join(job['skills'][:5])}")
        else:
            st.warning("No matching experience found.")

elif search_mode == "Certification Search":
    st.subheader("🏆 Search Certifications")
    cert_query = st.text_input("Search certifications by name or provider:")
    
    if cert_query:
        results = search_certifications(cert_query)
        if results:
            st.write(f"Found {len(results)} matching certifications:")
            for cert in results:
                st.write(f"**{cert['name']}** - {cert['issuer']} ({cert['year']})")
        else:
            st.warning("No matching certifications found.")

elif search_mode == "Quick Facts":
    st.subheader("⚡ Quick Facts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Experience", "5+ Years")
        st.metric("Current Company", "Capgemini")
        st.metric("Total Skills", f"{sum(len(skills) for skills in SKILLS_DATA.values())}")
        st.metric("Certifications", f"{len(CERTIFICATIONS)}")
    
    with col2:
        st.metric("Skill Categories", f"{len(SKILLS_DATA)}")
        st.metric("Companies Worked", f"{len(WORK_EXPERIENCE)}")
        st.metric("Location", "Mumbai")
        st.metric("Poetry Quotes", f"{len(POETRY_CONTENT['favorite_quotes'])}")

# Chat history
st.divider()
st.subheader("💡 AI Insights")

insights = [
    "Akhilesh has strong expertise in all major cloud platforms (AWS, Azure, GCP)",
    "His DevOps skills include the full CI/CD pipeline implementation",
    "He's actively learning MLOps to bridge ML and operations",
    "Poetry passion shows his creative and analytical thinking balance",
    "5+ years of progressive career growth across top tech companies"
]

for insight in insights:
    st.info(f"💡 {insight}")

# Data source indicator
st.divider()
st.caption("🔄 Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
st.caption("📊 Data source: Live portfolio database")
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# Import custom components
from components.career_timeline import render_career_timeline
from components.skills_visualization import render_skills_visualization
from components.poetry_section import render_poetry_section
from components.contact_info import render_contact_info
from data.work_experience import WORK_EXPERIENCE
from data.skills_data import SKILLS_DATA, CERTIFICATIONS
from data.poetry_content import POETRY_CONTENT

# Page configuration
st.set_page_config(
    page_title="Akhilesh Singh - DevOps Engineer & Poetry Enthusiast",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 10px;
    }
    .section-header {
        border-left: 4px solid #667eea;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
    .experience-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    .skill-tag {
        background: #e3f2fd;
        color: #1976d2;
        padding: 0.2rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Akhilesh Singh</h1>
        <h3>DevOps Engineer | Cloud Architect | Poetry Enthusiast</h3>
        <p>Bridging Technology and Creativity through Code and Verse</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose your focus:",
        ["🏠 Overview", "💼 Technical Journey", "📊 Skills & Certifications", "🎭 Creative Passion", "🤖 AI Assistant", "📞 Connect"]
    )

    if page == "🏠 Overview":
        render_overview()
    elif page == "💼 Technical Journey":
        render_technical_journey()
    elif page == "📊 Skills & Certifications":
        render_skills_certifications()
    elif page == "🎭 Creative Passion":
        render_creative_passion()
    elif page == "🤖 AI Assistant":
        render_ai_assistant()
    elif page == "📞 Connect":
        render_connect()

def render_overview():
    st.markdown('<h2 class="section-header">Professional Summary</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        **Experienced DevOps Engineer** actively transitioning into Full Stack Development and MLOps to build scalable, 
        intelligent, and production-ready software systems.
        
        🔹 **5+ years** of hands-on experience in cloud platforms (AWS, Azure, GCP)  
        🔹 **Expert** in CI/CD, Kubernetes, Docker, and Infrastructure as Code  
        🔹 **Passionate** about automation, monitoring, and system reliability  
        🔹 **Creative soul** with a deep love for poetry and literary expression  
        """)
        
        st.markdown("### 🎯 Current Focus")
        st.info("""
        - Expanding Full Stack development skills (Java, React, Node.js)
        - Exploring MLOps practices and tools (MLflow, Kubeflow)
        - Contributing to the intersection of technology and creativity
        """)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Years of Experience", "5+", "DevOps & Cloud")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Certifications", "5", "Cloud & DevOps")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Cloud Platforms", "3", "AWS, Azure, GCP")
        st.markdown('</div>', unsafe_allow_html=True)

    # Quick stats
    st.markdown('<h2 class="section-header">Quick Insights</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Companies", "3", "TCS → Tech Mahindra → Capgemini")
    with col2:
        st.metric("Current Role", "Consultant", "at Capgemini")
    with col3:
        st.metric("Education", "B.E.", "Computer Science")
    with col4:
        st.metric("Location", "Mumbai", "Maharashtra")

def render_technical_journey():
    st.markdown('<h2 class="section-header">Career Timeline</h2>', unsafe_allow_html=True)
    render_career_timeline(WORK_EXPERIENCE)

def render_skills_certifications():
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    render_skills_visualization(SKILLS_DATA)
    
    st.markdown('<h2 class="section-header">Certifications</h2>', unsafe_allow_html=True)
    
    for cert in CERTIFICATIONS:
        st.markdown(f"""
        <div class="experience-card">
            <h4>🏆 {cert['name']}</h4>
            <p><strong>Year:</strong> {cert['year']} | <strong>Issuer:</strong> {cert['issuer']}</p>
        </div>
        """, unsafe_allow_html=True)

def render_creative_passion():
    st.markdown('<h2 class="section-header">Poetry & Creative Expression</h2>', unsafe_allow_html=True)
    render_poetry_section(POETRY_CONTENT)

def render_ai_assistant():
    st.markdown('<h2 class="section-header">AI Portfolio Assistant</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h3>🤖 Ask me anything about Akhilesh's profile!</h3>
        <p>Get instant answers about experience, skills, certifications, and more</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search functionality
    search_mode = st.selectbox(
        "Choose search type:",
        ["Smart Q&A", "Skills Search", "Experience Search", "Quick Facts"]
    )
    
    if search_mode == "Smart Q&A":
        st.subheader("💬 Ask Questions")
        
        # Suggested questions
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
        user_question = st.text_input("Or ask your own question:", value=selected_suggestion)
        
        if user_question:
            answer = generate_ai_answer(user_question)
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
    
    # AI Insights
    st.divider()
    st.subheader("💡 AI Insights")
    
    insights = [
        "Strong expertise in all major cloud platforms (AWS, Azure, GCP)",
        "Full DevOps pipeline implementation experience",
        "Actively learning MLOps to bridge ML and operations",
        "Poetry passion shows creative and analytical thinking balance",
        "5+ years of progressive career growth across top tech companies"
    ]
    
    for insight in insights:
        st.info(f"💡 {insight}")

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
        searchable_text = f"{job['title']} {job['company']} {' '.join(job['description'])} {' '.join(job['skills'])}".lower()
        
        if query_lower in searchable_text:
            results.append(job)
    
    return results

def generate_ai_answer(question):
    """Generate intelligent answers based on portfolio data"""
    question_lower = question.lower()
    
    # Experience-related questions
    if any(word in question_lower for word in ['experience', 'work', 'job', 'role', 'position']):
        if 'current' in question_lower or 'present' in question_lower:
            current_job = WORK_EXPERIENCE[0]
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

def render_connect():
    st.markdown('<h2 class="section-header">Let\'s Connect</h2>', unsafe_allow_html=True)
    render_contact_info()

if __name__ == "__main__":
    main()

import streamlit as st

def render_contact_info():
    """Render contact information and social links"""
    
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h2>📞 Let's Connect & Collaborate</h2>
        <p style="font-size: 1.1rem;">
            Whether you want to discuss DevOps, cloud architecture, or share a beautiful poem!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Information
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📧 Contact Information")
        
        contact_info = {
            "📧 Email": "akhileshranjan.ks@gmail.com",
            "📱 Phone": "+91-8002392976",
            "🏠 Location": "Mumbai, Maharashtra",
            "🎂 Born": "August 2, 1998",
            "🗣️ Languages": "English, Hindi"
        }
        
        for label, info in contact_info.items():
            st.markdown(f"**{label}:** {info}")
    
    with col2:
        st.markdown("### 🌐 Professional Links")
        
        # Professional links
        links = [
            ("LinkedIn", "https://linkedin.com/in/akhilesh-singh", "💼"),
            ("GitHub", "https://github.com/akhilesh-singh", "💻"),
            ("HackerRank", "https://hackerrank.com/akhilesh", "🏆"),
            ("Coursera", "https://coursera.org/user/akhilesh", "📚"),
            ("Credly", "https://credly.com/users/akhilesh", "🏅"),
            ("GCP Skill Boost", "https://cloudskillsboost.google/profile/akhilesh", "☁️")
        ]
        
        for name, url, icon in links:
            st.markdown(f"{icon} **{name}**: [Visit Profile]({url})")
    
    # Address
    st.markdown("### 🏡 Address")
    st.info("Digamber Building - A wing 102, Airoli, Sector-20, Mumbai-400708, Maharashtra")
    
    # Call to action
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💼 Professional Opportunities
        - DevOps Engineering roles
        - Cloud Architecture projects
        - MLOps and Full Stack development
        - Technical consulting and mentoring
        """)
        
        if st.button("📧 Send Professional Email"):
            st.info("Email: akhileshranjan.ks@gmail.com\nSubject: Professional Opportunity")
    
    with col2:
        st.markdown("""
        ### 🎭 Creative Collaborations
        - Poetry discussions and exchanges
        - Tech-poetry fusion projects
        - Creative writing workshops
        - Literary technology initiatives
        """)
        
        if st.button("✉️ Send Creative Message"):
            st.info("Email: akhileshranjan.ks@gmail.com\nSubject: Creative Collaboration")
    
    # Education
    st.markdown("---")
    st.markdown("### 🎓 Education")
    st.markdown("""
    **Bachelor of Engineering (Computer Science)**  
    *Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV), Bhopal*  
    **Year:** 2019
    """)
    
    # Fun fact
    st.markdown("---")
    st.success("""
    🎯 **Fun Fact:** I believe the best engineers are also poets at heart - 
    we both craft something beautiful from seemingly simple elements!
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; font-style: italic;">
        <p>"Where cloud architecture meets creative expression"</p>
        <p>© 2025 Akhilesh Singh - DevOps Engineer & Poetry Enthusiast</p>
    </div>
    """, unsafe_allow_html=True)

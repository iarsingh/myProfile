import streamlit as st
import random

def render_poetry_section(poetry_content):
    """Render the poetry and creative passion section"""
    
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-bottom: 2rem;">
        <h2>🎭 Where Technology Meets Poetry</h2>
        <p style="font-style: italic; font-size: 1.1rem;">
            "In the silence between keystrokes, poetry is born"
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("### 📖 My Creative Journey")
    st.write(poetry_content["introduction"])
    
    # Tabs for different poetry content
    tab1, tab2, tab3, tab4 = st.tabs(["💫 Favorite Quotes", "🎵 Listening Preferences", "🔗 Tech & Poetry", "✨ Reflection"])
    
    with tab1:
        st.markdown("### ✨ Verses That Inspire Me")
        
        # Random quote feature
        if st.button("🔀 Show Random Quote"):
            quote = random.choice(poetry_content["favorite_quotes"])
        else:
            quote = poetry_content["favorite_quotes"][0]
        
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 2rem; border-radius: 10px; 
                    border-left: 4px solid #667eea; margin: 1rem 0;">
            <blockquote style="font-style: italic; font-size: 1.2rem; color: #495057; margin-bottom: 1rem;">
                "{quote['quote']}"
            </blockquote>
            <div style="text-align: right; color: #6c757d;">
                <strong>— {quote['author']}</strong><br>
                <em>{quote['poem']}</em>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # All favorite quotes
        st.markdown("#### 📚 Complete Collection")
        for i, quote in enumerate(poetry_content["favorite_quotes"]):
            with st.expander(f"Quote {i+1}: {quote['author']} - {quote['poem']}"):
                st.markdown(f"*\"{quote['quote']}\"*")
                st.markdown(f"**— {quote['author']}** from *{quote['poem']}*")
    
    with tab2:
        st.markdown("### 🎵 What I Love to Listen To")
        
        for i, preference in enumerate(poetry_content["listening_preferences"]):
            st.markdown(f"**{i+1}.** {preference}")
        
        st.markdown("---")
        st.info("""
        **Why Poetry Matters in Tech:**
        Poetry keeps me grounded and reminds me that behind every line of code, 
        there's human creativity and emotion. It helps me approach problems with 
        both analytical thinking and creative intuition.
        """)
    
    with tab3:
        st.markdown("### 🔗 The Connection Between Code and Verse")
        st.markdown(poetry_content["tech_poetry_connection"])
        
        # Interactive comparison
        st.markdown("#### 🔄 Parallels I've Discovered")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🖥️ In DevOps:**")
            st.markdown("""
            - Orchestrating systems in harmony
            - Creating elegant automation flows  
            - Debugging with patience and precision
            - Building resilient, beautiful architectures
            - Continuous improvement and iteration
            """)
        
        with col2:
            st.markdown("**📝 In Poetry:**")
            st.markdown("""
            - Crafting verses that flow seamlessly
            - Finding the perfect word for each moment
            - Editing with careful attention to detail  
            - Creating beauty that stands the test of time
            - Constantly refining and perfecting the craft
            """)
    
    with tab4:
        st.markdown("### ✨ Personal Reflection")
        st.write(poetry_content["personal_reflection"])
        
        st.markdown("---")
        
        # Interactive element
        if st.button("🎯 My Philosophy"):
            st.success("""
            **"Code with Poetry, Engineer with Heart"**
            
            Every system I architect, every pipeline I build, carries a piece of the creativity 
            that poetry has nurtured in me. Technology should not just work—it should inspire.
            """)
        
        # Quote of the day feature
        st.markdown("#### 💭 Today's Inspiration")
        daily_quotes = [
            "The best code is poetry in motion - elegant, purposeful, and beautiful.",
            "Like a well-structured poem, good architecture tells a story.",
            "In debugging, as in poetry, every word matters.",
            "Automation is the rhythm that keeps our digital world in harmony."
        ]
        
        import datetime
        today_index = datetime.datetime.now().day % len(daily_quotes)
        st.info(f"💡 {daily_quotes[today_index]}")

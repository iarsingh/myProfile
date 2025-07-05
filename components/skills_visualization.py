import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_skills_visualization(skills_data):
    """Render interactive skills visualization"""
    
    # Skills overview
    tab1, tab2, tab3 = st.tabs(["📊 Skills Overview", "🎯 Proficiency Levels", "📈 Skills Comparison"])
    
    with tab1:
        # Create a comprehensive skills dataframe
        all_skills = []
        for category, skills in skills_data.items():
            for skill, proficiency in skills.items():
                all_skills.append({
                    'Category': category,
                    'Skill': skill,
                    'Proficiency': proficiency
                })
        
        skills_df = pd.DataFrame(all_skills)
        
        # Sunburst chart for skills hierarchy
        fig_sunburst = px.sunburst(
            skills_df,
            path=['Category', 'Skill'],
            values='Proficiency',
            title="Skills Portfolio Overview",
            color='Proficiency',
            color_continuous_scale='Blues'
        )
        fig_sunburst.update_layout(height=600)
        st.plotly_chart(fig_sunburst, use_container_width=True)
    
    with tab2:
        # Category selection
        selected_category = st.selectbox(
            "Select a skill category to explore:",
            list(skills_data.keys())
        )
        
        # Horizontal bar chart for selected category
        category_skills = skills_data[selected_category]
        
        fig_bar = go.Figure(go.Bar(
            x=list(category_skills.values()),
            y=list(category_skills.keys()),
            orientation='h',
            marker_color=px.colors.sequential.Blues_r,
            text=[f"{v}%" for v in category_skills.values()],
            textposition='auto',
        ))
        
        fig_bar.update_layout(
            title=f"{selected_category} - Proficiency Levels",
            xaxis_title="Proficiency (%)",
            yaxis_title="Skills",
            height=400
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Skills description
        st.markdown(f"### 📝 {selected_category} Expertise")
        
        if selected_category == "Cloud Platforms":
            st.info("Extensive experience across major cloud providers with hands-on expertise in architecting, deploying, and managing scalable cloud solutions.")
        elif selected_category == "DevOps & CI/CD":
            st.info("Deep knowledge of continuous integration and deployment practices, with proven track record in building automated pipelines.")
        elif selected_category == "Containerization":
            st.info("Expert in containerization technologies and orchestration platforms, enabling scalable and resilient application deployments.")
        elif selected_category == "Programming Languages":
            st.info("Versatile programming skills across multiple languages, with focus on automation, backend development, and emerging full-stack capabilities.")
        elif selected_category == "MLOps Tools":
            st.info("Currently developing expertise in MLOps practices and tools to bridge the gap between machine learning and operations.")
    
    with tab3:
        # Radar chart comparing all categories
        categories = list(skills_data.keys())
        avg_proficiencies = [sum(skills.values()) / len(skills) for skills in skills_data.values()]
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=avg_proficiencies,
            theta=categories,
            fill='toself',
            name='Average Proficiency',
            line_color='rgb(102, 126, 234)'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Skills Categories Comparison",
            height=500
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Top skills summary
        st.markdown("### 🏆 Top Skills")
        
        # Flatten all skills and get top 10
        all_skills_flat = []
        for category, skills in skills_data.items():
            for skill, proficiency in skills.items():
                all_skills_flat.append((skill, proficiency, category))
        
        top_skills = sorted(all_skills_flat, key=lambda x: x[1], reverse=True)[:10]
        
        col1, col2 = st.columns(2)
        
        for i, (skill, proficiency, category) in enumerate(top_skills):
            if i < 5:
                with col1:
                    st.markdown(f"**{i+1}. {skill}** ({category})")
                    st.progress(proficiency / 100)
            else:
                with col2:
                    st.markdown(f"**{i+1}. {skill}** ({category})")
                    st.progress(proficiency / 100)

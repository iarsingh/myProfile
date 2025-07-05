import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

def render_career_timeline(work_experience):
    """Render an interactive career timeline"""
    
    # Create timeline data
    timeline_data = []
    for i, job in enumerate(work_experience):
        end_date = job['end_date'] if job['end_date'] else datetime.now()
        duration_days = (end_date - job['start_date']).days
        
        timeline_data.append({
            'Job': f"{job['title']} at {job['company']}",
            'Company': job['company'],
            'Title': job['title'],
            'Start': job['start_date'],
            'End': end_date,
            'Duration': job['duration'],
            'Location': job['location'],
            'Index': i
        })
    
    # Create Gantt chart
    fig = go.Figure()
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe']
    
    for i, job_data in enumerate(timeline_data):
        fig.add_trace(go.Scatter(
            x=[job_data['Start'], job_data['End']],
            y=[i, i],
            mode='lines+markers',
            line=dict(color=colors[i % len(colors)], width=8),
            marker=dict(size=12, color=colors[i % len(colors)]),
            name=job_data['Job'],
            hovertemplate=f"<b>{job_data['Title']}</b><br>" +
                         f"Company: {job_data['Company']}<br>" +
                         f"Duration: {job_data['Duration']}<br>" +
                         f"Location: {job_data['Location']}<extra></extra>"
        ))
    
    fig.update_layout(
        title="Career Journey Timeline",
        xaxis_title="Years",
        yaxis_title="Positions",
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(timeline_data))),
            ticktext=[f"{job['title']}<br>{job['company']}" for job in work_experience]
        ),
        height=400,
        showlegend=False,
        hovermode='closest'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed job descriptions
    st.markdown("### 📋 Detailed Experience")
    
    for job in work_experience:
        with st.expander(f"🏢 {job['title']} at {job['company']} ({job['duration']})"):
            st.markdown(f"**Location:** {job['location']}")
            st.markdown("**Key Responsibilities & Achievements:**")
            
            for desc in job['description']:
                st.markdown(f"• {desc}")
            
            st.markdown("**Technologies & Skills:**")
            skills_html = " ".join([f'<span class="skill-tag">{skill}</span>' for skill in job['skills']])
            st.markdown(f'<div>{skills_html}</div>', unsafe_allow_html=True)
            
            # Calculate experience duration
            end_date = job['end_date'] if job['end_date'] else datetime.now()
            duration_months = ((end_date.year - job['start_date'].year) * 12 + 
                             (end_date.month - job['start_date'].month))
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Duration", f"{duration_months} months")
            with col2:
                st.metric("Skills Used", len(job['skills']))
            with col3:
                status = "Current" if job['end_date'] is None else "Completed"
                st.metric("Status", status)

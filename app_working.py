import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Sports Speed by Atlee Mahorn, Oly",
    page_icon="🏃‍♂️",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .sport-card {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏃‍♂️ Sports Speed by Atlee Mahorn, Oly</h1>
    <h3>Proven Sports Speed System</h3>
    <p>Olympic Training Methodology for High School Athletics</p>
</div>
""", unsafe_allow_html=True)

# Navigation
page = st.sidebar.selectbox("Choose Section", [
    "🏠 Home",
    "🏃‍♂️ Training Builder", 
    "📊 Reports & Charts",
    "🔥 Recovery Heat Map",
    "🎯 Mood & Energy Tracker",
    "🎧 Real-Time Coaching"
])

if page == "🏠 Home":
    st.markdown("## Welcome to Olympic Training Methodology")
    st.markdown("### Professional speed training for high school coaches across 6 sports")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="sport-card">🏈 Football<br>Power & Acceleration</div>', unsafe_allow_html=True)
        st.markdown('<div class="sport-card">⚽ Soccer<br>Speed & Endurance</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="sport-card">🏀 Basketball<br>Agility & Quickness</div>', unsafe_allow_html=True)
        st.markdown('<div class="sport-card">⚾ Baseball<br>Base Running Speed</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="sport-card">🥍 Lacrosse<br>Field Transitions</div>', unsafe_allow_html=True)
        st.markdown('<div class="sport-card">🏃 Track & Field<br>Pure Speed Development</div>', unsafe_allow_html=True)

elif page == "🏃‍♂️ Training Builder":
    st.header("16-Week Training Builder")
    
    sport = st.selectbox("Select Sport", [
        "Football", "Soccer", "Basketball", "Baseball", "Lacrosse", "Track & Field"
    ])
    
    col1, col2 = st.columns(2)
    with col1:
        athlete_name = st.text_input("Athlete Name", "Enter name")
        age = st.number_input("Age", 14, 18, 16)
    with col2:
        position = st.text_input("Position/Event", "Enter position")
        experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Generate 16-Week Plan"):
        st.success(f"16-week {sport} speed training plan generated for {athlete_name}")
        
        phases = ["Base Building", "Strength Development", "Speed Focus", "Competition Peak"]
        for i, phase in enumerate(phases, 1):
            with st.expander(f"Phase {i}: {phase} (Weeks {(i-1)*4+1}-{i*4})"):
                st.write(f"**Focus:** {phase}")
                st.write(f"**Training Days:** 4-5 per week")
                st.write(f"**Key Exercises:** Sport-specific speed and power development")

elif page == "📊 Reports & Charts":
    st.header("Performance Analytics Dashboard")
    
    # Performance Chart
    st.subheader("16-Week Sprint Time Progression")
    weeks = list(range(1, 17))
    sprint_times = [4.8 - (i * 0.02) + np.random.normal(0, 0.02) for i in weeks]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=weeks, 
        y=sprint_times, 
        name='Sprint Time (s)', 
        line=dict(color='#1e40af', width=3),
        mode='lines+markers'
    ))
    
    fig.update_layout(
        title="40m Sprint Time Improvement",
        xaxis_title="Training Week",
        yaxis_title="Time (seconds)",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Multi-sport comparison
    st.subheader("Multi-Sport Performance Comparison")
    sports_data = {
        'Sport': ['Football', 'Soccer', 'Basketball', 'Baseball', 'Lacrosse', 'Track'],
        'Athletes': [32, 28, 24, 20, 16, 22],
        'Avg Improvement': [12.5, 10.8, 15.2, 9.3, 11.7, 18.4]
    }
    
    df = pd.DataFrame(sports_data)
    
    fig2 = px.bar(df, x='Sport', y='Avg Improvement', 
                  title='Average Performance Improvement by Sport (%)',
                  color='Avg Improvement',
                  color_continuous_scale='Blues')
    
    st.plotly_chart(fig2, use_container_width=True)

elif page == "🔥 Recovery Heat Map":
    st.header("Athlete Recovery Monitoring")
    
    # Generate recovery heat map data
    athletes = [f"Athlete {i+1}" for i in range(20)]
    muscle_groups = ['Hamstrings', 'Quadriceps', 'Calves', 'Glutes', 'Core']
    
    recovery_data = []
    for i in range(20):
        row = []
        for j in range(5):
            recovery_score = np.random.uniform(70, 100)
            row.append(recovery_score)
        recovery_data.append(row)
    
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=recovery_data,
        x=muscle_groups,
        y=athletes,
        colorscale='RdYlGn',
        text=[[f"{val:.1f}%" for val in row] for row in recovery_data],
        texttemplate="%{text}",
        textfont={"size": 8}
    ))
    
    fig_heatmap.update_layout(
        title="Real-Time Recovery Status by Muscle Group",
        height=500
    )
    
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Recovery summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Recovery Rate", "87.3%", "2.1%")
    with col2:
        st.metric("Athletes at Risk", "3", "-1")
    with col3:
        st.metric("Ready for Training", "17", "1")

elif page == "🎯 Mood & Energy Tracker":
    st.header("Athlete Mood & Energy Tracking")
    
    # Real-time mood and energy input
    st.subheader("Daily Check-In")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Current Mood**")
        mood_options = ["😊 Excellent", "😐 Good", "😕 Average", "😔 Poor", "😩 Very Poor"]
        current_mood = st.selectbox("How are you feeling today?", mood_options)
        
        st.write("**Energy Level**")
        energy_level = st.slider("Rate your energy (1-10)", 1, 10, 7)
        
        st.write("**Sleep Quality**")
        sleep_quality = st.slider("Rate your sleep quality (1-10)", 1, 10, 8)
        
    with col2:
        st.write("**Motivation Level**")
        motivation = st.slider("Rate your motivation (1-10)", 1, 10, 8)
        
        st.write("**Stress Level**")
        stress_level = st.slider("Rate your stress (1-10)", 1, 10, 3)
        
        st.write("**Physical Readiness**")
        physical_readiness = st.slider("Rate your physical readiness (1-10)", 1, 10, 7)
    
    # Submit mood/energy data
    if st.button("Submit Daily Check-In", type="primary"):
        st.success("Daily check-in recorded! Training recommendations updated.")
        
        # Display personalized recommendations
        st.subheader("Personalized Training Recommendations")
        
        total_score = (energy_level + sleep_quality + motivation + physical_readiness - stress_level) / 4
        
        if total_score >= 7:
            st.success("🟢 **High Performance Day** - Full intensity training recommended")
            st.write("- Complete planned speed sessions")
            st.write("- Focus on technique and power development")
            st.write("- Consider adding extra acceleration work")
        elif total_score >= 5:
            st.warning("🟡 **Moderate Performance Day** - Adjust training intensity")
            st.write("- Reduce training volume by 20%")
            st.write("- Focus on technique over intensity")
            st.write("- Include extra recovery work")
        else:
            st.error("🔴 **Low Performance Day** - Recovery focused session")
            st.write("- Light movement and mobility work only")
            st.write("- Focus on recovery strategies")
            st.write("- Consider rest day or active recovery")
    
    # Mood & Energy Trend Chart
    st.subheader("7-Day Mood & Energy Trends")
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    mood_scores = [8, 7, 6, 8, 9, 7, 8]
    energy_scores = [7, 8, 6, 7, 9, 8, 7]
    
    fig_trends = go.Figure()
    fig_trends.add_trace(go.Scatter(
        x=days, y=mood_scores, name='Mood Score', 
        line=dict(color='#1e40af', width=3), mode='lines+markers'
    ))
    fig_trends.add_trace(go.Scatter(
        x=days, y=energy_scores, name='Energy Level', 
        line=dict(color='#3b82f6', width=3), mode='lines+markers'
    ))
    
    fig_trends.update_layout(
        title="Weekly Mood & Energy Tracking",
        xaxis_title="Day",
        yaxis_title="Score (1-10)",
        height=400
    )
    
    st.plotly_chart(fig_trends, use_container_width=True)
    
    # Team mood overview
    st.subheader("Team Mood Overview")
    team_mood_data = {
        'Athlete': [f'Athlete {i+1}' for i in range(12)],
        'Mood': [8, 7, 9, 6, 8, 7, 9, 8, 6, 7, 8, 9],
        'Energy': [7, 8, 9, 5, 7, 8, 9, 7, 6, 8, 7, 9],
        'Status': ['Ready', 'Ready', 'Peak', 'Monitor', 'Ready', 'Ready', 'Peak', 'Ready', 'Monitor', 'Ready', 'Ready', 'Peak']
    }
    
    mood_df = pd.DataFrame(team_mood_data)
    st.dataframe(mood_df, use_container_width=True)

elif page == "🎧 Real-Time Coaching":
    st.header("Real-Time Coaching Feedback Overlay")
    
    # Coaching mode selector
    coaching_mode = st.selectbox("Select Coaching Mode", [
        "Live Training Session",
        "Video Analysis",
        "Performance Review",
        "Technique Coaching"
    ])
    
    if coaching_mode == "Live Training Session":
        st.subheader("🔴 LIVE: Training Session Active")
        
        # Real-time metrics display
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Current Athlete", "John Smith", "")
            st.metric("Sprint Time", "4.32s", "-0.08s")
        
        with col2:
            st.metric("Heart Rate", "165 bpm", "12 bpm")
            st.metric("Recovery Time", "2:15", "")
        
        with col3:
            st.metric("Session Progress", "65%", "")
            st.metric("Reps Completed", "8/12", "")
        
        with col4:
            st.metric("Intensity Level", "87%", "5%")
            st.metric("Technique Score", "8.2/10", "0.3")
        
        # Real-time coaching alerts
        st.subheader("⚡ Real-Time Coaching Alerts")
        
        alerts = [
            {"type": "success", "message": "🟢 Excellent acceleration phase - maintain form"},
            {"type": "warning", "message": "🟡 Slight decrease in stride frequency - focus on quick turnover"},
            {"type": "info", "message": "🔵 Heart rate optimal - ready for next rep"},
            {"type": "error", "message": "🔴 Form breakdown detected - extend recovery time"}
        ]
        
        for alert in alerts:
            if alert["type"] == "success":
                st.success(alert["message"])
            elif alert["type"] == "warning":
                st.warning(alert["message"])
            elif alert["type"] == "info":
                st.info(alert["message"])
            elif alert["type"] == "error":
                st.error(alert["message"])
        
        # Coaching feedback panel
        st.subheader("💬 Coaching Feedback Panel")
        
        feedback_text = st.text_area("Enter real-time coaching feedback:", 
                                   "Great start position! Focus on driving through the first 10m...")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Send to Athlete", type="primary"):
                st.success("Feedback sent to athlete's device!")
        
        with col2:
            if st.button("Save to Session Notes"):
                st.info("Feedback saved to session notes")
    
    elif coaching_mode == "Video Analysis":
        st.subheader("🎥 Video Analysis Mode")
        
        st.write("**Upload Training Video for Analysis**")
        uploaded_file = st.file_uploader("Choose video file", type=['mp4', 'mov', 'avi'])
        
        if uploaded_file is not None:
            st.video(uploaded_file)
            
            # Analysis tools
            st.subheader("Analysis Tools")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Time Markers**")
                start_time = st.time_input("Start Analysis", value=None)
                end_time = st.time_input("End Analysis", value=None)
                
                if st.button("Analyze Sprint Mechanics"):
                    st.success("Analyzing sprint mechanics...")
                    
                    # Mock analysis results
                    st.write("**Analysis Results:**")
                    st.write("- Acceleration phase: 0-30m - Excellent drive angle")
                    st.write("- Max velocity phase: 30-60m - Optimal stride length")
                    st.write("- Technique score: 8.7/10")
            
            with col2:
                st.write("**Annotation Tools**")
                annotation = st.text_area("Add coaching notes:")
                
                if st.button("Save Analysis"):
                    st.info("Video analysis saved to athlete profile")
    
    elif coaching_mode == "Performance Review":
        st.subheader("📊 Performance Review Session")
        
        # Performance metrics
        st.write("**Session Performance Summary**")
        
        performance_data = {
            'Metric': ['40m Sprint', '60m Sprint', 'Flying 20m', 'Standing Long Jump', 'Vertical Jump'],
            'Today': ['4.32s', '6.85s', '2.15s', '2.85m', '68cm'],
            'Personal Best': ['4.28s', '6.79s', '2.10s', '2.90m', '72cm'],
            'Improvement': ['-0.04s', '-0.06s', '-0.05s', '+0.05m', '+4cm']
        }
        
        perf_df = pd.DataFrame(performance_data)
        st.dataframe(perf_df, use_container_width=True)
        
        # Coaching recommendations
        st.subheader("🎯 Coaching Recommendations")
        
        recommendations = st.text_area("Session coaching recommendations:", 
                                     "Focus on maintaining acceleration through 40m mark. "
                                     "Excellent progress in flying 20m splits. "
                                     "Continue working on reactive strength for jumping improvements.")
        
        if st.button("Save Performance Review"):
            st.success("Performance review saved to athlete profile")
    
    elif coaching_mode == "Technique Coaching":
        st.subheader("🏃 Technique Coaching Session")
        
        technique_focus = st.selectbox("Select Technique Focus", [
            "Start Position & First Step",
            "Acceleration Mechanics",
            "Maximum Velocity Sprint",
            "Arm Action & Rhythm",
            "Deceleration & Finish"
        ])
        
        st.write(f"**Coaching Focus: {technique_focus}**")
        
        # Technique-specific coaching points
        if technique_focus == "Start Position & First Step":
            st.write("**Key Coaching Points:**")
            st.write("- Set position: 45-degree shin angle")
            st.write("- First step: Drive through the ground")
            st.write("- Body position: Maintain forward lean")
            
        elif technique_focus == "Acceleration Mechanics":
            st.write("**Key Coaching Points:**")
            st.write("- Ground contact: Push behind center of mass")
            st.write("- Arm action: Powerful drive from shoulders")
            st.write("- Posture: Gradual rise to upright position")
        
        # Real-time technique feedback
        technique_feedback = st.text_area("Real-time technique feedback:", 
                                        "Good drive angle on start. Focus on maintaining forward lean longer...")
        
        if st.button("Send Technique Cues"):
            st.success("Technique cues sent to athlete!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #1e40af; font-weight: bold;">
    Sports Speed by Atlee Mahorn, Olympic Methodology<br>
    Professional Training System for High School Athletics
</div>
""", unsafe_allow_html=True)
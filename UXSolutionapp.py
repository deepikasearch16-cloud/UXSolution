# app.py
import streamlit as st

st.set_page_config(page_title="Ultimatix AI Solutions Portal", layout="wide")
st.title("Ultimatix Innovation – AI Project Solutions Dashboard")
st.write("Ready-made AI solutions to accelerate TCS projects and improve delivery excellence.\n---")

# ---------- Navigation ----------
solutions = [
    "Project Planning",
    "Sprint Planning",
    "Compliance Checker",
    "Project Reporting",
    "RFP Assistant",
    "Contract Assistant",
    "Skill Matcher",
    "Risk Predictor",
    "Learning Recommender",
    "Collaboration Assistant"
]

selected_solution = st.sidebar.radio("Choose AI Solution", solutions)

# ---------- Solutions ----------
if selected_solution == "Project Planning":
    st.header("📅 Project Planning Demo")
    project_type = st.text_input("Project Type", value="Web App Development")
    project_size = st.selectbox("Project Size", ["Small", "Medium", "Large"], index=1)
    st.write("Suggested Milestones:\n1. Requirements Gathering\n2. Design Phase\n3. Development Phase\n4. Testing Phase\n5. Delivery & Handover")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Project Type, Project Size, Start Date, Team Size, Skills, Duration/Budget  
        **AI Outputs:** Suggested milestones, timeline, Gantt chart  
        **Benefits:** Reduces manual planning, ensures consistent timelines, improves delivery accuracy
        """)

elif selected_solution == "Sprint Planning":
    st.header("🏃‍♂️ Sprint Planning Demo")
    tasks = st.text_area("Tasks", value="Login Module\nPayment Integration\nDashboard UI")
    team_members = st.text_area("Team Members", value="Alice\nBob\nCharlie")
    st.write("Task Assignments:\nAlice → Login Module\nBob → Payment Integration\nCharlie → Dashboard UI\nSprint Duration: 2 Weeks")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Task List, Team Members, Sprint Duration, Task Dependencies  
        **AI Outputs:** Sprint assignments, task allocation, sprint schedule  
        **Benefits:** Saves planning time, optimizes team utilization, prevents overload
        """)

elif selected_solution == "Compliance Checker":
    st.header("✅ Compliance Checker Demo")
    st.write("Security Audit: ✅ Completed\nCode Review: ❌ Pending\nClient Approval: ✅ Completed")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Compliance Checklist, Project Phase, Supporting Documents  
        **AI Outputs:** Compliance status, flagged issues  
        **Benefits:** Ensures project compliance, reduces manual checks
        """)

elif selected_solution == "Project Reporting":
    st.header("📊 Project Reporting Demo")
    st.write("Sample Metrics Dashboard:\n- Completion: 65%\n- Pending Tasks: 12\n- Delayed Tasks: 3\n- Budget Utilization: 70%\n[Charts Placeholder]")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Project Metrics, Team Member Status, Issue Logs  
        **AI Outputs:** Visual dashboards, summary reports  
        **Benefits:** Provides instant reporting, enhances decision-making
        """)

elif selected_solution == "RFP Assistant":
    st.header("📝 RFP Assistant Demo")
    st.write("Proposal Draft Preview:\n1. Executive Summary\n2. Project Scope\n3. Proposed Solution\n4. Timeline & Milestones\n5. Cost Estimate")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Client Details, Project Scope, Timeline, Budget, Requirements  
        **AI Outputs:** Drafted proposal, highlighted gaps  
        **Benefits:** Accelerates RFP creation, reduces errors
        """)

elif selected_solution == "Contract Assistant":
    st.header("📜 Contract Assistant Demo")
    st.write("Contract Draft Preview:\nClause 1: Scope of Services\nClause 2: Payment Terms\nClause 3: Confidentiality\nClause 4: Termination")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Contract Type, Scope of Work, Payment Terms, Deliverables  
        **AI Outputs:** Draft contract with suggested clauses, risk alerts  
        **Benefits:** Saves time, ensures standardized contracts, reduces risk
        """)

elif selected_solution == "Skill Matcher":
    st.header("👥 Skill Matcher Demo")
    st.write("Required Skills: Python, SQL, Cloud\nTeam Members and Skills: Alice → Python, SQL | Bob → Java, Cloud | Charlie → Python, Cloud\nRecommended Team Composition: Alice → Python, SQL | Charlie → Cloud")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Required Skills, Team Members, Availability, Experience  
        **AI Outputs:** Recommended team composition  
        **Benefits:** Optimizes team assignment, improves project delivery
        """)

elif selected_solution == "Risk Predictor":
    st.header("⚠️ Risk Predictor Demo")
    st.write("Predicted Risks:\n- Schedule Delay: Medium\n- Budget Overrun: Low\n- Resource Risk: High")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Project Duration, Budget, Team Size, Complexity, Historical Data  
        **AI Outputs:** Risk levels for schedule, budget, resources  
        **Benefits:** Early warning for risks, allows proactive mitigation
        """)

elif selected_solution == "Learning Recommender":
    st.header("🎓 Learning Recommender Demo")
    st.write("Suggested Learning Paths:\n- Advanced Project Management\n- ERP Deployment Best Practices\n- Agile Methodologies")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Associate Role, Project Type / Tech Stack, Current Skills  
        **AI Outputs:** Recommended training, courses, certifications  
        **Benefits:** Upskilling for projects, better resource readiness
        """)

elif selected_solution == "Collaboration Assistant":
    st.header("💬 Collaboration Assistant Demo")
    st.write("Pending Approvals / Updates Summary:\n- Timesheet Approval → Pending\n- Design Document Review → Pending\nReminders Sent to Respective Team Members ✅")
    
    with st.expander("ℹ️ Info: Inputs, Outputs & Benefits"):
        st.markdown("""
        **Required Inputs:** Pending Approvals / Updates, Task Owners, Deadlines  
        **AI Outputs:** Summary, reminders, nudges  
        **Benefits:** Improves team collaboration, reduces delays
        """)

# ---------- Footer ----------
st.markdown("---")
st.markdown("Demo by: **Ultimatix Innovation**")

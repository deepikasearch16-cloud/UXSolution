import streamlit as st

st.set_page_config(page_title="Ultimatix AI Solutions Portal", layout="wide")
st.title("Ultimatix Innovation – AI Project Solutions Dashboard")
st.write("Interactive AI solutions demo for TCS projects.\n---")

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

# ---------- Project Planning ----------
if selected_solution == "Project Planning":
    st.header("📅 Project Planning – Real-Time Demo")
    project_name = st.text_input("Project Name", value="Web App Development")
    project_size = st.selectbox("Project Size", ["Small", "Medium", "Large"], index=1)
    team_size = st.number_input("Team Size", min_value=1, max_value=20, value=5)
    estimated_duration = st.number_input("Estimated Duration (weeks)", min_value=1, max_value=52, value=12)

    if st.button("Generate Project Plan"):
        milestones = []
        if project_size == "Small":
            milestones = [
                "1. Requirements Gathering (1 week)",
                "2. Design Phase (1 week)",
                "3. Development Phase (4 weeks)",
                "4. Testing & QA (1 week)",
                "5. Delivery & Handover (1 week)"
            ]
        elif project_size == "Medium":
            milestones = [
                "1. Requirements Gathering (2 weeks)",
                "2. Design Phase (2 weeks)",
                "3. Development Phase (6 weeks)",
                "4. Testing & QA (2 weeks)",
                "5. Delivery & Handover (2 weeks)"
            ]
        else:
            milestones = [
                "1. Requirements Gathering (3 weeks)",
                "2. Design Phase (3 weeks)",
                "3. Development Phase (12 weeks)",
                "4. Testing & QA (3 weeks)",
                "5. Delivery & Handover (3 weeks)"
            ]
        st.subheader(f"Suggested Milestones for {project_name}:")
        for m in milestones:
            st.write(m)

# ---------- Sprint Planning ----------
elif selected_solution == "Sprint Planning":
    st.header("🏃‍♂️ Sprint Planning – Real-Time Demo")
    tasks = st.text_area("Task Backlog (one per line)", value="Login Module\nPayment Integration\nDashboard UI")
    team_members = st.text_area("Team Members (one per line)", value="Alice\nBob\nCharlie")
    sprint_duration = st.number_input("Sprint Duration (weeks)", min_value=1, max_value=4, value=2)

    if st.button("Generate Sprint Plan"):
        task_list = tasks.split("\n")
        members = team_members.split("\n")
        st.subheader("Task Assignments:")
        for i, task in enumerate(task_list):
            assignee = members[i % len(members)]
            st.write(f"{assignee} → {task}")
        st.write(f"Sprint Duration: {sprint_duration} weeks")

# ---------- Collaboration Assistant ----------
elif selected_solution == "Collaboration Assistant":
    st.header("💬 Collaboration Assistant – Real-Time Demo")
    pending_tasks = st.text_area("Pending Approvals/Updates (one per line)", value="Timesheet Approval\nDesign Document Review")
    owners = st.text_area("Task Owners (one per line, same order)", value="Alice\nBob")

    if st.button("Generate Reminders"):
        tasks = pending_tasks.split("\n")
        owners_list = owners.split("\n")
        st.subheader("Reminders Sent:")
        for i, task in enumerate(tasks):
            owner = owners_list[i % len(owners_list)]
            st.write(f"{task} → Reminder sent to {owner}")

# ---------- Learning Recommender ----------
elif selected_solution == "Learning Recommender":
    st.header("🎓 Learning Recommender – Real-Time Demo")
    role = st.text_input("Associate Role", value="Business Analyst")
    project_type = st.text_input("Project Type/Tech Stack", value="ERP Implementation")
    current_skills = st.text_area("Current Skills (comma separated)", value="Excel, SQL")

    if st.button("Generate Learning Paths"):
        st.subheader("Recommended Learning Paths:")
        if "SQL" in current_skills:
            st.write("- Advanced SQL & Data Modeling")
        if "Excel" in current_skills:
            st.write("- Advanced Excel for Project Management")
        st.write("- Agile Project Management Certification")
        st.write("- ERP Best Practices Training")

# ---------- Other solutions (Static Pre-Filled for Demo) ----------
else:
    st.write("Static demo outputs for selected solution. Pre-filled to showcase AI capabilities.")

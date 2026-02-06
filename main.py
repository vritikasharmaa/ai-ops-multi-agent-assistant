import streamlit as st
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import VerifierAgent


st.title("🤖 AI Ops Multi-Agent Assistant")
st.markdown("Plan and execute DevOps tasks using AI agents")

task = st.text_input("Enter DevOps Task")

if st.button("Run Agent Workflow") and task:

    with st.spinner("Planner Agent thinking..."):
        plan = create_plan(task)

    st.success("Plan Generated")

    st.subheader("📋 Generated Plan")
    st.json(plan)

    with st.spinner("Executor Agent running tools..."):
        results, logs = execute_plan(plan)

    st.subheader("⚙ Execution Results")
    st.json(results)

    st.subheader("🧠 Agent Reasoning Logs")
    for log in logs:
        st.write("•", log)

    # ✅ Verifier Agent (MANDATORY)
    verifier = VerifierAgent()
    status = verifier.verify(results)

    st.subheader("✅ Verifier Output")
    st.json({
    "status": "success" if "successful" in status.lower() else "failed",
    "message": status
     })



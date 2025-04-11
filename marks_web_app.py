import streamlit as st

# Page configuration
st.set_page_config(page_title="Marks to Career Path", page_icon="🎓", layout="centered")

# App title and subtitle
st.title("🎓 Marks to Career Path")
st.markdown("Enter your subject marks and get career suggestions based on your strengths.")

# Student Info
student_name = st.text_input("Enter your name")

# Subject list
subjects = ["Math", "Science", "English", "History", "Geography", "Computer Science"]
marks = {}

st.markdown("### Enter your marks:")

# Collect marks
for subject in subjects:
    marks[subject] = st.number_input(f"{subject}", min_value=0, max_value=100, step=1)

# On submit
if st.button("Submit"):
    st.success(f"Thanks {student_name or 'Student'}! Your marks have been recorded.")

    st.markdown("### Your Entered Marks:")
    for subject, score in marks.items():
        st.write(f"**{subject}**: {score}")

    # Career guidance logic
    st.markdown("### Career Path Suggestions:")

    if all(score >= 85 for score in marks.values()):
        st.info("Excellent performance across subjects! You're well-suited for high-achievement careers like **Medicine, Engineering, Data Science, or Research.**")
    elif marks["Computer Science"] >= 80:
        st.info("Great job in Computer Science! You might enjoy careers in **Software Development, AI, Cybersecurity, or Web Development.**")
    elif marks["Math"] >= 80 and marks["Science"] >= 80:
        st.info("Strong Math and Science skills suggest paths like **Engineering, Physics, Data Analytics, or Architecture.**")
    elif marks["English"] >= 85:
        st.info("Your English is impressive! Consider **Journalism, Law, Content Writing, or Education.**")
    elif marks["History"] >= 80 or marks["Geography"] >= 80:
        st.info("Strong in humanities? Think about **Civil Services, Archaeology, Teaching, or Law.**")
    else:
        st.warning("Keep working hard and exploring! Every mark is a step forward. Explore your interests and build skills over time.")

    # Motivational Quote
    st.markdown("> *“Your future is created by what you do today, not tomorrow.” — Robert Kiyosaki*")
    

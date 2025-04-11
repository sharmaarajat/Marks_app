import streamlit as st

st.set_page_config(page_title="Marks Entry Form", page_icon="✏️", layout="centered")

st.title("School Marks Entry Form")

subjects = ["Math", "Science", "English", "History", "Geography", "Computer Science"]
marks = {}

st.markdown("### Enter marks for each subject:")

for subject in subjects:
    marks[subject] = st.number_input(f"{subject}", min_value=0, max_value=100, step=1)

if st.button("Submit"):
    st.success("Marks Submitted Successfully!")
    st.markdown("### Entered Marks:")
    for subject, score in marks.items():
        st.write(f"{subject}: {score}")

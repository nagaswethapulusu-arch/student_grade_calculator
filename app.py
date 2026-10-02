import streamlit as st
import pandas as pd


def get_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid"
    elif mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


st.title("Student Grade Calculator")

st.header("Check a single mark")
mark = st.number_input("Enter marks", min_value=-100, max_value=200, value=75, step=1)
grade = get_grade(mark)
if grade == "Invalid":
    st.error("Invalid marks. Marks must be between 0 and 100.")
else:
    st.success(f"Grade: {grade}")

st.header("Class results")
students = ["Asha", "Ravi", "Meena", "Kiran", "Swetha", "Harsh", "Rupesh", "Akhil", "Divya", "Teja"]
marks = [78, 85, 62, 90, 71, 89, 70, 65, 45, 105]
df = pd.DataFrame({
    "Student": students,
    "Marks": marks,
    "Grade": [get_grade(m) for m in marks],
})
st.table(df)

st.header("Grading scale")
st.table(pd.DataFrame({
    "Marks": ["90 - 100", "80 - 89", "70 - 79", "60 - 69", "Below 60", "< 0 or > 100"],
    "Grade": ["A", "B", "C", "D", "F", "Invalid"],
}))

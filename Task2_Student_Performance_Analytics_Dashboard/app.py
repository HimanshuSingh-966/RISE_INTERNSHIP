import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Config
st.set_page_config(page_title="📊 Student Performance Dashboard", layout="wide")
sns.set(style="whitegrid")

# Title
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🎓 Student Performance Analytics</h1>
    <p style='text-align: center;'>Early intervention dashboard for identifying at-risk students</p>
""", unsafe_allow_html=True)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Task2_Student_Performance_Analytics_Dashboard/student-por.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filter Data")
min_grade, max_grade = st.sidebar.slider("Filter by Final Grade (G3)", 0, 20, (0, 20))
max_absences = st.sidebar.slider("Max Absences", 0, int(df['absences'].max()), int(df['absences'].max()))
studytime_options = sorted(df['studytime'].unique())
selected_studytime = st.sidebar.multiselect("Select Study Time Levels", studytime_options, default=studytime_options)

# Apply filters
filtered_df = df[(df['G3'] >= min_grade) & (df['G3'] <= max_grade)]
filtered_df = filtered_df[filtered_df['absences'] <= max_absences]
filtered_df = filtered_df[filtered_df['studytime'].isin(selected_studytime)]

# KPI Section
st.markdown("### 📈 Key Metrics")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Students", len(filtered_df))
k2.metric("Average Final Grade", float(round(filtered_df['G3'].mean(), 2)))
k3.metric("Avg. Absences", float(round(filtered_df['absences'].mean(), 1)))
k4.metric("Avg. Study Time", float(round(filtered_df['studytime'].mean(), 1)))

# Plot Section in Grid Layout
st.markdown("### 📊 Visual Insights")
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)
row3_col1, row3_col2 = st.columns(2)

# Grade Distribution
with row1_col1:
    fig1, ax1 = plt.subplots()
    sns.histplot(data=filtered_df, x='G3', kde=True, bins=20, color="skyblue", ax=ax1)
    ax1.set_title("Distribution of Final Grades (G3)")
    ax1.set_xlabel("Final Grade")
    ax1.set_ylabel("Number of Students")
    st.pyplot(fig1)

# Correlation Matrix
with row1_col2:
    corr_cols = ['G1', 'G2', 'G3', 'absences', 'studytime', 'failures']
    valid_cols = [col for col in corr_cols if col in filtered_df.columns]
    if len(valid_cols) >= 2:
        corr_data = filtered_df[valid_cols].corr()
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr_data, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax2)
        ax2.set_title("Correlation between Student Factors")
        st.pyplot(fig2)

# Absences vs Grade
with row2_col1:
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='absences', y='G3', hue='studytime', palette='coolwarm', ax=ax3)
    ax3.set_title("Impact of Absences on G3")
    ax3.set_xlabel("Absences")
    ax3.set_ylabel("Final Grade")
    st.pyplot(fig3)

# Study Time vs Grade
with row2_col2:
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=filtered_df, x='studytime', y='G3', hue='studytime', palette='Purples', ax=ax4, legend=False)
    ax4.set_title("Study Time vs Final Grade")
    ax4.set_xlabel("Study Time")
    ax4.set_ylabel("Final Grade")
    st.pyplot(fig4)

# Age vs G3
with row3_col1:
    if 'age' in filtered_df.columns:
        fig5, ax5 = plt.subplots()
        sns.boxplot(data=filtered_df, x='age', y='G3', hue='age', palette='Blues', ax=ax5, legend=False)
        ax5.set_title("Age vs Final Grade")
        ax5.set_xlabel("Age")
        ax5.set_ylabel("Final Grade")
        st.pyplot(fig5)

# Failures vs G3
with row3_col2:
    if 'failures' in filtered_df.columns:
        fig6, ax6 = plt.subplots()
        sns.boxplot(data=filtered_df, x='failures', y='G3', hue='failures', palette='Reds', ax=ax6, legend=False)
        ax6.set_title("Failures vs Final Grade")
        ax6.set_xlabel("Past Class Failures")
        ax6.set_ylabel("Final Grade")
        st.pyplot(fig6)

# Gender vs G3
st.markdown("### 🚻 Gender vs Final Grade")
if 'sex' in filtered_df.columns:
    fig7, ax7 = plt.subplots()
    sns.boxplot(data=filtered_df, x='sex', y='G3', hue='sex', palette='Greens', ax=ax7, legend=False)
    ax7.set_title("Gender vs Final Grade")
    ax7.set_xlabel("Gender")
    ax7.set_ylabel("Final Grade")
    st.pyplot(fig7)

# Top and Bottom Performers with IDs
st.markdown("### 🏆 Top & Struggling Students")
id_cols = ['school'] if 'school' in filtered_df.columns else []

filtered_df = filtered_df.reset_index()
top_students = filtered_df.sort_values(by='G3', ascending=False).head(5)[id_cols + ['index', 'G1', 'G2', 'G3', 'absences', 'studytime']]
bottom_students = filtered_df.sort_values(by='G3', ascending=True).head(5)[id_cols + ['index', 'G1', 'G2', 'G3', 'absences', 'studytime']]

c1, c2 = st.columns(2)
with c1:
    st.write("**Top Performers**")
    st.dataframe(top_students.rename(columns={'index': 'Student ID'}))
with c2:
    st.write("**Struggling Students**")
    st.dataframe(bottom_students.rename(columns={'index': 'Student ID'}))

# Insights
st.markdown("### 💡 Insights & Suggestions")
st.info("- Students with low study time and high absences are more likely to score below average.")
st.info("- G1 and G2 are highly correlated with final performance (G3). Early scores can predict final success.")
st.info("- Consider interventions for students below grade 10 or with more than 10 absences.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Internship Project | Tamizhan Skills - RISE Program</p>", unsafe_allow_html=True)

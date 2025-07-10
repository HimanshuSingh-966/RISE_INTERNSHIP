# 🎓 Student Performance Analytics Dashboard
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task2_Student_Performance_Analytics_Dashboard)

This project is an interactive web dashboard built with Streamlit to analyze student performance data. The primary goal is to provide educators and administrators with a tool for early intervention by identifying students who may be at risk. The dashboard visualizes various factors influencing student grades, such as attendance, study time, and past academic performance.

The application uses student performance data from a Portuguese language course, contained in `student-por.csv`.

## 📈 Features

*   **Dynamic Data Filtering:** Interactively filter the student data by:
    *   Final Grade Range (G3)
    *   Maximum Number of Absences
    *   Weekly Study Time
*   **Key Metrics:** An overview panel displaying key performance indicators (KPIs) for the selected cohort:
    *   Total Students
    *   Average Final Grade
    *   Average Absences
    *   Average Study Time
*   **Comprehensive Visualizations:** A suite of plots to uncover insights from the data:
    *   **Distribution of Final Grades:** Histogram showing the overall performance of students.
    *   **Correlation Matrix:** Heatmap revealing the relationships between grades (G1, G2, G3), absences, study time, and failures.
    *   **Impact of Absences on Grades:** Scatter plot illustrating how absences affect final grades.
    *   **Study Time vs. Final Grade:** Box plot comparing performance across different study time levels.
    *   **Age, Failures & Gender Analysis:** Box plots showing grade distributions based on student age, past failures, and gender.
*   **Student Identification Lists:**
    *   **Top Performers:** A table listing the top 5 students based on final grades.
    *   **Struggling Students:** A table highlighting the 5 students with the lowest final grades, enabling targeted intervention.
*   **Actionable Insights:** A dedicated section providing suggestions based on the analysis, such as prioritizing students with high absences or low early-term grades (G1, G2).

## 🛠️ Technologies Used

*   Python
*   Streamlit
*   Pandas
*   Seaborn
*   Matplotlib

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/himanshusingh-966/rise_internship.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd rise_internship/Task2_Student_Performance_Analytics_Dashboard
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install streamlit pandas seaborn matplotlib
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

5.  Open your web browser and navigate to the local URL provided by Streamlit (e.g., `http://localhost:8501`).
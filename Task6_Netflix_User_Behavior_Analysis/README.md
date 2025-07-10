# 🎬 Netflix User Behavior Analysis Dashboard
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task6_Netflix_User_Behavior_Analysis)

This project provides an interactive dashboard to analyze and visualize personal Netflix user behavior. It processes raw data from a Netflix account takeout, merges it with a broader Netflix titles dataset, and presents the insights through a web application built with Streamlit.

## 🚀 Features

The interactive dashboard allows you to explore your viewing habits with the following features:

*   **Key Metrics:** Get a quick overview with statistics like total watch time in hours, unique titles watched, and the total number of viewing sessions.
*   **Interactive Filters:** Dynamically filter the data by user profile and year to narrow down the analysis.
*   **Top Watched Titles:** A bar chart showcasing the most frequently watched movies and shows.
*   **Genre Distribution:** See which genres you watch the most.
*   **Viewing Patterns:**
    *   **By Day:** A count plot showing viewing activity across the days of the week.
    *   **By Hour:** A histogram revealing the most common hours of the day for watching content.
*   **Country-wise Viewership:** A breakdown of the top countries of origin for the content you've watched.

## 📊 Data

The analysis is performed on a merged dataset created from two primary sources:

1.  **Personal Netflix Data:** Exported from a user's account settings, located in the `dataset_processing/` directory. This includes:
    *   `All_ViewingActivity.csv`
    *   `All_Profiles.csv`
    *   `All_Devices.csv`
    *   And other behavioral data.
2.  **Netflix Titles Dataset:** A public dataset (`netflix_titles.csv`) containing metadata about shows and movies available on Netflix, such as genre and country of production.

The `dataset_processing/processing.ipynb` notebook details the steps for cleaning, processing, and merging these sources into the final `netflix_behavior_merged.csv` file, which powers the dashboard.

## 🛠️ How to Run Locally

To run the dashboard on your own machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/himanshusingh-966/rise_internship.git
    cd rise_internship/Task6_Netflix_User_Behavior_Analysis
    ```

2.  **Install the required Python libraries:**
    ```sh
    pip install streamlit pandas seaborn matplotlib
    ```

3.  **Run the Streamlit application:**
    ```sh
    streamlit run app.py
    ```

4.  The dashboard will automatically open in a new tab in your web browser.
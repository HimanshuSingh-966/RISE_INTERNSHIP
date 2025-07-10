# 🎬 Netflix User Behavior Analysis Dashboard
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task6_Netflix_User_Behavior_Analysis)

This project provides an interactive dashboard to analyze and visualize personal Netflix user behavior. It processes raw data from a Netflix account takeout, merges it with a broader Netflix titles dataset, and presents the insights through a web application built with Streamlit.

## 🚀 Live Application

You can access and interact with the live dashboard here:
[https://riseinternship-xnvrrtq5g3vupjy45mgz8c.streamlit.app/](https://riseinternship-xnvrrtq5g3vupjy45mgz8c.streamlit.app/)

## 🚀 Features

The interactive dashboard allows you to explore your viewing habits with the following features:

* **Key Metrics:** Get a quick overview with statistics like total watch time in hours, unique titles watched, and the total number of viewing sessions.
* **Interactive Filters:** Dynamically filter the data by user profile and year to narrow down the analysis.
* **Top Watched Titles:** A bar chart showcasing the most frequently watched movies and shows.
* **Genre Distribution:** See which genres you watch the most.
* **Viewing Patterns:**
    * **By Day:** A count plot showing viewing activity across the days of the week.
    * **By Hour:** A histogram revealing the most common hours of the day for watching content.
* **Country-wise Viewership:** A breakdown of the top countries of origin for the content you've watched.

## 📊 Data

The analysis is performed on a merged dataset created from two primary sources:

1.  **Personal Netflix Data:** Exported from a user's account settings, located in the `dataset_processing/` directory. This includes:
    * `All_ViewingActivity.csv`
    * `All_Profiles.csv`
    * `All_Devices.csv`
    * And other behavioral data.
2.  **Netflix Titles Dataset:** A public dataset (`netflix_titles.csv`) containing metadata about shows and movies available on Netflix, such as genre and country of production.

The `dataset_processing/processing.ipynb` notebook details the steps for cleaning, processing, and merging these sources into the final `netflix_behavior_merged.csv` file, which powers the dashboard.

## 🛠️ How to Run Locally

To run the dashboard on your own machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/himanshusingh-966/rise_internship.git](https://github.com/himanshusingh-966/rise_internship.git)
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

## ✨ Dashboard Output Visualizations

Here are some screenshots from the interactive Netflix User Behavior Analysis Dashboard:

### 1. Dashboard Overview and Key Metrics
![Dashboard Overview and Key Metrics](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140253.png)
This image shows the main dashboard layout, including interactive filters for user profile and year, along with key metrics like total watch time and unique titles watched.

### 2. Top Watched Titles
![Top Watched Titles](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140304.png)
A bar chart displaying the most frequently watched movies and shows, indicating popular content.

### 3. Genre Distribution
![Genre Distribution](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140316.png)
A visualization (likely a bar or pie chart) showing the distribution of watched content across different genres.

### 4. Viewing Activity by Day of the Week
![Viewing Activity by Day of the Week](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140329.png)
A plot (likely a count plot) illustrating viewing activity across the days of the week, revealing preferred watching days.

### 5. Viewing Activity by Hour of the Day
![Viewing Activity by Hour of the Day](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140342.png)
A histogram or bar chart showing the distribution of viewing activity across different hours of the day, highlighting peak viewing times.

### 6. Country-wise Viewership
![Country-wise Viewership](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task6_Netflix_User_Behavior_Analysis/images/Screenshot%202025-07-10%20140353.png)
A visualization providing a breakdown of the top countries of origin for the content that has been watched.

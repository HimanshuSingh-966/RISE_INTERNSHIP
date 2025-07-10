# COVID-19 Global Data Analysis Dashboard

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task4_COVID_19_Data_Analysis)

## Overview

This repository contains an interactive web application built with Streamlit for visualizing and analyzing global COVID-19 data. The dashboard provides a visual narrative of the pandemic's spread, recovery trends, and mortality rates across various countries and WHO regions.

## 🚀 Live Application

You can access and interact with the live dashboard here:
[https://riseinternship-32phln3gr3iffqdzmrerer.streamlit.app/](https://riseinternship-32phln3gr3iffqdzmrerer.streamlit.app/)

## Features

The dashboard offers a range of interactive features and visualizations:

* **Interactive Filters**:
    * Filter data by WHO Region.
    * Filter data by specific countries within a selected region.
    * Sort visualizations by case type: `Confirmed`, `Deaths`, `Recovered`, or `Active`.
    * Filter countries based on a dynamic range of confirmed cases.

* **Key Visualizations**:
    * **Top 10 Countries**: A bar chart displaying the top 10 countries based on the selected case type.
    * **Comparative Statistics**: A stacked horizontal bar chart comparing confirmed, deaths, recovered, and active cases for the top 15 countries.
    * **Mortality and Recovery Rates**: A heatmap showing `Deaths / 100 Cases`, `Recovered / 100 Cases`, and `Deaths / 100 Recovered` for the top 20 countries.
    * **Weekly Growth Trends**: Side-by-side bar charts illustrating the weekly percentage increase and absolute change in cases for the top 10 countries.
    * **WHO Region Summary**: A bar chart summarizing the total confirmed, deaths, and recovered cases for each WHO region.
    * **Confirmed vs. Deaths**: A log-scale scatter plot to visualize the relationship between confirmed cases and deaths, colored by WHO region.

## Dataset

The analysis is performed on the `country_wise_latest.csv` dataset. This file contains aggregated, country-level data on COVID-19, including fields for confirmed cases, deaths, recoveries, active cases, and regional information from the World Health Organization (WHO).

## Technologies Used

* **Streamlit**: For building and serving the interactive web application.
* **Pandas**: For data loading, manipulation, and aggregation.
* **Seaborn & Matplotlib**: For generating the charts and visualizations.

## Setup and Usage

To run this dashboard locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/HimanshuSingh-966/RISE_INTERNSHIP.git](https://github.com/HimanshuSingh-966/RISE_INTERNSHIP.git)
    cd RISE_INTERNSHIP/Task4_COVID_19_Data_Analysis
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install streamlit pandas seaborn matplotlib
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

4.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## ✨ Dashboard Output Visualizations

Here are various screenshots from the interactive COVID-19 Data Analysis Dashboard:

### 1. Dashboard Overview with Filters
![Dashboard Overview with Filters](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133115.png)
This image showcases the main dashboard layout with interactive filters for WHO Region, Country, and Confirmed Cases range, along with key performance indicators.

### 2. Top 10 Countries by Case Type (e.g., Confirmed)
![Top 10 Countries by Case Type](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133149.png)
A bar chart displaying the top 10 countries based on the selected case type (e.g., Confirmed cases), providing a quick overview of the most affected nations.

### 3. Comparative Statistics for Top 15 Countries
![Comparative Statistics for Top 15 Countries](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133212.png)
A stacked horizontal bar chart comparing Confirmed, Deaths, Recovered, and Active cases for the top 15 countries, offering a detailed case breakdown.

### 4. Mortality and Recovery Rates Heatmap
![Mortality and Recovery Rates Heatmap](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133226.png)
A heatmap visualizing `Deaths / 100 Cases`, `Recovered / 100 Cases`, and `Deaths / 100 Recovered` for the top 20 countries, highlighting critical health metrics.

### 5. Weekly Percentage Increase in Cases
![Weekly Percentage Increase in Cases](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133239.png)
A bar chart illustrating the weekly percentage increase in cases for the top 10 countries, useful for tracking growth trends.

### 6. Weekly Absolute Change in Cases
![Weekly Absolute Change in Cases](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133250.png)
A bar chart showing the weekly absolute change in cases for the top 10 countries, indicating the raw increase in numbers.

### 7. Confirmed vs. Deaths (Log Scale Scatter Plot)
![Confirmed vs. Deaths Log Scale Scatter Plot](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task4_COVID_19_Data_Analysis/images/Screenshot%202025-07-10%20133306.png)
A log-scale scatter plot illustrating the relationship between confirmed cases and deaths, with points colored by WHO region to reveal regional patterns.

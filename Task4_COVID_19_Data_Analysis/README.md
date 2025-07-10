# COVID-19 Global Data Analysis Dashboard

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task4_COVID_19_Data_Analysis)

## Overview

This repository contains an interactive web application built with Streamlit for visualizing and analyzing global COVID-19 data. The dashboard provides a visual narrative of the pandemic's spread, recovery trends, and mortality rates across various countries and WHO regions.

## Features

The dashboard offers a range of interactive features and visualizations:

*   **Interactive Filters**:
    *   Filter data by WHO Region.
    *   Filter data by specific countries within a selected region.
    *   Sort visualizations by case type: `Confirmed`, `Deaths`, `Recovered`, or `Active`.
    *   Filter countries based on a dynamic range of confirmed cases.

*   **Key Visualizations**:
    *   **Top 10 Countries**: A bar chart displaying the top 10 countries based on the selected case type.
    *   **Comparative Statistics**: A stacked horizontal bar chart comparing confirmed, deaths, recovered, and active cases for the top 15 countries.
    *   **Mortality and Recovery Rates**: A heatmap showing `Deaths / 100 Cases`, `Recovered / 100 Cases`, and `Deaths / 100 Recovered` for the top 20 countries.
    *   **Weekly Growth Trends**: Side-by-side bar charts illustrating the weekly percentage increase and absolute change in cases for the top 10 countries.
    *   **WHO Region Summary**: A bar chart summarizing the total confirmed, deaths, and recovered cases for each WHO region.
    *   **Confirmed vs. Deaths**: A log-scale scatter plot to visualize the relationship between confirmed cases and deaths, colored by WHO region.

## Dataset

The analysis is performed on the `country_wise_latest.csv` dataset. This file contains aggregated, country-level data on COVID-19, including fields for confirmed cases, deaths, recoveries, active cases, and regional information from the World Health Organization (WHO).

## Technologies Used

*   **Streamlit**: For building and serving the interactive web application.
*   **Pandas**: For data loading, manipulation, and aggregation.
*   **Seaborn & Matplotlib**: For generating the charts and visualizations.

## Setup and Usage

To run this dashboard locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HimanshuSingh-966/RISE_INTERNSHIP.git
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
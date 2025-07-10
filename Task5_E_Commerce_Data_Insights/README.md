# 🛍️ E-Commerce Data Insights Dashboard

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task5_E_Commerce_Data_Insights)

This repository contains an interactive dashboard built with Streamlit to analyze and visualize e-commerce data. The dashboard provides key insights into sales performance, customer behavior, and product popularity from a transnational online retail dataset.

## Features

The dashboard offers a comprehensive view of the e-commerce data through various metrics and visualizations:

*   **Key Performance Indicators (KPIs):**
    *   💰 Total Revenue
    *   📦 Total Orders
    *   👥 Unique Customers
    *   🧾 Unique Products
*   **Interactive Filters:**
    *   Filter data by Country.
    *   Filter data by Year.
*   **Visualizations:**
    *   **📈 Top 10 Selling Products:** A bar chart showing the most sold products by quantity.
    *   **🌍 Revenue Distribution by Country:** A pie chart illustrating the revenue share of the top 10 countries.
    *   **📊 User Purchase Frequency:** A histogram displaying the distribution of the number of orders per customer.
    *   **🕐 Sales by Hour of Day:** A line chart tracking revenue generated at different hours of the day.
    *   **📅 Monthly Revenue Trend:** A line chart showing the total revenue trend month over month.

## Data Source

The application uses the [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) from the UCI Machine Learning Repository. This is a transnational dataset that contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based non-store online retail.

The dataset is included in this repository as `e_commerce_data.csv`.

## How to Run

To run this dashboard on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/himanshusingh-966/RISE_INTERNSHIP.git
    cd RISE_INTERNSHIP/Task5_E_Commerce_Data_Insights
    ```

2.  **Install the required libraries:**
    Make sure you have Python installed. Then, install the necessary libraries using pip.
    ```bash
    pip install streamlit pandas matplotlib seaborn
    ```

3.  **Run the Streamlit application:**
    Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```

4.  **View the dashboard:**
    Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

**Note:** The path to the CSV file in `app.py` is currently hardcoded. You may need to update the `load_data` function to use a relative path like `pd.read_csv("e_commerce_data.csv", ...)` for the application to run correctly in a standard environment.
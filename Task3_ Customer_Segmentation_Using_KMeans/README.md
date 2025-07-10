# Customer Segmentation Using K-Means Clustering

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/HimanshuSingh-966/RISE_INTERNSHIP/tree/main/Task3_%20Customer_Segmentation_Using_KMeans)

## Project Overview

This project demonstrates customer segmentation using the K-Means clustering algorithm, an unsupervised machine learning technique. The goal is to partition a mall's customer base into distinct groups based on their annual income and spending score. By identifying these segments, a business can develop targeted marketing strategies for each group.

## Dataset

The analysis is performed on the `Mall_Customers.csv` dataset, which contains the following columns:
- `CustomerID`: A unique identifier for each customer.
- `Gender`: The gender of the customer.
- `Age`: The age of the customer.
- `Annual Income (k$)`: The annual income of the customer in thousands of dollars.
- `Spending Score (1-100)`: A score assigned by the mall based on customer behavior and spending nature. A higher score indicates a higher propensity to spend.

## Methodology

The `customer_segmentation.ipynb` Jupyter Notebook details the following steps:

1.  **Data Loading & Exploration**: The dataset is loaded using pandas, and an initial analysis is performed to understand its structure and features.
2.  **Feature Selection**: For this clustering task, `Annual Income (k$)` and `Spending Score (1-100)` are selected as the primary features for segmentation.
3.  **Finding the Optimal Number of Clusters (K)**: The Elbow Method is employed to determine the optimal number of clusters (K) for the K-Means algorithm. This is done by plotting the Within-Cluster Sum of Squares (WCSS) against the number of clusters and identifying the "elbow" point where the rate of decrease in WCSS slows down significantly. The analysis identified K=5 as the optimal value.
4.  **K-Means Model Training**: A K-Means model is trained on the selected features with K set to 4.
5.  **Visualization**: The resulting customer segments are visualized using a scatter plot, where each point represents a customer, and the color represents the assigned cluster. The centroids of each cluster are also plotted.

## Results

The K-Means algorithm successfully segmented the customers into four distinct groups:

1.  **High Income, Low Spending**: Cautious or dissatisfied wealthy customers.
2.  **High Income, High Spending**: The primary target group for premium products.
3.  **Mid Income, Mid Spending**: The average customer segment.
4.  **Low Income, Low Spending**: Cautious customers with limited purchasing power.

These insights can be leveraged to create tailored marketing campaigns and improve customer engagement.

## How to Run

To run this analysis on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/himanshusingh-966/rise_internship.git](https://github.com/himanshusingh-966/rise_internship.git)
    cd rise_internship/Task3_ Customer_Segmentation_Using_KMeans
    ```
2.  **Install required libraries:**
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn jupyterlab
    ```
3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter lab customer_segmentation.ipynb
    ```
    Execute the cells in the notebook sequentially to reproduce the analysis and visualizations.

## ✨ Output Visualizations

Here are the key visualizations from the customer segmentation analysis:

### 1. Elbow Method for Optimal K
![Elbow Method for Optimal K](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task3_%20Customer_Segmentation_Using_KMeans/images/Screenshot%202025-07-10%20131532.png)

This plot shows the Within-Cluster Sum of Squares (WCSS) against the number of clusters, helping to identify the "elbow" point (K=4) for optimal clustering.

### 2. Segmented Customers 2D Scatter Plot (Raw)
![Segmented Customers 2D Scatter Plot Raw](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task3_%20Customer_Segmentation_Using_KMeans/images/Screenshot%202025-07-10%20131552.png)

A scatter plot displaying the customers based on Annual Income and Spending Score, color-coded by their assigned cluster. This visualization helps in understanding the initial grouping before centroid visualization.

### 3. Customer Segments with Centroids
![Customer Segments with Centroids](https://raw.githubusercontent.com/HimanshuSingh-966/RISE_INTERNSHIP/main/Task3_%20Customer_Segmentation_Using_KMeans/images/Screenshot%202025-07-10%20131607.png)

This scatter plot visualizes the **four** distinct customer segments, with each cluster represented by a different color. The centroids (center points) of each cluster are also marked, clearly indicating the average income and spending score for each segment.

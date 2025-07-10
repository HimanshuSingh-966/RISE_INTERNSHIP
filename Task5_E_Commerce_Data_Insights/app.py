import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.set_page_config(page_title="E-Commerce Data Insights", layout="wide")
st.title("🛍️ E-Commerce Data Insights Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Task5_E_Commerce_Data_Insights/e_commerce_data.csv", encoding='ISO-8859-1')
    df.dropna(subset=["CustomerID"], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("📌 Filters")
country = st.sidebar.selectbox("Select Country", ['All'] + sorted(df['Country'].unique()))
year = st.sidebar.selectbox("Select Year", ['All'] + sorted(df['Year'].unique()))

filtered_df = df.copy()
if country != 'All':
    filtered_df = filtered_df[filtered_df['Country'] == country]
if year != 'All':
    filtered_df = filtered_df[filtered_df['Year'] == year]

# KPIs
total_revenue = filtered_df['Revenue'].sum()
total_orders = filtered_df['InvoiceNo'].nunique()
total_customers = filtered_df['CustomerID'].nunique()
total_products = filtered_df['StockCode'].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("📦 Total Orders", total_orders)
col3.metric("👥 Unique Customers", total_customers)
col4.metric("🧾 Unique Products", total_products)

st.markdown("---")

# Top Selling Products
st.subheader("📈 Top 10 Selling Products")
top_products = filtered_df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(x=top_products.values, y=top_products.index, ax=ax1, palette='dark:#5A9')
ax1.set_xlabel("Quantity Sold")
ax1.set_ylabel("Product")
ax1.set_title("Top 10 Products")
for p in ax1.patches:
    ax1.annotate(f"{int(p.get_width())}", 
                 (p.get_width() + 5, p.get_y() + 0.4), fontsize=8)
plt.tight_layout()
st.pyplot(fig1)

# Revenue by Country - Pie Chart
st.subheader("🌍 Revenue Distribution by Country")
country_revenue = filtered_df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
top_countries = country_revenue.head(10)
others = country_revenue.sum() - top_countries.sum()
top_countries['Others'] = others

fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.pie(top_countries.values, labels=None, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
ax2.legend(top_countries.index, loc="best", fontsize=8)
ax2.set_title("Revenue Share by Country")
ax2.axis('equal')
plt.tight_layout()
st.pyplot(fig2)

# 📊 Purchase Frequency by User
st.subheader("📊 User Purchase Frequency")
user_freq = filtered_df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.histplot(user_freq, bins=20, kde=False, ax=ax3, color='teal')
ax3.set_title("Orders per Customer")
ax3.set_xlabel("Number of Orders")
ax3.set_ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

# 📆 Sales by Hour
st.subheader("🕐 Sales by Hour of Day")
sales_by_hour = filtered_df.groupby('Hour')['Revenue'].sum()

fig4, ax4 = plt.subplots(figsize=(8, 4))
sns.lineplot(x=sales_by_hour.index, y=sales_by_hour.values, ax=ax4, marker='o', color='orange')
ax4.set_title("Revenue by Hour")
ax4.set_xlabel("Hour of Day")
ax4.set_ylabel("Revenue (£)")
ax4.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig4)

# 🔁 Monthly Revenue Trend
st.subheader("📅 Monthly Revenue Trend")
monthly_revenue = filtered_df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
monthly_revenue['Month-Year'] = monthly_revenue['Year'].astype(str) + '-' + monthly_revenue['Month'].astype(str)

fig5, ax5 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=monthly_revenue, x='Month-Year', y='Revenue', marker='o', color='purple', ax=ax5)
ax5.set_title("Monthly Revenue Trend")
ax5.set_xlabel("Month-Year")
ax5.set_ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig5)

st.markdown("---")
st.caption("📊 Data Source: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)")

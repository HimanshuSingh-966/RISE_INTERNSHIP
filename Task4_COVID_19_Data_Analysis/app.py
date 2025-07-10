import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load dataset
df = pd.read_csv("Task4_COVID_19_Data_Analysis/country_wise_latest.csv")

st.title("🌍 COVID-19 Global Data Dashboard")

st.markdown("""
This interactive dashboard presents a visual story of the global COVID-19 pandemic—its spread, recovery trends, and
mortality rates. Use the sidebar to filter by WHO region, country, and case counts.
""")

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🔍 Filters")

# Region Filter
regions = ['All'] + sorted(df['WHO Region'].dropna().unique())
selected_region = st.sidebar.selectbox("Select WHO Region", regions)

# Country Filter (based on selected region)
filtered_df = df if selected_region == 'All' else df[df['WHO Region'] == selected_region]
countries = ['All'] + sorted(filtered_df['Country/Region'].unique())
selected_country = st.sidebar.selectbox("Select Country", countries)

# Case Type Filter
case_type = st.sidebar.radio("Sort by Case Type", ['Confirmed', 'Deaths', 'Recovered', 'Active'])

# Confirmed Case Range Filter
min_confirmed = int(df['Confirmed'].min())
max_confirmed = int(df['Confirmed'].max())
confirmed_range = st.sidebar.slider("Confirmed Case Range", min_confirmed, max_confirmed, (min_confirmed, max_confirmed))

# Apply filters
if selected_region != 'All':
    df = df[df['WHO Region'] == selected_region]

if selected_country != 'All':
    df = df[df['Country/Region'] == selected_country]

df = df[(df['Confirmed'] >= confirmed_range[0]) & (df['Confirmed'] <= confirmed_range[1])]

# ---------------- Top Stats Section ----------------
st.header(f"🌟 Top 10 Countries by {case_type}")

top_df = df.sort_values(by=case_type, ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_df, x=case_type, y='Country/Region', hue='Country/Region', palette='coolwarm', ax=ax, legend=False)
ax.set_title(f"Top 10 Countries by {case_type}")
st.pyplot(fig)

# ---------------- Comparative Plot ----------------
st.header("📊 Comparative Statistics for Top 15 Countries")
comp_df = df[['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']].sort_values(by='Confirmed', ascending=False).head(15)
comp_df.set_index('Country/Region', inplace=True)
fig, ax = plt.subplots(figsize=(14, 6))
comp_df.plot(kind='barh', stacked=True, ax=ax, colormap='tab20')
plt.title("Confirmed, Deaths, Recovered & Active Cases (Top 15)")
st.pyplot(fig)

# ---------------- Heatmap ----------------
st.header("🔥 Mortality and Recovery Rates (Top 20 Countries)")
rate_df = df[['Country/Region', 'Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered']].set_index('Country/Region')
rate_df = rate_df.sort_values(by='Deaths / 100 Cases', ascending=False).head(20)
fig, ax = plt.subplots(figsize=(14, 6))
sns.heatmap(rate_df, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5, ax=ax)
plt.title("Mortality & Recovery Ratios")
st.pyplot(fig)

# ---------------- Weekly Growth ----------------
st.header("📈 Weekly Growth Trends")
col5, col6 = st.columns(2)

with col5:
    st.subheader("% Increase Over the Week")
    growth_df = df.sort_values(by='1 week % increase', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=growth_df, x='1 week % increase', y='Country/Region', hue='Country/Region', palette='rocket', ax=ax, legend=False)
    ax.set_title("% Increase")
    st.pyplot(fig)

with col6:
    st.subheader("Absolute Change Over the Week")
    change_df = df.sort_values(by='1 week change', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=change_df, x='1 week change', y='Country/Region', hue='Country/Region', palette='crest', ax=ax, legend=False)
    ax.set_title("Absolute Increase")
    st.pyplot(fig)

# ---------------- Region-wise Summary ----------------
st.header("🗺️ WHO Region-wise Summary")
region_summary = df.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered']].sum().sort_values(by='Confirmed', ascending=False)
fig, ax = plt.subplots(figsize=(12, 5))
region_summary.plot(kind='bar', ax=ax, colormap='Dark2')
plt.title("Region-wise COVID-19 Summary")
plt.xticks(rotation=45)
st.pyplot(fig)

# ---------------- Confirmed vs Deaths Scatter ----------------
st.header("📍 Confirmed vs Deaths (Log Scale)")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='Confirmed', y='Deaths', hue='WHO Region', palette='Set1', s=120, edgecolor='black', ax=ax)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title("Confirmed vs Deaths (Log Scale)")
ax.set_xlabel("Confirmed Cases (log scale)")
ax.set_ylabel("Deaths (log scale)")
st.pyplot(fig)

st.markdown("---")
st.caption("📦 Data source: COVID-19 Dataset (uploaded CSV)")

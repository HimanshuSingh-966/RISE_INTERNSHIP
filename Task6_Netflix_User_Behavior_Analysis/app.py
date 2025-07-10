import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
@st.cache_data

def load_data():
    df = pd.read_csv("Task6_Netflix_User_Behavior_Analysis/netflix_behavior_merged.csv", parse_dates=['Start Time', 'Date'], low_memory=False)

    # Drop unwanted or problematic columns (like nested dicts, JSONs, mixed types)
    columns_to_drop = [
        'Attributes', 'Supplemental Video Type', 'Bookmark', 'Latest Bookmark',
        'Game Handle', 'Profile Transferred', 'Profile Transfer Time',
        'Profile Transferred From Account', 'Profile Transferred To Account',
        'Opt-Out', 'Privacy And Data Settings', 'Esn', 'Device Type_y',
        'Acct First Playback Date', 'Acct Last Playback Date',
        'Acct First Playback Date For User Generated Plays', 'Acct Last Playback Date For User Generated Plays',
        'Profile First Playback Date', 'Profile Last Playback Date',
        'Profile First Playback Date For User Generated Plays', 'Profile Last Playback Date For User Generated Plays',
        'Deactivation Time', 'Unnamed: 0'
    ]
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Fix duration to seconds
    df['Duration'] = pd.to_timedelta(df['Duration'], errors='coerce')
    df['Duration_sec'] = df['Duration'].dt.total_seconds()

    return df

df = load_data()

# ------------------------------ UI ------------------------------
st.title("🎬 Netflix User Behavior Dashboard")
st.markdown("Analyze streaming trends, binge patterns, genres & more")

# Sidebar filters
st.sidebar.header("🔎 Filter Data")
selected_profile = st.sidebar.multiselect("Select Profile(s)", df['Profile Name'].unique(), default=df['Profile Name'].unique())
selected_year = st.sidebar.multiselect("Select Year(s)", sorted(df['Year'].dropna().unique()), default=sorted(df['Year'].dropna().unique()))

filtered_df = df[(df['Profile Name'].isin(selected_profile)) & (df['Year'].isin(selected_year))]

# ------------------------ KPIs ------------------------
st.subheader("🔢 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Watch Time (hrs)", round(filtered_df['Duration_sec'].sum() / 3600, 2))
col2.metric("Unique Titles Watched", filtered_df['Title'].nunique())
col3.metric("Total Watch Sessions", filtered_df.shape[0])

# ------------------------ Visuals ------------------------
st.markdown("---")
st.subheader("🧠 Top Watched Titles")
top_titles = filtered_df['Title'].value_counts().nlargest(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_titles.values, y=top_titles.index, palette="magma", ax=ax1)
ax1.set_xlabel("Watch Count")
ax1.set_ylabel("Title")
st.pyplot(fig1)

st.subheader("📊 Genre Distribution")
genre_data = filtered_df['listed_in'].dropna().str.split(', ', expand=True).stack()
genre_counts = genre_data.value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Count")
ax2.set_ylabel("Genre")
st.pyplot(fig2)

st.subheader("📅 Viewing Pattern by Day")
fig3, ax3 = plt.subplots()
sns.countplot(data=filtered_df, x='Weekday', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], palette="Set2", ax=ax3)
ax3.set_ylabel("Watch Sessions")
ax3.set_xlabel("Weekday")
st.pyplot(fig3)

st.subheader("⏰ Viewing Pattern by Hour")
fig4, ax4 = plt.subplots()
sns.histplot(data=filtered_df, x='Hour', bins=24, kde=False, color='skyblue', ax=ax4)
ax4.set_ylabel("Watch Count")
ax4.set_xlabel("Hour of Day")
st.pyplot(fig4)

st.subheader("🌍 Country-wise Viewership")
country_counts = filtered_df['Country'].value_counts().head(10)
fig5, ax5 = plt.subplots()
sns.barplot(y=country_counts.index, x=country_counts.values, palette="viridis", ax=ax5)
ax5.set_xlabel("Views")
ax5.set_ylabel("Country")
st.pyplot(fig5)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit, Pandas, Seaborn, Matplotlib")

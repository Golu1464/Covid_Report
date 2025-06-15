import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="COVID-19 Dashboard", layout="centered")

st.title("🌍 COVID-19 Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("covid_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Clean data
df = df.dropna(subset=['location', 'total_cases'])

# Sidebar: Select country
countries = sorted(df['location'].unique())
selected_country = st.sidebar.selectbox("Select a Country", countries)

# Filter by country
country_df = df[df['location'] == selected_country]
latest = country_df.sort_values('date').iloc[-1]

# Helper function to show metrics
def safe_metric(label, value):
    if pd.notna(value):
        st.metric(label, f"{int(value):,}")
    else:
        st.metric(label, "Data not available")

# Show metrics
st.subheader(f"📊 COVID-19 Summary - {selected_country}")

col1, col2, col3 = st.columns(3)
with col1:
    safe_metric("Total Cases", latest.get('total_cases'))

with col2:
    safe_metric("Total Deaths", latest.get('total_deaths'))

with col3:
    safe_metric("People Fully Vaccinated", latest.get('people_fully_vaccinated'))

col4, col5, col6 = st.columns(3)
with col4:
    safe_metric("Total Tests", latest.get('total_tests'))

with col5:
    safe_metric("Population", latest.get('population'))

with col6:
    safe_metric("Total Recoveries", latest.get('total_cases') - latest.get('total_deaths') if pd.notna(latest.get('total_cases')) and pd.notna(latest.get('total_deaths')) else None)

# Plot: Daily New Cases
st.subheader("📈 Daily New COVID-19 Cases Over Time")
if 'new_cases' in country_df.columns and country_df['new_cases'].notna().any():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(country_df['date'], country_df['new_cases'], color='blue')
    ax.set_title(f'Daily New Cases in {selected_country}')
    ax.set_xlabel("Date")
    ax.set_ylabel("New Cases")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("No daily new case data available.")

# Plot: Vaccination Progress
if 'people_fully_vaccinated' in country_df.columns and country_df['people_fully_vaccinated'].notna().any():
    st.subheader("💉 Vaccination Progress Over Time")

    fig, ax = plt.subplots(figsize=(10, 4))

    # Scatter plot with larger dots
    ax.scatter(
        country_df['date'],
        country_df['people_fully_vaccinated'],
        color='green',
        s=20  # Size of dots (increase this for larger markers)
    )

    ax.set_title(f'Vaccination Progress in {selected_country}')
    ax.set_xlabel("Date")
    ax.set_ylabel("Fully Vaccinated People")
    ax.grid(True)

    st.pyplot(fig)
else:
    st.warning("No vaccination data available.")


# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Data Source: Our World In Data")

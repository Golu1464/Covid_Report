# 🦠 COVID-19 Dashboard with Streamlit

This project is a simple, interactive **COVID-19 data dashboard** built using **Python**, **Pandas**, **Matplotlib**, and **Streamlit**. It allows users to visualize the latest COVID-19 statistics for any country, including total cases, deaths, vaccinations, and trends over time.

---

## 📊 Features

- 🌍 Select a country from a dropdown list
- 📈 View:
  - Total confirmed cases
  - Total deaths
  - People fully vaccinated
  - Total tests conducted
  - Population
- 📉 Line chart of daily new COVID-19 cases
- 💉 Vaccination progress plot
- 🧠 Handles missing data gracefully (no crashes)

---

## 🗂️ Folder Structure

covid_dashboard/
│
├── app.py # Main Streamlit app
├── covid_data.csv # COVID-19 dataset (from Our World In Data)
├── requirements.txt # Required Python packages
└── README.md # This file


---

## 🛠️ Installation & Running Locally

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/covid-dashboard.git
cd covid-dashboard

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py

🧪 Dataset Source
The dataset used is from Our World In Data (OWID). It includes daily updates on COVID-19 cases, deaths, vaccinations, testing, and more.
https://github.com/owid/covid-19-data

To update your data:

wget https://covid.ourworldindata.org/data/owid-covid-data.csv -O covid_data.csv

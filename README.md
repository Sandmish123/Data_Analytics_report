# Data_Analytics_report

---

## Overview

This project is a web-based Data Analytics and Visualization Dashboard built using **Streamlit**, **MongoDB**, and various data analysis libraries. It provides an interface for users to upload or fetch data, perform Exploratory Data Analysis (EDA), and visualize results interactively. It also integrates with a database to store and retrieve data.

---

## Features

1. **Data Source Options**:
   - Upload CSV files.
   - Fetch data from APIs.

2. **Database Integration**:
   - Store and retrieve data in/from **MongoDB**.

3. **SQL Editor**:
   - Run SQL queries to manipulate and analyze data.
   - Limit: 5 queries per session.

4. **Python Editor**:
   - Perform Python-based operations on data (future enhancement).

5. **Data Visualization**:
   - Options to explore data using:
     - Overview
     - Correlation Plot
     - Missing Values Plot
     - Pairplot
     - Skewness and Kurtosis Plot
     - Univariate Analysis

6. **Data Cleaning**:
   - Built-in data cleaning feature using the **Klib** library.

7. **Interactive Visualizations**:
   - Generate graphs and plots dynamically based on selected options.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Access the app at `http://localhost:8501` in your browser.

---

## Folder Structure

```plaintext
project/
│
├── app.py                # Main application file
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── database/             # Database-related files
│   ├── db_connect.py     # Database connection logic
│   └── db_config.py      # Database configuration
├── utils/                # Utility functions for analysis
│   ├── eda.py            # EDA-related functions
│   └── correlation.py    # Visualization utilities
├── data/                 # Sample datasets
│   └── sample_data.csv   # Example data file
└── logs/                 # Logging files
    └── app.log           # Application logs
```

---

## Usage

### 1. Upload Data
- Choose between **CSV** or **API** as the data source.
- Preview data before performing any analysis.

### 2. Store Data
- Save data to the database by providing a table name.

### 3. Perform SQL Queries
- Use the built-in SQL editor to query stored data.
- Query limit: 5 queries per session.

### 4. Perform EDA
- Choose from several analysis options like overview, correlation plot, missing values, etc.

### 5. Visualize Data
- Generate interactive charts and graphs based on selected columns.

---

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Database**: MongoDB
- **Libraries**:
  - Pandas
  - Matplotlib
  - Klib
  - Requests

---

## Future Enhancements

1. Add a Python Editor for custom scripting.
2. Enhance API integration for dynamic data processing.
3. Improve database interactions for larger datasets.
4. Deploy the app using cloud platforms.

---

## Contribution

Feel free to contribute by:
- Forking this repository.
- Creating a new branch.
- Submitting a pull request with detailed descriptions.

---

## License

This project is licensed under the MIT License.

--- 

This README provides a complete overview of your project and guides users through installation, setup, and usage. Let me know if you'd like further refinements!

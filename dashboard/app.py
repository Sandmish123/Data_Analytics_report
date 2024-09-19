# import streamlit as st
# import pandas as pd
# import requests
# from ydata_profiling import ProfileReport
# import streamlit.components.v1 as components  # Import streamlit components for HTML rendering

# st.title("Automated Data Insights Dashboard")

# # Option to select between CSV or API
# data_source = st.radio("Choose Data Source", ["CSV", "API"])

# # Initialize an empty DataFrame
# data = pd.DataFrame()

# # If CSV is selected
# if data_source == "CSV":
#     uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
#     if uploaded_file is not None:
#         data = pd.read_csv(uploaded_file)
#         st.write("Data Preview:")
#         st.write(data.head())

# # If API is selected
# elif data_source == "API":
#     api_url = st.text_input("Enter API URL")
#     if api_url:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             try:
#                 data = pd.DataFrame(response.json())  # Assuming API returns JSON
#                 st.write("Data Preview:")
#                 st.write(data.head())
#             except ValueError:
#                 st.error("Error: The API response format is not compatible.")
#         else:
#             st.error(f"Failed to fetch data. Status Code: {response.status_code}")

# # Perform EDA with ydata Profiling if data is available
# if not data.empty:
#     st.write("Generating EDA Report...")
#     profile = ProfileReport(data, explorative=True)

#     # Generate the report and display it
#     profile_html = profile.to_html()
#     components.html(profile_html, height=1000, scrolling=True)

#******************************************************************************************************************************************

# app.py
# import streamlit as st
# import pandas as pd
# import sys
# sys.path.append(".")
# from utils.eda import analyze_data
# from utils.correlation import suggest_visualizations, generate_plot
# sys.path.append(".")
# from database.db_connect import insert_data_to_db

# def main():
#     st.title("Data Analysis and Visualization")

#     data_source = st.radio("Choose Data Source", ["CSV"])
    
#     if data_source == "CSV":
#         uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
#         if uploaded_file:
#             data = pd.read_csv(uploaded_file)
#             st.write("Data Preview:", data.head())

#             # Store data in the database
#             if st.button("Store Data in Database"):
#                 table_name = st.text_input("Enter Table Name", "uploaded_data")
#                 if table_name:
#                     insert_data_to_db(data, table_name)
#                     st.success(f"Data has been successfully stored in the table: {table_name}")

#             # Perform analysis
#             correlations = analyze_data(data)
#             st.write("Top 5 Correlations:", correlations)

#             correlation_pair = st.selectbox("Select Correlation Pair", correlations.index)
#             visualizations = suggest_visualizations(correlation_pair, data)

#             for viz in visualizations:
#                 if st.button(f"Show {viz['type']}"):
#                     x, y = correlation_pair
#                     generate_plot(data, x, y, viz['type'])

# if __name__ == "__main__":
#     main()


# ********************************************************************************************************************************************



# import streamlit as st
# import pandas as pd
# import sys
# sys.path.append(".")
# from utils.eda import analyze_data
# from utils.correlation import suggest_visualizations, generate_plot
# sys.path.append(".")
# from database.db_connect import insert_data_to_db
# from database.db_connect import execute_sql  # Add an appropriate function for SQL execution

# def main():
#     st.title("Data Analysis and Visualization")

#     # Step 1: Choose data source and upload
#     data_source = st.radio("Choose Data Source", ["CSV"])
    
#     if data_source == "CSV":
#         uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
#         if uploaded_file:
#             data = pd.read_csv(uploaded_file)
#             st.write("Data Preview:", data.head())

#             # Step 2: Store data in the database
#             if st.button("Store Data in Database"):
#                 table_name = st.text_input("Enter Table Name", "uploaded_data")
#                 if table_name:
#                     insert_data_to_db(data, table_name)
#                     st.success(f"Data has been successfully stored in the table: {table_name}")

#             # Step 3: SQL and Python Editors
#             st.subheader("SQL and Python Editors")
            
#             # SQL Editor
#             sql_code = st.text_area("SQL Editor", "SELECT * FROM uploaded_data LIMIT 10;")
#             if st.button("Execute SQL"):
#                 try:
#                     sql_result = execute_sql(sql_code)
#                     st.write("SQL Query Result:", sql_result)
#                 except Exception as e:
#                     st.error(f"Error executing SQL: {e}")

#             # Python Code Editor
#             python_code = st.text_area("Python Editor", "print(data.head())")
#             if st.button("Run Python Code"):
#                 try:
#                     exec(python_code, globals())
#                 except Exception as e:
#                     st.error(f"Error executing Python code: {e}")

#             # Step 4: Data Analysis
#             correlations = analyze_data(data)
#             st.write("Top 5 Correlations:", correlations)

#             correlation_pair = st.selectbox("Select Correlation Pair", correlations.index)
#             visualizations = suggest_visualizations(correlation_pair, data)

#             # Step 5: Visualization Options
#             st.subheader("Visualization Options")
#             for viz in visualizations:
#                 if st.button(f"Show {viz['type']}"):
#                     x, y = correlation_pair
#                     generate_plot(data, x, y, viz['type'])

# if __name__ == "__main__":
#     main()




# import streamlit as st
# import pandas as pd
# import sys
# sys.path.append(".")
# from utils.eda import analyze_data
# from utils.correlation import suggest_visualizations, generate_plot
# sys.path.append(".")
# from database.db_connect import fetch_data_from_db, insert_data_to_db

# def main():
#     st.title("Data Analysis and Visualization")
    
#     data_source = st.radio("Choose Data Source", ["SQL Editor", "CSV"])

#     # SQL Editor to fetch data from the database
#     if data_source == "SQL Editor":
#         query = st.text_area("Enter SQL Query", "SELECT * FROM uploaded_data LIMIT 10")
#         if st.button("Execute Query"):
#             data = fetch_data_from_db(query)  # Fetch data from the database based on the query
#             if data is not None:
#                 st.write("Fetched Data:", data.head())  # Display the fetched data
#                 # st.write(f"Shape of Data: {data.shape}")

#                 # Perform EDA
#                 st.subheader("Exploratory Data Analysis")
#                 correlations = analyze_data(data)  # Perform analysis (you can customize this function)
#                 st.write("Top 5 Correlations:", correlations)

#                 correlation_pair = st.selectbox("Select Correlation Pair", correlations.index)
#                 visualizations = suggest_visualizations(correlation_pair, data)

#                 for viz in visualizations:
#                     if st.button(f"Show {viz['type']}"):
#                         x, y = correlation_pair
#                         generate_plot(data, x, y, viz['type'])
#             else:
#                 st.error("Failed to fetch data from the database.")

#     # CSV upload option (previously implemented)
#     elif data_source == "CSV":
#         uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
#         if uploaded_file:
#             data = pd.read_csv(uploaded_file)
#             st.write("Data Preview:", data.head())
#             st.write(f"Shape of Data: {data.shape}")
            
#             if st.button("Store Data in Database"):
#                 table_name = st.text_input("Enter Table Name", "uploaded_data")
#                 if table_name:
#                     insert_data_to_db(data, table_name)
#                     st.success(f"Data has been successfully stored in the table: {table_name}")

# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
import requests
import sys
sys.path.append(".")
from utils.eda import analyze_data
from utils.correlation import suggest_visualizations, generate_plot
sys.path.append(".")
from database.db_connect import fetch_data_from_db, insert_data_to_db
# sys.path.append(".")
# from dashboard.test import perform_eda  # Import perform_eda function from test.py
from threading import Thread
import klib
import matplotlib.pyplot as plt




class app:
        
    def uploads():
        st.title("Data Analysis and Visualization")
        data = None  # Initialize data as None
        data_source = st.radio("Choose Data Source", ["API", "CSV"])
        # CSV upload option
        if data_source == "CSV":
            uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
            if uploaded_file:
                data = pd.read_csv(uploaded_file)
                st.write("Data Preview:", data.head())
                st.write(f"Shape of Data: {data.shape}")
                
                if st.button("Store Data in Database"):
                    table_name = st.text_input("Enter Table Name", "uploaded_data")
                    if table_name:
                        insert_data_to_db(data, table_name)
                        st.success(f"Data has been successfully stored in the table: {table_name}")
        elif data_source == "API":
            api_url = st.text_input("Enter API URL")
            if api_url:
                response = requests.get(api_url)
                if response.status_code == 200:
                    try:
                        data = pd.DataFrame(response.json())  # Assuming API returns JSON
                        st.write("Data Preview:")
                        st.write(data.head())
                    except ValueError:
                        st.error("Error: The API response format is not compatible.")
                else:
                    st.error(f"Failed to fetch data. Status Code: {response.status_code}")
        if data is not None:
            st.subheader("Choose an Action")
            action = st.radio("Select Action", ["SQL Editor", "Python Editor", "Visualizer"])
            
            if action == "SQL Editor":
                obj.sql_interface()
            elif action == "Visualizer":
                obj.visualizer(data)
        else:
            st.info("Please upload a CSV file or fetch data from the API to proceed.")
        


            

    def sql_interface(self):
        # Initialize a counter in Streamlit session state to track the number of executed queries
        if 'query_count' not in st.session_state:
            st.session_state.query_count = 0

        # Check if the query limit (5) has been reached
        if st.session_state.query_count < 5:
            # Display the query input text area
            query = st.text_area("Enter SQL Query", "SELECT * FROM uploaded_data LIMIT 10")
            
            if st.button(f"Execute Query (Remaining Queries: {5 - st.session_state.query_count})"):
                # Fetch data based on the query
                data = fetch_data_from_db(query)
                
                # Display the fetched data
                if data is not None:
                    st.write("Fetched Data:", data.head())
                    # Increment the query count after successfully executing a query
                    st.session_state.query_count += 1
                else:
                    st.error("Failed to fetch data from the database.")
        else:
            # Disable the button and display a message once the limit is reached
            st.write("You have reached the limit of 5 queries.")
            st.button("Execute Query", disabled=True)  # Display a disabled button

    

    # def visualizer(self,data):
        
    #     st.subheader("Exploratory Data Analysis with Klib")
    #     # Present options for EDA (these should match with the options in test.py)
    #     eda_option = st.selectbox("Choose EDA Option", [
    #         "Overview", "Correlation Plot", "Missing Values Plot", 
    #         "Pairplot", "Skewness and Kurtosis Plot", "Univariate Analysis"
    #     ])

    #     # Trigger the EDA based on the user's selection
    #     if st.button("Run EDA"):

                
    #         # Trigger the EDA based on the user's selection
    #         if eda_option == "Overview":
    #             st.write(klib.describe(data))  # Correct usage of klib.describe
    #             st.write(klib.data_cleaning(data))
    #         elif eda_option == "Correlation Plot":
    #             st.write(klib.corr_plot(data))  # Correct usage of klib correlation plot
    #         elif eda_option == "Missing Values Plot":
    #             st.write(klib.missingval_plot(data))  # Missing value visualization
    #         elif eda_option == "Pairplot":
    #             st.write(klib.pairplot(data))
    #         elif eda_option == "Skewness and Kurtosis Plot":
    #             st.write(klib.dist_plot(data))  # Visualize skewness
    #         elif eda_option == "Univariate Analysis":
    #             st.write(klib.cat_plot(data))  # Categorical univariate analysis
    #         else:
    #             st.error("Invalid option selected.")
   
    def visualizer(self , data):
        st.subheader("Exploratory Data Analysis with Klib")

        # Data cleaning option
        if st.button("Clean Data"):
            cleaned_data = klib.data_cleaning(data)
            st.write("Cleaned Data Preview:")
            st.write(cleaned_data.head())
            st.write(f"Shape of Cleaned Data: {cleaned_data.shape}")
            data = cleaned_data  # Update the data variable with cleaned data

        # Present options for EDA
        eda_option = st.selectbox("Choose EDA Option", [
            "Overview", "Correlation Plot", "Missing Values Plot", 
            "Pairplot", "Skewness and Kurtosis Plot", "Univariate Analysis"
        ])

        # Trigger the EDA based on the user's selection
        if eda_option == "Overview":
            st.write(klib.describe.cat_plot(data))  # Correct usage of klib overview
        elif eda_option == "Correlation Plot":
            klib.corr_plot(data) # Correct usage of klib correlation plot
        elif eda_option == "Missing Values Plot":
            klib.missingval_plot(data)  # Generate the missing values plot
        elif eda_option == "Pairplot":
            st.write(klib.pairplot(data))
        elif eda_option == "Skewness and Kurtosis Plot":
            st.write(klib.dist_plot(data))  # Visualize skewness




if __name__ == "__main__":                  
    obj=app()
    app.uploads()

    

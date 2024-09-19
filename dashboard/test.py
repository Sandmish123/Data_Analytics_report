import klib
import pandas as pd
from 

# Define a function for each type of EDA
def perform_eda(choice, data):
    df = data
    
    # Display the first few rows of the DataFrame
    print(df.head(5))
    
    if choice == 'overview':
        # Overview of the dataset
        klib.describe(df)  # Returns various statistics and details about the dataframe
        klib.data_cleaning(df)  # Performs data cleaning and returns a clean dataframe
    elif choice == 'correlation':
        # Correlation plot
        klib.corr_plot(df)  # Visualize the correlation matrix
    elif choice == 'missing_values':
        # Plot for missing values
        klib.missingval_plot(df)  # Visualize missing values in the dataframe
    elif choice == 'pairplot':
        # Pairplot
        klib.pair_plot(df)  # Plot relationships between pairs of columns
    elif choice == 'skew_kurtosis':
        # Skewness and Kurtosis plot (klib doesn't directly support this, but can be done manually)
        print("Skewness and Kurtosis:")
        skewness = df.skew()
        kurtosis = df.kurt()
        print("Skewness:\n", skewness)
        print("Kurtosis:\n", kurtosis)
    elif choice == 'univariate_analysis':
        # Univariate analysis
        klib.cat_plot(df)  # Visualize categorical data
    else:
        print("Invalid choice. Please enter a valid option.")

# utils/eda.py

import pandas as pd

def analyze_data(data):
    """Perform basic EDA such as correlation analysis."""
    # Select only numeric columns
    numeric_data = data.select_dtypes(include=['number'])
    
    if numeric_data.empty:
        raise ValueError("No numeric columns found in the data for correlation analysis.")
    
    # Calculate correlations
    correlations = numeric_data.corr().abs().unstack().sort_values(ascending=False)
    correlations = correlations[correlations != 1].drop_duplicates().head(5)  # Top 5 correlations
    return correlations




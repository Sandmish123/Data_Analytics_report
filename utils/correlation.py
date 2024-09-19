# utils/correlation.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def suggest_visualizations(correlation_pair, data):
    x, y = correlation_pair
    if pd.api.types.is_numeric_dtype(data[x]) and pd.api.types.is_numeric_dtype(data[y]):
        # Example: Scatter plot, Line plot, Heatmap
        return [
            {"type": "Scatter Plot", "function": sns.scatterplot},
            {"type": "Line Plot", "function": sns.lineplot},
            {"type": "Heatmap", "function": sns.heatmap}
        ]
    # Add more logic for other data types

def generate_plot(data, x, y, plot_type):
    plt.figure(figsize=(10, 6))
    if plot_type == "Scatter Plot":
        sns.scatterplot(x=x, y=y, data=data)
    elif plot_type == "Line Plot":
        sns.lineplot(x=x, y=y, data=data)
    elif plot_type == "Heatmap":
        corr_matrix = data[[x, y]].corr()
        sns.heatmap(corr_matrix, annot=True)
    plt.title(f"{plot_type} for {x} vs {y}")
    plt.show()

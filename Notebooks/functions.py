
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to show outliers using boxplot
def show_outliers(dataframe):
    sns.boxplot(data=dataframe)
    # You can customize the plot as per your preference
    # For example, you can set labels and title using plt.xlabel(), plt.ylabel(), and plt.title()
    plt.show()

# Function to show correlation matrix
def show_correlation_matrix(dataframe):
    corr_matrix = dataframe.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
    plt.show()

# General preprocessing function 
def preprocess_data(dataframe):
    # Example: Handling missing values by dropping rows with missing values
    dataframe = dataframe.dropna()
    # You can add more preprocessing steps as per your requirements
    return dataframe

# Function to show distribution using histogram
def show_distribution(dataframe, column):
    sns.histplot(data=dataframe, x=column)
    plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col= None, sep=",")


    # Create scatter plot
    scatter_plot = plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"], label ="Sea Level")

    # Create first line of best fit
    best_fit_line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"], alternative= "two-sided")
    ex_years = pd.Series(list(range(2014, 2051)))
    df = pd.concat([df, ex_years.to_frame("Year")],ignore_index=True)
    y_pred = best_fit_line.intercept + best_fit_line.slope * df["Year"]
    plt.plot(df["Year"],y_pred, color="red", label="Line of Best Fit (1880 - 2050)")
    plt.xticks([float(x) for x in range(1850, 2100, 25)])

    # Create second line of best fit
    best_fit_line2 = linregress((df.loc[(df["Year"] >= 2000) & (df["Year"] <= 2013),"Year"]),(df.loc[(df["Year"] >= 2000) & (df["Year"] <= 2013),"CSIRO Adjusted Sea Level"]), alternative= "two-sided")
    y_pred2 = best_fit_line2.intercept + best_fit_line2.slope * df.loc[df["Year"] >= 2000,"Year"]
    plt.plot(df.loc[df["Year"]>=2000,"Year"], y_pred2, color="blue", label="Line of Best Fit (2000 - 2050)")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# draw_plot()
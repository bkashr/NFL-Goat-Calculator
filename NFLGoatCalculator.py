import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

# 1️⃣ Collect Data
# Example: Scraping Pro Football Reference (or loading a CSV if available)
def load_qb_data():
    url = "https://www.pro-football-reference.com/leaders/pass_yds_career.htm"  # Example URL
    df = pd.read_html(url)[0]  # Extract table
    df.columns = df.columns.droplevel()  # Drop multi-index
    return df

# 2️⃣ Clean & Process Data
def clean_data(df):
    df = df.dropna()  # Remove NaNs
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]  # Format column names
    return df

# 3️⃣ Define Scoring System
def calculate_goat_score(df):
    weights = {
        "superbowls": 10, 
        "mvps": 8, 
        "wins": 5, 
        "yards": 0.001, 
        "tds": 0.5, 
        "turnovers": -2, 
        "all_pro_teammates": -1
    }
    
    df["goat_score"] = (
        df["superbowls"] * weights["superbowls"] +
        df["mvps"] * weights["mvps"] +
        df["wins"] * weights["wins"] +
        df["yards"] * weights["yards"] +
        df["tds"] * weights["tds"] +
        df["turnovers"] * weights["turnovers"] +
        df["all_pro_teammates"] * weights["all_pro_teammates"]
    )
    return df

# 4️⃣ Analyze & Rank
def rank_qbs(df):
    df = df.sort_values(by="goat_score", ascending=False)
    return df

# 5️⃣ Visualize Results
def plot_top_qbs(df, top_n=10):
    top_qbs = df.head(top_n)
    plt.figure(figsize=(10,5))
    plt.barh(top_qbs["player"], top_qbs["goat_score"], color="blue")
    plt.xlabel("GOAT Score")
    plt.ylabel("Quarterback")
    plt.title("Top 10 QBs of All Time")
    plt.gca().invert_yaxis()
    plt.show()

# Main Function to Run Analysis
def main():
    df = load_qb_data()
    df = clean_data(df)
    df = calculate_goat_score(df)
    df = rank_qbs(df)
    print(df.head(10))  # Show top 10 QBs
    plot_top_qbs(df)

if __name__ == "__main__":
    main()

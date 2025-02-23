Best Quarterback of All Time - Python Ranking System

Overview

This project calculates the Greatest Quarterback of All Time (GOAT) using various statistical factors. The program collects QB data, processes and normalizes the statistics, applies a weighted scoring system, and ranks the top quarterbacks accordingly. It also includes a visualization feature for better insights.

Features

Data Collection: Scrapes quarterback stats from Pro Football Reference or loads data from a CSV file.

Data Cleaning & Processing: Formats and normalizes statistics for fair comparisons.

Custom Scoring System: Uses weighted factors such as Super Bowls, MVPs, total wins, yards, and turnovers.

Ranking System: Sorts QBs based on their computed GOAT Score.

Visualization: Generates a bar chart displaying the top-ranked quarterbacks.

Installation

Prerequisites

Python 3.x

Required libraries: pandas, numpy, requests, matplotlib

Setup

Clone this repository:

git clone https://github.com/yourusername/best-qb-ranking.git
cd best-qb-ranking

Install dependencies:

pip install -r requirements.txt

Run the script:

python best_qb_ranking.py

Usage

The script will automatically fetch quarterback data, clean it, compute scores, and display the top 10 QBs.

Modify the weights dictionary in calculate_goat_score() to tweak the ranking formula.

To visualize results, the script generates a bar chart of the top QBs.

Customization

Load CSV Instead of Scraping: Modify load_qb_data() to read from a CSV file instead of scraping.

Adjust Scoring Weights: Change the values in the weights dictionary to reflect personal ranking preferences.

Add More Factors: Expand the dataset with additional stats like passer rating, completion percentage, and playoff wins.

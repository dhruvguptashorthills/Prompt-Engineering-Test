# Nifty 50 Analysis Script

## Overview
This script fetches the latest Nifty 50 stock data from the NSE India API and performs various analyses, including:
- Identifying the top 5 gainers and losers of the day.
- Finding stocks that are 30% below their 52-week high.
- Finding stocks that are 20% above their 52-week low.
- Identifying the top 5 performers over the last 30 days.
- Generating a bar chart for the top gainers and losers.

The results are saved in a text file and a bar chart image.

## Requirements
- Python 3.7 or higher
- The following Python libraries:
  - `requests`
  - `pandas`
  - `matplotlib`

## Installation
1. Clone or download this repository.
2. Install the required libraries using pip:
   ```bash
   pip install requests pandas matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python script.py
   ```
2. The output will be saved in the `output` directory:
   - `nifty50_analysis.txt`: Contains the analysis results.
   - `gainers_losers_chart.png`: Bar chart of the top gainers and losers.

## Output Details
- **Top 5 Gainers and Losers**: Lists the stocks with the highest and lowest percentage changes for the day.
- **Stocks 30% Below 52-Week High**: Lists stocks trading significantly below their 52-week high.
- **Stocks 20% Above 52-Week Low**: Lists stocks trading significantly above their 52-week low.
- **Top 5 Performers in Last 30 Days**: Lists stocks with the highest percentage change over the last 30 days.
- **Bar Chart**: A bar chart visualizing the top 5 gainers and losers is saved as `gainers_losers_chart.png`.

## License
This project is licensed under the MIT License.
Polymarket Data Analysis Dashboard
==================================
streamlit hosted website: https://polymarket-analysis.streamlit.app/

colab notebook: https://colab.research.google.com/drive/1dv43DR_Ae1N1jK5E32N0bKi5v0S5tTyr?usp=sharing

dune library: https://dune.com/workspace/u/naitikv/library/folders/creations

Overview
--------

Analysis of user behavior and market dynamics on Polymarket, focusing on growth patterns since the recent election cycle. The project includes comprehensive data analysis, interactive visualizations, and detailed insights about trading patterns, user engagement, and market performance.


Features
--------

-   Interactive Streamlit dashboard
-   Real-time data updates via Dune Analytics API
-   Comprehensive market categorization
-   Detailed timezone-based trading analysis
-   User retention and engagement metrics
-   Market growth visualization
-   Technical approach documentation

Data Source
-----------

-   Primary data source: Dune Analytics
-   Main table: `polymarket_polygon.market_trades`
-   Data retrieval: Custom SQL queries via Dune API
-   Automated data updates using Python scripts

Technical Stack
---------------

-   Python 3.9
-   Streamlit for web interface
-   Plotly for interactive visualizations
-   Pandas for data manipulation
-   Dune client for API access

Installation
------------

1.  Clone the repository

`git clone https://github.com/07naitik/polymarket-analysis.git`

`cd polymarket-analysis`

2.  Create and activate virtual environment


`python3 -m venv venv`

`source venv/bin/activate`

3.  Install dependencies


`pip install -r requirements.txt`

4.  Run the dashboard


`streamlit run app.py`



Key Questions Answered
----------------------

1.  **Which timezones show the highest trading activity?**
    -   Analysis of 24-hour trading cycle
    -   Peak trading identification during UTC hours
    -   Geographic user activity distribution
2.  **What types of markets attract new users?**
    -   Market category preference analysis
    -   New user distribution across different market types
    -   Category-wise entry point analysis
3.  **How long do new users typically stay active?**
    -   User lifecycle analysis
    -   Activity duration patterns
    -   User retention statistics
4.  **Which markets have seen the most growth?**
    -   Post-election volume trends by category
    -   Identification of growth leaders
    -   Analysis of market volume spikes
5.  **How has user retention changed since the election?**
    -   Comparative retention analysis
    -   Pre vs. post-election user behavior
    -   Changes in engagement patterns


Contact
-------

Naitik Verma - 07vermanaitik@gmail.com

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
  
Design Questions
================

How would you track user retention long-term?
---------------------------------------------

Based on my analysis of the trading data, I would suggest:

1.  **Daily Active Users Tracking**
    -   Track how often users come back to trade
    -   Look at their trading frequency over time
    -   See if they're exploring different market categories
2.  **Simple Retention Metrics**
    -   Count how many users return after their first trade
    -   See how long users typically stay active
    -   Check if certain first trades lead to better retention
3.  **User Groups**
    -   Group users based on when they joined
    -   Compare how different groups behave
    -   See which groups stick around longer

The key is keeping it simple but effective - focus on understanding basic patterns in how users interact with the platform.

What metrics would you use to measure market health?
----------------------------------------------------

From what I've learned analyzing the data:

1.  **Trading Activity**
    -   Daily trading volume
    -   Number of active traders
    -   How often trades happen
2.  **Market Interest**
    -   How many new users join each market
    -   Which markets attract repeat traders
    -   Whether users stay in one market or explore others
3.  **Basic Performance**
    -   How quickly markets get resolved
    -   Whether traders come back to similar markets
    -   If markets maintain steady activity

I think these basic metrics would give a good picture of market health without overcomplicating things.

How could we improve new user onboarding based on the data?
-----------------------------------------------------------

Looking at the patterns in our user data, I'd suggest:

1.  **Start Simple**
    -   Guide new users to popular, straightforward markets first
    -   Show them markets where other new users have had success
    -   Keep the initial experience uncomplicated
2.  **Learn from Success**
    -   Look at what successful users did when they started
    -   Use that to suggest first markets for new users
    -   Help them start with reasonable trade sizes
3.  **Show Progress**
    -   Let users know how they're doing compared to others
    -   Suggest new markets as they get more comfortable
    -   Give them tips based on what worked for similar users

The goal would be to make the first experience positive and build confidence gradually. Nothing too complex - just helpful guidance based on what we see in the data.

These suggestions come from my analysis of user behavior in the data we have. I tried to focus on practical, data-driven improvements that would be realistic to implement.


Contact
-------

Naitik Verma - 07vermanaitik@gmail.com

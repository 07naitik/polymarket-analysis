Polymarket Data Analysis - Technical Approach Documentation
===========================================================

Overview
--------

This document outlines the methodology and technical approach used for analyzing Polymarket trading data to understand user behavior and market dynamics since the recent election cycle.

Initial Approach: Polymarket API
--------------------------------

Initially attempted to use Polymarket's public API (<https://docs.polymarket.com/#introduction>) for data collection. However, this approach proved unsuitable because:

-   Limited access to historical data
-   No direct endpoints for aggregated trading metrics
-   Focus on market creation and order placement rather than analytical data
-   Lack of built-in functionality for user behavior analysis

Data Source Solution: Dune Analytics
------------------------------------

### Data Discovery

After consulting with the team, discovered Dune Analytics as a viable data source:

-   Access to curated Polymarket data tables
-   Primary table used: `polymarket_polygon.market_trades`
-   Rich dataset including transaction details, market information, and trade specifics

### Key Table Fields

`block_number, block_time, tx_hash, evt_index, action,
contract_address, condition_id, event_market_name,
question, polymarket_link, token_outcome, neg_risk,
asset_id, price, amount, shares, fee, maker, taker,
unique_key, token_outcome_name`

Data Processing Methodology
---------------------------

### Time-Based Analysis

Implemented hourly trading volume aggregation using SQL:

`WITH hourly_trades AS (
  SELECT
    DATE_TRUNC('hour', block_time) AS trade_hour,
    SUM(amount) AS total_amount_traded
  FROM polymarket_polygon.market_trades
  WHERE
    block_time >= TRY_CAST('2024-11-06' AS TIMESTAMP)
  GROUP BY 1
)`

### Market Categorization

Developed a comprehensive CASE statement system for market classification:

-   Politics & Elections (keywords: election, president, vote, etc.)
-   Sports (keywords: nba, nfl, premier league, etc.)
-   Crypto & Blockchain (keywords: bitcoin, ethereum, defi, etc.)
-   Technology & AI
-   Finance & Economy
-   Weather & Climate

### Data Pipeline

1.  SQL Query Execution on Dune
2.  Data Retrieval via Dune API
3.  Python Processing using Pandas
4.  Visualization using Plotly
5.  Analysis Documentation in Markdown

Technical Implementation
------------------------

### Data Collection

-   Utilized Dune's API for automated data retrieval
-   Implemented Python scripts for periodic data updates
-   Used query results identifier for consistent data access

### Visualization Stack

-   Primary tool: Plotly Express for interactive visualizations
-   Supporting libraries: Pandas for data manipulation
-   Dashboard: Streamlit for web interface


Development Environment
-----------------------

-   Local development on macOS
-   Python 3.9 virtual environment
-   Version control with Git
-   Package management via pip

Key Features
------------

1.  Real-time data updates via Dune API
2.  Interactive visualizations
3.  Modular code structure
4.  Comprehensive market categorization
5.  Detailed markdown analyses
6.  User-friendly dashboard interface
from dune_client.client import DuneClient
import plotly.express as px
import pandas as pd
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("DUNE_API_KEY")

def get_dune_client():
    return DuneClient(api_key)

def get_timezone_activity_plot():
    """
    Returns a bar chart of trading volume by UTC hour.
    (Query Result ID: 4647415)
    """
    dune = get_dune_client()
    query_result_1 = dune.get_latest_result(4647415)
    # Extract the rows (which is a list of dictionaries)
    data = query_result_1.result.rows
    # Convert to a DataFrame
    df = pd.DataFrame(data)
    
    # Create a bar chart using Plotly Express
    fig = px.bar(
        df,
        x='utc_hour',
        y='total_traded',
        labels={'utc_hour': 'UTC Hour', 'total_traded': 'Total Traded Volume ($)'},
        title='Trading Volume by UTC Hour',
        template='plotly_white'
    )
    # Customize the x-axis to display every hour (0 through 23)
    fig.update_xaxes(dtick=1)
    
    return fig

def get_market_attraction_plot():
    """
    Returns a donut (pie) chart of new users by market category,
    excluding the "Other" category.
    (Query Result ID: 4647796)
    """
    dune = get_dune_client()
    query_result_2 = dune.get_latest_result(4647796)
    # Extract the rows and convert to DataFrame
    data = query_result_2.result.rows
    df = pd.DataFrame(data)
    
    # Filter out the 'Other' category
    df_filtered = df[df['category'] != "Other"]
    
    # Create a donut chart using Plotly Express
    fig = px.pie(
        df_filtered,
        names='category',
        values='new_users',
        title='Distribution of New Users by Market Category (Excluding Other)',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4  # Creates the donut effect
    )
    # Display percentages and labels inside the chart slices
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    return fig

def get_user_activity_duration_plot():
    """
    Returns a funnel chart that visualizes how long new users stay active.
    (Query Result ID: 4648005)
    """
    dune = get_dune_client()
    query_result_3 = dune.get_latest_result(4648005)
    # Extract and convert the rows to a DataFrame
    data = query_result_3.result.rows
    df = pd.DataFrame(data)
    
    # Ensure active_day_bucket is treated as an ordered categorical variable
    df["active_day_bucket"] = pd.Categorical(
        df["active_day_bucket"],
        categories=["0-99", "100-199", "200-299", "300-399", "400-499", "500-599", "600-699", "700-799"],
        ordered=True
    )
    
    # Create a funnel chart using Plotly Express
    fig = px.funnel(
        df,
        y="active_day_bucket",
        x="user_count",
        title="User Retention: How Long Do New Users Typically Stay Active?",
        labels={"active_day_bucket": "Active Day Bucket", "user_count": "User Count"}
    )
    
    # Enhance the layout for a professional look
    fig.update_layout(
        template="plotly_white",
        title_font_size=20,
        yaxis_title="Active Day Bucket",
        xaxis_title="User Count"
    )
    
    return fig

def get_market_growth_plot():
    """
    Returns a line chart showing market growth over time,
    excluding the 'Other' category.
    (Query Result ID: 4648680)
    """
    dune = get_dune_client()
    query_result_4 = dune.get_latest_result(4648680)
    # Extract the rows and convert to a DataFrame
    data = query_result_4.result.rows
    df = pd.DataFrame(data)
    
    # Convert the 'date' column to datetime format (removing the ' UTC' part)
    df['date'] = pd.to_datetime(df['date'].str.replace(' UTC', ''))
    
    # Define the list of market columns to include (excluding 'other_volume')
    market_columns = ['crypto_volume', 'finance_volume', 'politics_volume', 'sports_volume', 'tech_volume', 'weather_volume']
    
    # Transform the DataFrame from wide to long format for the selected market columns
    df_long = df.melt(
        id_vars='date',
        value_vars=market_columns,
        var_name='market',
        value_name='volume'
    )
    
    # Create the line chart with one line per market category
    fig = px.line(
        df_long,
        x='date',
        y='volume',
        color='market',
        markers=True,
        title='Market Growth Over Time (Excluding Other)',
        labels={'date': 'Date', 'volume': 'Volume', 'market': 'Market Category'}
    )
    
    # Enhance layout for a professional appearance
    fig.update_layout(
        template='plotly_white',
        title_font_size=20,
        xaxis_title='Date',
        yaxis_title='Volume'
    )
    
    return fig

def get_retention_changes_plot():
    """
    Returns a grouped bar chart comparing pre- and post-election user retention by active day bucket.
    (Query Result ID: 4648910)
    
    Note: Although the function name is 'get_timezone_plot', this code uses the provided query for election-based user retention.
    """
    dune = get_dune_client()
    query_result_5 = dune.get_latest_result(4648910)
    # Extract the rows and convert to a DataFrame
    data = query_result_5.result.rows
    df = pd.DataFrame(data)
    
    # Reshape the DataFrame for a grouped bar chart
    df_long = df.melt(
        id_vars='active_day_bucket',
        value_vars=['pre_election_users', 'post_election_users'],  # pre first, then post
        var_name='election_period',
        value_name='user_count'
    )
    
    # Rename for clarity
    df_long['election_period'] = df_long['election_period'].replace({
        'pre_election_users': 'Pre-Election',
        'post_election_users': 'Post-Election'
    })
    
    # Ensure the categorical ordering: Pre-Election first, then Post-Election
    df_long['election_period'] = pd.Categorical(
        df_long['election_period'],
        categories=["Pre-Election", "Post-Election"],
        ordered=True
    )
    
    # Create a grouped bar chart using Plotly Express
    fig = px.bar(
        df_long,
        x='active_day_bucket',
        y='user_count',
        color='election_period',
        barmode='group',
        title='User Retention: Pre vs. Post Election by Active Day Bucket',
        labels={'active_day_bucket': 'Active Day Bucket', 'user_count': 'User Count', 'election_period': 'Election Period'},
        template='plotly_white'
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title='Active Day Bucket',
        yaxis_title='User Count'
    )
    
    return fig
import snowflake.connector
import streamlit as st

# Replace with your Snowflake credentials
conn = snowflake.connector.connect(
    user='lakshman798',
    password='Passw0rd@1982',
    account='RK81977',
    warehouse='COMPUTE_WH',
    database='DEV',
    schema='TEST'
)

# Get user role from session or external authentication
user_role = st.session_state.get('user_role')


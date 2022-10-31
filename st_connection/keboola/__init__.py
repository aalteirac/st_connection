import streamlit as st
from st_connection.keboola.keboola_connection import keboola

# Placing in st.connection for convenience
# Instantiate a connection with:
#    conn = st.connection.snowflake.connection.login()
# or
#    conn = st.connection.snowflake.connection.singleton()
# Instantiate a session with:
#    session = st.connection.snowflake.session.login()
# or
#    session = st.connection.snowflake.session.singleton()

st.connection.keboola_connection = keboola.connection

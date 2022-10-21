import streamlit as st
import st_connection.connection
from snowflake.connector import SnowflakeConnection, connect

# Implementation that creates Snowflake Connector connections
class SnowflakeConnectionImpl(st.connection.AbstractConnection):
    def __init__(self):
        pass

    def is_open(self, conn: SnowflakeConnection) -> bool:
        return not conn.is_closed()

    def connect(self, params) -> SnowflakeConnection:
        return connect(**params)
    
    def close(self, conn: SnowflakeConnection):
        conn.close()
    
    def ST_KEY(self):
        return 'ST_SNOW_CONN'
    
    def default_form_options(self):
        return {'account': '', 'user': '', 'password': None}


class snowflake:
    connection = st.connection.connection(SnowflakeConnectionImpl())

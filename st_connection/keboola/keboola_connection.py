import streamlit as st
import st_connection.connection
from kbcstorage.client import Client

# Implementation that creates Keboola Connector connections
class KeboolaConnectionImpl(st.connection.AbstractConnection):
    def __init__(self):
        pass

    def is_open(self,client:Client ) -> bool:
        try:    
            client.buckets.list() 
            return True
        except Exception as e:
            return False


    def connect(self, params):
        client = Client(params['URL'], params['Token'])
        try:    
            client.buckets.list() 
            return client
        except Exception as e:
            raise e
    
    def close(self,client):
        True
    
    def ST_KEY(self):
        return 'ST_KEBOOLA_CONN'
    
    def default_form_options(self):
        return {'URL': '', 'Token': None}


class keboola:
    connection = st.connection.connection(KeboolaConnectionImpl())

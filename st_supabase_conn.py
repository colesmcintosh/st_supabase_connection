from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client, Client
import streamlit as st
from typing import Union

class SupabaseConnection(ExperimentalBaseConnection[Client]):
    def __init__(self, **kwargs):
        super().__init__(connection_name='supabase')
        self.client = self._connect(**kwargs)

    def _connect(self, **kwargs) -> Client:
        """Creates Supabase Client and connection"""
        if 'supabase_url' in kwargs and 'supabase_key' in kwargs:
            url = kwargs.pop('supabase_url')
            key = kwargs.pop('supabase_key')
        else:
            url = self._secrets['supabase_url']
            key = self._secrets['supabase_key']
        return create_client(url, key)

    def get_client(self) -> Client:
        """Returns the Supabase Client Object"""
        return self.client

    def insert(self, table_name: str, data: Union[dict, list]):
        """Inserts data into a table."""
        if isinstance(data, list):
            for item in data:
                return self.client.table(table_name).insert(item).execute()
        else:
            return self.client.table(table_name).insert(data).execute()

    def update(self, table_name: str, data: Union[dict, list], where_field: str, where_value: str):
        """Updates data in a table."""
        if isinstance(data, list):
            for item in data:
                return self.client.table(table_name).update(item).eq(where_field, where_value).execute()
        else:
            return self.client.table(table_name).update(data).eq(where_field, where_value).execute()

    def select(self, table_name: str, columns: str, where_field: str = None, where_value: str = None):
        """Selects data from a table."""
        return self.client.table(table_name).select(columns).eq(where_field, where_value).execute().data if where_field == None and where_value == None else self.client.table(table_name).select(columns).execute().data

    def delete(self, table_name: str, where_field: str, where_value: str):
        """Deletes data from a table."""
        return self.client.table(table_name).delete().eq(where_field, where_value).execute()





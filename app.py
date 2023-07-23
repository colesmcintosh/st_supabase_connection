import streamlit as st
from st_supabase_conn import SupabaseConnection

st.set_page_config(
    page_title='Supabase Data Connector',
    page_icon='🦸‍♂️'
)

"# 🦸‍♂️ Supabase Data Connector"

"""
This app demonstrates the use of `st.experimental_connection` 
with `SupabaseConnection` to perform different operations on a Supabase database with Streamlit.
"""

# Initialize the connection
conn = st.experimental_connection('supabase', type=SupabaseConnection)


# Input for table name
table_name = "test_table"

insert_tab, select_tab, update_tab, delete_tab, get_client_tab = st.tabs(['Insert Demo', 'Select Demo', 'Update Demo', 'Delete Demo', 'Client Demo'])

# Section for INSERT operation
with insert_tab:
    with st.expander('Sample JSON to insert'):
        st.json("""{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30
}
""")

    insert_data = st.text_area("Enter the data to insert (in JSON format)")
    if st.button("Insert data"):
        with st.spinner('Inserting...'):
            data = eval(insert_data)
            result = conn.insert(table_name, data)
            st.success('Successful Insertion', icon="🔥")

# Section for SELECT operation
with select_tab:
    select_columns = st.text_input("Enter the columns to select (comma separated) or * to select all")
    select_where_field = st.text_input("Enter the field for the WHERE clause", key='select_where_field')
    select_where_value = st.text_input("Enter the value for the WHERE clause", key='select_where_value')
    if st.button("Select data"):
        with st.spinner('Fetching...'):
            result = conn.select(table_name, select_columns, select_where_field, select_where_value)
            st.table(result)
            st.success("Successful Query", icon="🎉")

# Section for UPDATE operation
with update_tab:
    with st.expander('Sample JSON to update'):
        update_json = {
    "id": "1",
    "name": "Jane Doe",
    "email": "janedoe@example.com"
}
        st.json(update_json)
                
    update_data = st.text_area("Enter the data to update (in JSON format)")
    update_where_field = st.text_input("Enter the field for the WHERE clause", key='update_where_field')
    update_where_value = st.text_input("Enter the value for the WHERE clause", key='update_where_value')
    if st.button("Update data"):
        with st.spinner('Updating...'):
            data = eval(update_data)
            result = conn.update(table_name, data, update_where_field, update_where_value) if update_where_field and update_where_value else conn.update(table_name, data, "id", update_json['id'])
            st.success('Successful Update', icon="✅")

# Section for DELETE operation
with delete_tab:
    st.warning('You must provide a WHERE field and value!', icon="📍")
    delete_where_field = st.text_input("Enter the field for the WHERE clause", key='delete_where_field', )
    delete_where_value = st.text_input("Enter the value for the WHERE clause", key='delete_where_value')
    if st.button("Delete data"):
        if delete_where_field and delete_where_value:
            with st.spinner('Deleting...'):
                result = conn.delete(table_name, delete_where_field, delete_where_value)
                st.success(f'Successful Deletion of record with {delete_where_field} value of {delete_where_value}', icon="❌")
        else:
            st.error('You must provide a WHERE field and value!', icon="📍")

with get_client_tab:
    if st.button("Get Client"):
        with st.spinner('Getting Client...'):
            result = conn.get_client()
            st.write(result)
            st.success('Successfully retrieved client object', icon='🤖')
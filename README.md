# Streamlit-Supabase Connection

Streamlit-Supabase Connection is a Python library for connecting to a Supabase database using Streamlit's `experimental_connection` function. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage

> You can (and probably should) provide your Supabase URL and key in a secrets.toml file instead of hard coding it in

```python
from st_supabase_conn import SupabaseConnection

# Initialize connection
conn = SupabaseConnection(supabase_url="Your Supabase URL", supabase_key="Your Supabase Key")

"""
conn = SupabaseConnection()

^^^ If you provide the values in a secrets.toml file you can initialize it like this ^^^
"""

# Insert data
conn.insert("table_name", {"key": "value"})

# Update data
conn.update("table_name", {"key": "updated_value"}, "id", 1)

# Select data
data = conn.select("table_name", "*")

# Delete data
conn.delete("table_name", "id", 1)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
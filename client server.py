import requests
import pandas as pd
from io import StringIO

symbol = "INFY.NS"
start = "2020-10-01"
end = "2025-10-30"

url = f"http://127.0.0.1:8000/stock/{symbol}/csv?start={start}&end={end}"
response = requests.get(url)

if response.ok:
    df = pd.read_csv(StringIO(response.text))
    print(df.head())
else:
    print("Error:", response.text)

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

print(df)

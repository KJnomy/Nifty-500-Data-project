from fastapi import FastAPI, Response
import yfinance as yf
import pandas as pd
from datetime import datetime
import os

app = FastAPI()

SAVE_DIR = "stock_data"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.get("/stock/{symbol}/csv")
def get_stock_data(symbol: str, start: str = "2020-01-01", end: str = None):
    
    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")

    try:
        data = yf.download(symbol, start=start, end=end)
        if data.empty:
            return {"error": f"No data found for {symbol}"}

        csv_data = data.to_csv()
        file_path = os.path.join(SAVE_DIR, f"{symbol}_{start}_to_{end}.csv")
        data.to_csv(file_path)

        return Response(content=csv_data, media_type="text/csv")

    except Exception as e:
        return {"error": str(e)}


'''
now for starting the Fastapi you have to type a command in new terminal as
uvicorn {filename}:app --reload      
{filename} is name which you have saved of the file
 
'''



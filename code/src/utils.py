import pandas as pd
import json
from openai import OpenAI
from io import StringIO

def load_transactions(file_path):
    return pd.read_csv(file_path)

def normalize_transactions(transactions):
    # Normalize only the 'amount' column
    transactions['amount'] = (transactions['amount'] - transactions['amount'].mean()) / transactions['amount'].std()
    return transactions

def save_anomalies(anomalies, output_file):
    anomalies.to_csv(output_file, index=False)

def detect_anomalies(transactions, api_key):
    
    client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key=api_key,
    )
    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
        {
        "role": "user",
        "content": f"Detect anomalies in below historical csv data where match status is Break and reason out the why anomaly has come and store against column 'anomaly reason' for each occurrence :\n{transactions.to_csv(index=False)}"
        }
        ]
    )
    
    if not completion.choices:
        raise ValueError("No choices returned from the API")

    #print(completion.choices)

    anomalies = completion.choices[0].message.content
    anomalies_df = pd.read_csv(StringIO(anomalies))
    return anomalies_df
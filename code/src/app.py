#import os
from utils import load_transactions, normalize_transactions, save_anomalies, detect_anomalies

def main():
    input_file = 'src/data/enhanced_mismatch_data.csv'
    output_file = 'src/data/anomalies.csv'
    api_key = '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' # os.getenv('OPENAI_API_KEY') 

    transactions = load_transactions(input_file)
    #print(transactions)
   # normalized_transactions = normalize_transactions(transactions)
    anomalies = detect_anomalies(transactions, api_key)
    save_anomalies(anomalies, output_file)

if __name__ == "__main__":
    main()
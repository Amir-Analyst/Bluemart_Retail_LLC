"""
BlueMart Data Processing Pipeline
Refactored for Industry Standards
"""

import pandas as pd
import numpy as np
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def process_data():
    print("Starting Data Processing...")
    
    # 1. Load Master Data (Small enough for memory)
    try:
        print("   Loading master data...")
        skus = pd.read_csv(config.FILE_SKUS)
        stores = pd.read_csv(config.FILE_STORES)
        promos = pd.read_csv(config.FILE_PROMOTIONS, parse_dates=['start_date', 'end_date'])
    except FileNotFoundError as e:
        print(f"Error loading files: {e}")
        print("   Please run scripts/generate_data.py first.")
        return

    # Pre-process promos for faster lookup
    promos = promos.sort_values('start_date')
    promo_lookup = {}
    for _, row in promos.iterrows():
        for d in pd.date_range(row['start_date'], row['end_date']):
            promo_lookup[d] = row['promo_name']

    # Initialize aggregation containers
    partial_aggregates = []
    
    # Global metrics counters
    global_metrics = {
        "total_revenue": 0.0,
        "total_profit": 0.0,
        "total_quantity": 0,
        "count": 0
    }
    
    chunk_size = 100000
    print(f"   Processing sales data in chunks of {chunk_size}...")
    
    try:
        # Process Sales in Chunks
        chunk_iter = pd.read_csv(config.FILE_SALES, chunksize=chunk_size)
        
        for i, chunk in enumerate(chunk_iter):
            # Merge
            chunk = chunk.merge(skus, on='sku_id', how='left').merge(stores, on='store_id', how='left')
            
            # Feature Engineering
            chunk['date'] = pd.to_datetime(chunk['date'], errors='coerce')
            # Drop rows with invalid dates
            chunk = chunk.dropna(subset=['date'])
            chunk['promo_name'] = chunk['date'].map(promo_lookup).fillna('No Promotion')
            chunk['month'] = chunk['date'].dt.month_name()
            chunk['year'] = chunk['date'].dt.year
            chunk['revenue'] = chunk['total_value']
            chunk['profit'] = chunk['revenue'] - (chunk['cost_price'] * chunk['quantity'])
            
            # Update Global Metrics
            global_metrics["total_revenue"] += chunk['revenue'].sum()
            global_metrics["total_profit"] += chunk['profit'].sum()
            global_metrics["total_quantity"] += int(chunk['quantity'].sum())
            global_metrics["count"] += len(chunk)
            
            # Partial Aggregation for Dashboard
            # Group by key dimensions to reduce size immediately
            grouped_chunk = chunk.groupby(
                ['date', 'month', 'year', 'store_id', 'store_name', 'category', 'channel', 'sku_id', 'sku_name']
            ).agg(
                revenue=('revenue', 'sum'),
                profit=('profit', 'sum'),
                quantity=('quantity', 'sum')
            ).reset_index()
            
            partial_aggregates.append(grouped_chunk)
            
            if (i + 1) % 5 == 0:
                print(f"   Processed {i + 1} chunks...")
                
    except FileNotFoundError:
         print(f"Error: {config.FILE_SALES} not found.")
         return

    # 4. Final Aggregation
    print("   Performing final aggregation...")
    if not partial_aggregates:
        print("No data processed.")
        return

    full_df = pd.concat(partial_aggregates)
    dashboard_df = full_df.groupby(
        ['date', 'month', 'year', 'store_id', 'store_name', 'category', 'channel', 'sku_id', 'sku_name']
    ).agg(
        revenue=('revenue', 'sum'),
        profit=('profit', 'sum'),
        quantity=('quantity', 'sum')
    ).reset_index()
    
    # 5. Save Summary Metrics
    print("   Calculating final global metrics...")
    summary_metrics = {
        "total_revenue": float(global_metrics["total_revenue"]),
        "total_profit": float(global_metrics["total_profit"]),
        "total_quantity": int(global_metrics["total_quantity"]),
        "avg_revenue_per_order": float(global_metrics["total_revenue"] / global_metrics["count"]) if global_metrics["count"] > 0 else 0,
        "avg_profit_per_order": float(global_metrics["total_profit"] / global_metrics["count"]) if global_metrics["count"] > 0 else 0
    }
    
    import json
    print(f"Saving summary metrics to {config.FILE_SUMMARY_METRICS}")
    with open(config.FILE_SUMMARY_METRICS, 'w') as f:
        json.dump(summary_metrics, f)
    
    # 6. Save Dashboard Data
    print(f"Saving processed data to {config.FILE_DASHBOARD_DATA}")
    dashboard_df.to_csv(config.FILE_DASHBOARD_DATA, index=False)
    print("Data Processing Complete!")

if __name__ == "__main__":
    process_data()

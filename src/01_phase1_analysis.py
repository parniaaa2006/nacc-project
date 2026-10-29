import pandas as pd
df_uds = pd.read_csv("data/raw/udslong_imputed.csv")
rows, cols = df_uds.shape
print(f"Total Rows (Observations): {rows:,}")
print(f"Total Columns (Variables): {cols}\n")
print("--- Column Details ---")
for i, col in enumerate(df_uds.columns, 1):
    data_type = df_uds[col].dtype
    sample_val = df_uds[col].iloc[0] if rows > 0 else "N/A"
    print(f"{i:03d}. {col:<30} | Type: {str(data_type):<10} | Sample: {sample_val}")



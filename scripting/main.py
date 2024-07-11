import pandas as pd

# Load CSV files
df_a = pd.read_csv('branch_a.csv')
df_b = pd.read_csv('branch_b.csv')
df_c = pd.read_csv('branch_c.csv')

# Menggabungkan semua dataframes
df = pd.concat([df_a, df_b, df_c])

# Hapus baris NaN pada 'transaction_id', 'date', and 'customer_id'
df = df.dropna(subset=['transaction_id', 'date', 'customer_id'])

# Convert 'date' kolom ke datetime format
df['date'] = pd.to_datetime(df['date'])

# Hapus duplikat berdasarkan pada 'transaction_id', pilih berdasarkan 'date' terbaru
df = df.sort_values('date').drop_duplicates(subset='transaction_id', keep='last')

# Hitung total penjualan tiap cabang
df['total_sales'] = df['quantity'] * df['price']
total_sales_per_branch = df.groupby('branch')['total_sales'].sum().reset_index()

# Simpan hasil ke CSV file yang baru
total_sales_per_branch.to_csv('total_sales_per_branch.csv', index=False)

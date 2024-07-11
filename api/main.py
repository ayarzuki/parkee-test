import requests
import pandas as pd

# Fungsi untuk mendapatkan data dari API berdasarkan negara
def get_universities_data(country):
    url = f'http://universities.hipolabs.com/search?country={country}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Mendapatkan data dari API untuk negara 'United States'
data = get_universities_data('United States')

# Membuat DataFrame dari data yang didapatkan
df = pd.DataFrame(data)

# Memilih kolom yang diinginkan
df = df[['name', 'web_pages', 'country', 'domains', 'state-province']]

# Mengganti nama kolom 'state-province' menjadi 'state_province'
df.rename(columns={'state-province': 'state_province'}, inplace=True)

# Menyaring data yang tidak memiliki data 'state_province'
filtered_df = df[df['state_province'].notna()]

# Menampilkan DataFrame yang sudah difilter
print(filtered_df)

# Menyimpan hasil ke file CSV
filtered_df.to_csv('universities_with_state_province.csv', index=False)

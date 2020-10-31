print('\nData dikirimkan oleh server gojek')
data_dari_server_gojek = {
    'tanngal':'2020-10-31',
    'driver list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 100},
        {'nama': 'tri', 'jarak': 300},
        {'nama': 'tri', 'jarak': 1000},
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver list']}")
print(f"Driver #1 {data_dari_server_gojek['driver list'][0]}")
print(f"Driver #1 {data_dari_server_gojek['driver list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver list'][0]['jarak']} meter")

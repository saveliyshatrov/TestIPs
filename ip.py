import pandas as pd

f = open('hits.txt', 'r').read()
array = f.split('\n')

ip_addresses = []

array = list(filter(None, array))  # Удаление пустых значений
for i in range(len(array)):
    ip_addresses.append(array[i].split('\t')[1])


d = pd.Series(ip_addresses).value_counts()
print(d)
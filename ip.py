f = open('hits.txt', 'r').read()
array = f.split('\n')

ip_addresses = []

dict_of_ip = {}

array = list(filter(None, array))  # Удаление пустых значений
for i in range(len(array)):
    ip_addresses.append(array[i].split('\t')[1])

Dict = {}
for i in range(len(ip_addresses)):
    if str(ip_addresses[i]) not in Dict:
        Dict.update( { ip_addresses[i]: 0 } )
        Dict[ip_addresses[i]] += 1
    else:
        Dict[ip_addresses[i]] += 1

a = sorted(Dict.items(), key=lambda x: x[1], reverse=True)    

for i in range(5):
    print(a[i][0], '--------', a[i][1])

#есть вариант еще через Pandas
#import pandas as pd
#d = pd.Series(ip_addresses).value_counts(sort = True)
#print(d)
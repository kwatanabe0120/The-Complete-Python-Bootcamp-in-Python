price_lookup = {'Orenge':1.23, 'Cake': 1, 'Apple':'Will be decided later'}

print(price_lookup['Cake'])

test = {'test':100, 'list':[1,2,3,4,12.54,'wooow'], 'dic':{'insidekry':'really? can you?','test':14124123}}
print(test['list'][5])
print(test['dic']['insidekry'])

listtest = {'test':['a','b','c']}
print(listtest['test'][2].upper())

update = {'k1':100,'k2':200,'k3':300}
update['k4']=400
print(update)

update['k4']=124312412
print(update)

print(update.keys())
print(update.values())
print(update.items())

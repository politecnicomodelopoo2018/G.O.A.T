from Aerolinea import Arolinea
import json

A = Arolinea()
A.JSON()
A.Ejerecicios()
algo = json.dumps(A.Diccionario)
print(A.Diccionario)
with open('algo.json','w') as f:
   f.write(algo)

for a in A.Vuelos:
   for b in a.pasajeros:
      print(b.Dni)
   print('----------------')


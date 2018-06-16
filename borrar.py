import json


dic = {'Vuelos':
  [
    {
      'avion': 'A1',
      'fecha': '2018-03-30',
      'hora': '12:00',
      'origen': 'Buenos Aires',
      'destino': 'Atlanta',
      "tripulacion": ["3","5","6","7"],
      "pasajeros": ["1","2","17","15"]
    }
  ]
}

algo = json.dumps(dic)
with open('algo.algo','w') as f:
    f.write(algo)

with open('algo.algo', 'r') as f:
    aux1 = f.read()

    aux2 = json.loads(aux1)

print(aux2)
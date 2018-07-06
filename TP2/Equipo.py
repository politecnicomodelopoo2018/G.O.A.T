class equipo():

    id_equipo = None
    liga = None
    fundacion = None


    def __init__(self,id,l,f):
        self.id_equipo=id
        self.liga=l
        self.fundacion=f

    def insert(self):
        db.connect()
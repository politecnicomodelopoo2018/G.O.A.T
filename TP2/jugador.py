from persona import persona
class jugador(persona):
    posicion = None

    def __init__(self,d,n,a,s,f,na,e,p):
        persona.__init__(d,n,a,s,f,na,e)
        self.posicion=p

    def mostrarAll(self,equipo):
        a = db.connect("select * from Jugador where Equipo.Nombre = %s join Equipo on Id_Equipo = Jugador.Equipo;",(equipo))
        lista = []
        for b in a:
            c = jugador(b['Dni'],b['Nombre'],b['Apellido'],b['Sueldo'],b['Fecha_nac'],b['Nacionalidad'],b[])

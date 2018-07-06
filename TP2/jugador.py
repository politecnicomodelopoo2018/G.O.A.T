from persona import persona
class jugador(persona):
    posicion = None

    def __init__(self,d,n,a,s,f,na,e,p):
        persona.__init__(d,n,a,s,f,na,e)
        self.posicion=p


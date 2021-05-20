from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

openclubs = open('data/datos_clubs.txt', 'r', encoding='utf-8')
    
#Ingreso de los clubes de la dirección [data/datos_clubs.txt]
for c in openclubs:
    texto_club = c.split(";")
    texto_club[-1] = texto_club[-1].strip()
    session.add(Club(nombre=texto_club[0], deporte=texto_club[1], fundacion=texto_club[-1]))
    
consultaClub = session.query(Club).all()

openjugadores = open('data/datos_jugadores.txt', 'r', encoding='utf-8')

# Ingreso de los jugadores de la dirección [data/datos_jugadores.txt]
for j in openjugadores:
    texto_jug = j.split(";")
    texto_jug[-1] = texto_jug[-1].strip()
    
    for club in consultaClub:
        if(texto_jug[0] == club.nombre):
            id_club = club.id
            
    session.add(Jugador(nombre=texto_jug[3], dorsal=texto_jug[2], posicion=texto_jug[1], club_id= id_club))
   
session.commit()

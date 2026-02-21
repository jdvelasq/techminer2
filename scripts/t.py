text = """Acevedo Cacua, Santiago
Arango Villa, Santiago
ARBELAEZ URIBE, JUAN FELIPE
ARDILA FRANCO, PAULA ANDREA
BALLESTEROS LORA, RUBER
Barrios Molina, Mariana
Benavides Zabala, Obeimar Jose
BETANCOURT URIBE, ELISA
BRAVO CASTILLO, BANY
Burbano Ortega, Ronald Camilo
Buritica Garcia, Arley
Cadavid Arango, Juan Esteban
Calle Becerra, Juan Felipe
CARVAJAL LONDOÑO, MARIA ISABEL
Castilla Ospina, Santiago Jose
Córdoba Jiménez, Juan Pablo
CORREA OCAMPO, JOHAN EDUARDO
Cortes Camacho, Maribel
Cortés Montoya, Simón David
Cossio Vergara, Jesus David
DAZA ALVAREZ, ARTURO ALEJANDRO
ESTRADA GRISALES, DAVID
Flórez González, Johan Camilo
García Díaz, Simón
Garcia Morales, Jeiner Jose
Garcia Roldan, Tomas
Giraldo Toro, Daniel
Gonzalez Jimenez, Mateo
Henao Ceballos, Yesica Andrea
HERNANDEZ CIFUENTES, STIVEN
Hernandez Noriega, Maria Clara
HURTADO MARTÍNEZ, JUAN CARLOS
JARAMILLO PABON, DANIEL
JIMENEZ PATIÑO, JAIME ALONSO
Marin Montoya, Juan Pablo
MEJIA LOPEZ, SANTIAGO
MENDOZA GALLEGO, DANIEL
MOLINA MORILLO, JORGE LUIS
MONTIEL ACEVEDO, JUAN SEBASTIAN
MONTOYA PEREZ, SERGIO
MORA FERNANDEZ, LINA JULIANA
Muñoz Alarcón, María Alejandra
NAVARRO ESPINOSA, DANIEL ESTEBAN
PABON VELASCO, CAMILO ANDRES
Pérez Zea, Verónica
Pineda Orozco, Sergio Alejandro
Ramírez Ramírez, Isabel Cristina
RESTREPO YUSTI, DAVID
RODRIGUEZ RODRIGUEZ, JESUS DANIEL
Sanchez Mata, Hinara Pastora
SÁNCHEZ RESTREPO, JUAN MANUEL
Sanchez Villota, Juan Pablo
Sanchez Zuluaga, Juan Sebastian
SUAREZ GUZMAN, PAULA ANDREA
TORRES MUÑOZ, FREDY ANDRÉS
Uribe Cadavid, Juan David
VALENCIA QUINTERO, BRAYAN
Varela Ojeda, Luis Alejandro
Varela Vanegas, Santiago 
Vasquez Correa, Juan Esteban
VILLA ALZATE, DAVID
VILLARRAGA FRANCO, MIGUEL ÁNGEL
VILLARREAL MÁRQUEZ, JORGE ALFREDO"""

text = (
    text.lower()
    .replace("á", "a")
    .replace("é", "e")
    .replace("í", "i")
    .replace("ó", "o")
    .replace("ú", "u")
    .replace("ñ", "n")
    .split("\n")
)

text = [t.split(", ")[1] + " " + t.split(", ")[0] for t in text]

print("\n".join(text))

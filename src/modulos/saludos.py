def saludar():
  print("Hola, saludos desde saludos.saludar()")

class Saludo:
  def __init__(self):
    print("Hola, te saludos desde Saludo.init")

# Asi evitamos que se pueda ejecutar algo de este modulo, a menos que se quiera ejecutar intencionalmente
if __name__ == "__main__":
  saludar()

# imprime el nombre del modulo actual (saludos)
# print(__name__)
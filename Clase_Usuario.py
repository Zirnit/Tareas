import re

letraRegex = re.compile(r"[a-z]")
mayuscRegex = re.compile(r"[A-Z]")
numeroRegex = re.compile(r"\d")
caracterRegex = re.compile(r"[!#$%&/()=?_@]")

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 16 >= len(password) >= 8 and len(numeroRegex.findall(password)) > 0 and len(caracterRegex.findall(password)) > 0 or len(mayuscRegex.findall(password)) > 0:
            return True
        else:
            return False

    def login(self,password):
        if password == self.password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contraseña):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña

    def get_correo(self):
        return self.__correo
    def get_contraseña(self):
        return self.__contraseña
    def get_nombre(self):
        return self.__nombre
    def get_id(self):
        return self.__id_usuario
    
    # Método para verificar contraseña
    def verificar_contraseña(self, contraseña):
        return self.__contraseña == contraseña 
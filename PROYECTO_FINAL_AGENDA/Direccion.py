#Clase Direccion

class Direccion:
    def __init__(self,calle, piso, ciudad, codigo_Postal):
        self._calle = calle
        self._piso = piso
        self._ciudad = ciudad
        self._codigo_Postal = codigo_Postal
    
    def get_calle(self):
        return self._calle
    
    def set_calle(self, calle):
        self._calle = calle

    def get_piso(self):
        return self._piso
    
    def set_piso(self, piso):
        self._piso = piso

    def get_ciudad(self):
        return self._ciudad
    
    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def get_codigo_Postal(self):
        return self._codigo_Postal
    
    def set_codigo_Postal(self, codigo_Postal):
        self._codigo_Postal = codigo_Postal





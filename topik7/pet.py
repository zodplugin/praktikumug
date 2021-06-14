class Pet():
    def __init__(self,nama,jenis,umur):
        self.__nama = nama
        self.__jenis = jenis
        self.__umur = umur
    def set_nama(self,nama):
        self.__nama = nama
    def set_jenis(self,jenis):
        self.__jenis = jenis
    def set_umur(self,umur):
        self.__umur = umur
    def get_nama(self):
        return self.__nama
    def get_jenis(self):
        return self.__jenis
    def get_umur(self):
        return self.__umur

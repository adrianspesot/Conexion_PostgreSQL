from os import system
from logger_base import log
from psycopg2 import pool #importamos la clase de pool desde psycopg2
class Conexion:
    #Los siguientes son ATRIUBUTOS DE CLASE
    _DATABASE = 'EjercicioPersona'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1' #o localhost
    '''Las siguientes variables por para el pool de conexiones'''
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    ''''Configuramos el pool de conexiones'''
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                        host = cls._HOST,
                                                        user = cls._USERNAME,
                                                        password = cls._PASSWORD,
                                                        port = cls._DB_PORT,
                                                        database = cls._DATABASE)
                log.debug(f'Creacion Exitosa del Pool: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener pool: {e}')
                system.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn() #getconn se encarga de regresar un
        #objeto de conexion a la base de datos
        log.debug(f'Conexion Obtenida de Pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion) #liberamos conexiones que ya no esten en uso
        log.debug(f'Regresamos la conexion al Pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() # cerramos todas las conexiones
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
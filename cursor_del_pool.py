from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor() #Obtenemos cursor
        return self._cursor #retornamos a cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion: #esto pregunta si es ditinto a None
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit() #guardamos todos los cambios en la database
            log.debug('Commit de la transaccion')

        self._cursor.close() #cerramos el cursor y luego liberamos la conexion
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('DENTRO DEL BLOQUE WITH')
        cursor.execute('DELETE FROM personas WHERE id_persona = 12')
        #log.debug(cursor.fetchall()) # este va solo en SELECT

from usuario import Usuario
from conexion import Conexion
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario (username, password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuarios Insertados: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuarios Actualizados: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuarios Eliminados: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    '''Insertar Objetos'''
    # usuario1 = Usuario(username='fluffly',password=5432)
    # usuarios_insertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuario Insertado: {usuarios_insertados}')

    ''''Actualizar objetos'''
    usuario2 = Usuario(username='pit',password='253697',id_usuario=5)
    usuarios_actualizados = UsuarioDAO.actualizar(usuario2)
    log.debug(f'Usuario Actualizado: {usuarios_actualizados}')

    '''Eliminar Registro'''
    # usuario3= Usuario(id_usuario= 2)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario3)
    # log.debug(f'Persona eliminada: {usuarios_eliminados}')

    '''Seleccionar Objetos'''
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
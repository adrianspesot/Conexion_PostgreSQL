from usuario import Usuario
from usuario_DAO import UsuarioDAO
from logger_base import log
opcion = None
while opcion != 5: #distinto de 5 porque 5 es salir 
    print('''Opciones:
    1. Listar Usuarios
    2. Agregar Usuario
    3. Modificar Usuario
    4. Eliminar Usuario
    5. Salir
    ''')

    opcion = int(input(f'Escribe tu opcion (1-5): '))

    if opcion == 1: #listar usuarios
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.debug(usuario)
    elif opcion ==2: #Ingresar usuario
        usuario = input('Escribe el nombre de usuario: ')
        contrasenia = input('Escribe la contraseña: ')
        usuarios_insertados = UsuarioDAO.insertar(Usuario(username=usuario, password= contrasenia))
        print(f'Usuario Insertado: {usuarios_insertados}')
    elif opcion ==3: #Actualizar
        idusuario = input('Escribe id_usuario a modificar: ')
        usuario = input('Escribe el nuevo nombre de usuario: ')
        contrasenia = input('Escribe la nueva contraseña: ')
        usuarios_actualizados = UsuarioDAO.actualizar(Usuario(username=usuario, password= contrasenia,id_usuario=idusuario))
        print(f'Usuario Insertado: {usuarios_actualizados}')
    elif opcion == 4: # Eliminar
        idusuario = input('Escribe id_usuario a eliminar: ')
        usuarios_eliminados = UsuarioDAO.eliminar(Usuario(id_usuario=idusuario))
        print(f'Persona eliminada: {usuarios_eliminados}')
    elif opcion == 5:
        pass
    else:
        print('La opcion ingresada no es correcta, vuelva a ejecutar el programa e ingrese una opcion del 1 al 5')    

else: 
    log.info('SALIMOS DE LA APLICACION')
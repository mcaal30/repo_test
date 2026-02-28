from app.services.usuario_service import UsuarioService

service = UsuarioService()

usuario = service.crear_usuario("Max")
#print(usuario)

print(service.obtener_usuarios())
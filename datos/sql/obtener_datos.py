from datos.sql.conexion import sesion
from modelos.modelos import User


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    return listado_objetos
    
def obtener_user_por_id(id):
    return sesion.query(User).filter_by(id=id).first()

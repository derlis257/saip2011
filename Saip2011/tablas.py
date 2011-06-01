#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

engine = create_engine('postgresql://postgres:admin@localhost/postgres')
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

try:
    from sqlalchemy.dialects.postgresql import *
except ImportError:
    from sqlalchemy.databases.postgres import *
TB_equipo_rol = Table(u'TB_equipo_rol', metadata,
    Column(u'id_equipo', INTEGER(), ForeignKey('Tabla_EquipoDesarrollo.id_equipo')),
    Column(u'id_rol', INTEGER(), ForeignKey('Tabla_Rol.id_rol')),
)

TB_equipo_usuario = Table(u'TB_equipo_usuario', metadata,
    Column(u'id_equipo', INTEGER(), ForeignKey('Tabla_EquipoDesarrollo.id_equipo')),
    Column(u'id_usuario', INTEGER(), ForeignKey('Tabla_Usuario.id_usuario')),
)

TB_item_adjunto = Table(u'TB_item_adjunto', metadata,
    Column(u'id_item', INTEGER(), ForeignKey('Tabla_Item.id_item')),
    Column(u'id_adjunto', INTEGER(), ForeignKey('Tabla_Adjunto.id_adjunto')),
)

TB_proyecto_equipo = Table(u'TB_proyecto_equipo', metadata,
    Column(u'id_proyecto', INTEGER(), ForeignKey('Tabla_Proyecto.id_proyecto')),
    Column(u'id_equipo', INTEGER(), ForeignKey('Tabla_EquipoDesarrollo.id_equipo')),
)

TB_proyecto_fases = Table(u'TB_proyecto_fases', metadata,
    Column(u'id_proyecto', INTEGER(), ForeignKey('Tabla_Proyecto.id_proyecto')),
    Column(u'id_fase', INTEGER(), ForeignKey('Tabla_Fase.id_fase')),
)

TB_rol_privilegios = Table(u'TB_rol_privilegios', metadata,
    Column(u'id_rol', INTEGER(), ForeignKey('Tabla_Rol.id_rol')),
    Column(u'id_privilegio', INTEGER(), ForeignKey('Tabla_Privilegios.id_privilegio')),
)

tg_group_permission = Table(u'tg_group_permission', metadata,
    Column(u'group_id', INTEGER(), ForeignKey('tg_group.group_id')),
    Column(u'permission_id', INTEGER(), ForeignKey('tg_permission.permission_id')),
)

tg_user_group = Table(u'tg_user_group', metadata,
    Column(u'user_id', INTEGER(), ForeignKey('tg_user.user_id')),
    Column(u'group_id', INTEGER(), ForeignKey('tg_group.group_id')),
)

class TablaAdjunto(DeclarativeBase):
    __tablename__ = 'Tabla_Adjunto'

    #column definitions
    id_adjunto = Column(u'id_adjunto', INTEGER(), primary_key=True, nullable=False)
    text = Column(u'text', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaEquipoDesarrollo(DeclarativeBase):
    __tablename__ = 'Tabla_EquipoDesarrollo'

    #column definitions
    id_equipo = Column(u'id_equipo', INTEGER(), primary_key=True, nullable=False)

    #relation definitions


class TablaFase(DeclarativeBase):
    __tablename__ = 'Tabla_Fase'

    #column definitions
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    estado = Column(u'estado', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    id_fase = Column(u'id_fase', INTEGER(), primary_key=True, nullable=False)
    nombre_fase = Column(u'nombre_fase', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaHistorial(DeclarativeBase):
    __tablename__ = 'Tabla_Historial'

    #column definitions
    creado_por = Column(u'creado_por', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    fecha_creacion = Column(u'fecha_creacion', TIMESTAMP(timezone=False))
    id_Item = Column(u'id_Item', INTEGER(), nullable=False)
    id_historial = Column(u'id_historial', INTEGER(), primary_key=True, nullable=False)
    version = Column(u'version', INTEGER(), nullable=False)

    #relation definitions


class TablaItem(DeclarativeBase):
    __tablename__ = 'Tabla_Item'

    #column definitions
    adjunto = Column(u'adjunto', INTEGER())
    campos = Column(u'campos', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    complejidad = Column(u'complejidad', INTEGER(), nullable=False)
    creado_por = Column(u'creado_por', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    estado = Column(u'estado', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    fase = Column(u'fase', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    fecha_creacion = Column(u'fecha_creacion', TIMESTAMP(timezone=False))
    id_item = Column(u'id_item', INTEGER(), primary_key=True, nullable=False)
    lista_item = Column(u'lista_item', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    nombretipo = Column(u'nombretipo', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), ForeignKey('Tabla_TipoItem.nombre_tipo'))
    proyecto = Column(u'proyecto', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaLineaBase(DeclarativeBase):
    __tablename__ = 'Tabla_LineaBase'

    #column definitions
    estado = Column(u'estado', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    fecha_creacion = Column(u'fecha_creacion', TIMESTAMP(timezone=False))
    id_linea_base = Column(u'id_linea_base', INTEGER(), primary_key=True, nullable=False)

    #relation definitions


class TablaPrivilegio(DeclarativeBase):
    __tablename__ = 'Tabla_Privilegios'

    #column definitions
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    id_privilegio = Column(u'id_privilegio', INTEGER(), primary_key=True, nullable=False)
    nombre_privilegio = Column(u'nombre_privilegio', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaProyecto(DeclarativeBase):
    __tablename__ = 'Tabla_Proyecto'

    #column definitions
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    id_proyecto = Column(u'id_proyecto', INTEGER(), primary_key=True, nullable=False)
    nombre_proyecto = Column(u'nombre_proyecto', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaRol(DeclarativeBase):
    __tablename__ = 'Tabla_Rol'

    #column definitions
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    id_rol = Column(u'id_rol', INTEGER(), primary_key=True, nullable=False)
    nombre_rol = Column(u'nombre_rol', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaTipoItem(DeclarativeBase):
    __tablename__ = 'Tabla_TipoItem'

    #column definitions
    descripcion = Column(u'descripcion', TEXT(length=None, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    id_tipo = Column(u'id_tipo', INTEGER(), primary_key=True, nullable=False)
    nombre_tipo = Column(u'nombre_tipo', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TablaUsuario(DeclarativeBase):
    __tablename__ = 'Tabla_Usuario'

    #column definitions
    Password = Column(u'Password', VARCHAR(length=80, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    alias = Column(u'alias', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    apellido = Column(u'apellido', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    email_address = Column(u'email_address', VARCHAR(length=80, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    id_usuario = Column(u'id_usuario', INTEGER(), primary_key=True, nullable=False)
    nacionalidad = Column(u'nacionalidad', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    nombre = Column(u'nombre', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    nrodoc = Column(u'nrodoc', INTEGER())
    tipodocumento = Column(u'tipodocumento', VARCHAR(length=30, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))

    #relation definitions


class TgGroup(DeclarativeBase):
    __tablename__ = 'tg_group'

    #column definitions
    created = Column(u'created', TIMESTAMP(timezone=False))
    display_name = Column(u'display_name', VARCHAR(length=255, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    group_id = Column(u'group_id', INTEGER(), primary_key=True, nullable=False)
    group_name = Column(u'group_name', VARCHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TgPermission(DeclarativeBase):
    __tablename__ = 'tg_permission'

    #column definitions
    description = Column(u'description', VARCHAR(length=255, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    permission_id = Column(u'permission_id', INTEGER(), primary_key=True, nullable=False)
    permission_name = Column(u'permission_name', VARCHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions


class TgUser(DeclarativeBase):
    __tablename__ = 'tg_user'

    #column definitions
    created = Column(u'created', TIMESTAMP(timezone=False))
    display_name = Column(u'display_name', VARCHAR(length=255, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    email_address = Column(u'email_address', VARCHAR(length=255, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)
    password = Column(u'password', VARCHAR(length=80, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False))
    user_id = Column(u'user_id', INTEGER(), primary_key=True, nullable=False)
    user_name = Column(u'user_name', VARCHAR(length=16, convert_unicode=False, assert_unicode=None, unicode_error=None, _warn_on_bytestring=False), nullable=False)

    #relation definitions



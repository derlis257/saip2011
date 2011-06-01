# -*- coding: utf-8 -*-
"""
Equipo de Desarrollo* related model.


"""
import os
from datetime import datetime
import sys

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym

from saip2011.model import DeclarativeBase, metadata, DBSession
from saip2011.model.proyecto import Proyecto , tabla_proyecto_equipo

__all__ = ['EquipoDesarrollo']


#{ Association tables
tabla_equipo_rol = Table('TB_equipo_rol', metadata,
	Column('id_equipo', Integer, ForeignKey('Tabla_EquipoDesarrollo.id_equipo', onupdate="CASCADE", ondelete="CASCADE")),
	Column('id_rol', Integer, ForeignKey('Tabla_Rol.id_rol', onupdate="CASCADE", ondelete="CASCADE"))
)

tabla_equipo_usuario = Table('TB_equipo_usuario', metadata,
	Column('id_equipo', Integer, ForeignKey('Tabla_EquipoDesarrollo.id_equipo', onupdate="CASCADE", ondelete="CASCADE")),
	Column('id_usuario', Integer, ForeignKey('Tabla_Usuario.id_usuario', onupdate="CASCADE", ondelete="CASCADE"))
)


class EquipoDesarrollo(DeclarativeBase):
      
        """
	Definicion de Equipo de Desarrollo.

	"""

	__tablename__ = 'Tabla_EquipoDesarrollo'

	#{ Columns

	id_equipo = Column(Integer, autoincrement=True, primary_key=True)

	#{ Relations   /// se indica quien me va a usar

	equipo = relation(Proyecto, secondary=tabla_proyecto_equipo, backref='Equipo_de_Desarrollo')
    
    
	#{ Special methods

	def __repr__(self):
		return '<Equipo : id=%s>' % self.id_equipo
    
	def __unicode__(self):
      	  return self.id_equipo
    
   	 #}


#
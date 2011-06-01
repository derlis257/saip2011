# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by :mod:`repoze.who` and :mod:`repoze.what` are
defined.

It's perfectly fine to re-use this definition in the Saip application,
though.

"""
import os
from datetime import datetime
import sys

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime , Text , Enum
from sqlalchemy.orm import relation, synonym

from saip2011.model import DeclarativeBase, metadata, DBSession

__all__ = ['Item']

tabla_item_adjunto = Table('TB_item_adjunto', metadata,
	Column('id_item', Integer, ForeignKey('Tabla_Item.id_item', onupdate="CASCADE", ondelete="CASCADE")),
	Column('id_adjunto', Integer, ForeignKey('Tabla_Adjunto.id_adjunto', onupdate="CASCADE", ondelete="CASCADE"))
)


class Item(DeclarativeBase):
	"""
	Definicion Item
	"""

	__tablename__ = 'Tabla_Item'

	#{ Columns
	
	id_item = Column(Integer, autoincrement=True, primary_key=True)

	tipo_id = Column('nombretipo', Unicode(30), ForeignKey('Tabla_TipoItem.nombre_tipo'))

	tipoitem = relation('TipoItem', backref='itemm')

	fase = Column(Unicode(30) ,  nullable=False)

	proyecto = Column(Unicode(30), nullable=False)

	adjunto = Column(Integer)

	complejidad = Column(Integer, nullable=False)

	estado = Column(Unicode(30), nullable=False)

	campos = Column(Text, nullable=False)

	lista_item = Column(Text)

	creado_por = Column(Unicode(30))

	fecha_creacion = Column(DateTime, default=datetime.now)
	
	#{ Special methods
	
			
	def __repr__(self):
		return '<Item: Id Item=%s>' % self.id_item

	def __unicode__(self):
		return self.id_item

	#}



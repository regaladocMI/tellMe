from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Numeric,
    ForeignKey, UniqueConstraint, Text
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    nombre_visible = Column(String(100), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)

    proveedores_auth = relationship("UsuarioProveedorAuth", back_populates="usuario")


class UsuarioProveedorAuth(Base):
    __tablename__ = "usuario_proveedor_auth"

    id_usuario_proveedor_auth = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    proveedor = Column(String(30), nullable=False)
    id_externo_proveedor = Column(String(255), nullable=False)
    fecha_vinculacion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="proveedores_auth")

    __table_args__ = (
        UniqueConstraint("proveedor", "id_externo_proveedor", name="uq_proveedor_idexterno"),
    )


class NivelIngles(Base):
    __tablename__ = "nivel_ingles"

    id_nivel_ingles = Column(Integer, primary_key=True)
    codigo = Column(String(2), unique=True, nullable=False)
    descripcion = Column(String(50), nullable=False)


class TipoEmisor(Base):
    __tablename__ = "tipo_emisor"

    id_tipo_emisor = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True, nullable=False)


class TipoError(Base):
    __tablename__ = "tipo_error"

    id_tipo_error = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)


class Tema(Base):
    __tablename__ = "tema"

    id_tema = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_nivel_ingles = Column(Integer, ForeignKey("nivel_ingles.id_nivel_ingles"), nullable=False)
    nombre = Column(String(150), nullable=False)
    prompt_base = Column(Text, nullable=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("id_usuario", "nombre", name="uq_tema_usuario_nombre"),
    )


class Sesion(Base):
    __tablename__ = "sesion"

    id_sesion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_tema = Column(Integer, ForeignKey("tema.id_tema"), nullable=False)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
    puntaje_promedio = Column(Numeric(4, 2), nullable=True)


class Mensaje(Base):
    __tablename__ = "mensaje"

    id_mensaje = Column(Integer, primary_key=True)
    id_sesion = Column(Integer, ForeignKey("sesion.id_sesion"), nullable=False)
    id_tipo_emisor = Column(Integer, ForeignKey("tipo_emisor.id_tipo_emisor"), nullable=False)
    texto = Column(Text, nullable=False)
    orden = Column(Integer, nullable=False)
    puntaje = Column(Integer, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)


class Correccion(Base):
    __tablename__ = "correccion"

    id_correccion = Column(Integer, primary_key=True)
    id_mensaje = Column(Integer, ForeignKey("mensaje.id_mensaje"), nullable=False)
    id_tipo_error = Column(Integer, ForeignKey("tipo_error.id_tipo_error"), nullable=False)
    texto_original = Column(Text, nullable=False)
    texto_corregido = Column(Text, nullable=False)
    explicacion = Column(Text, nullable=True)


class Vocabulario(Base):
    __tablename__ = "vocabulario"

    id_vocabulario = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    palabra_o_frase = Column(String(200), nullable=False)
    significado = Column(Text, nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("id_usuario", "palabra_o_frase", name="uq_vocabulario_usuario_palabra"),
    )


class VocabularioOcurrencia(Base):
    __tablename__ = "vocabulario_ocurrencia"

    id_vocabulario_ocurrencia = Column(Integer, primary_key=True)
    id_vocabulario = Column(Integer, ForeignKey("vocabulario.id_vocabulario"), nullable=False)
    id_mensaje = Column(Integer, ForeignKey("mensaje.id_mensaje"), nullable=False)
    fecha_ocurrencia = Column(DateTime, default=datetime.utcnow)


class ConfiguracionUsuario(Base):
    __tablename__ = "configuracion_usuario"

    id_configuracion_usuario = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), unique=True, nullable=False)
    velocidad_habla = Column(Numeric(3, 2), default=1.00)
    paciencia_segundos = Column(Numeric(4, 2), default=2.00)
    ocultar_transcripcion = Column(Boolean, default=False)
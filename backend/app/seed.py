from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models import NivelIngles, TipoEmisor, TipoError

engine = create_engine("sqlite:///./tellme.db")

with Session(engine) as session:
    if session.query(NivelIngles).count() == 0:
        niveles = [
            NivelIngles(codigo="A1", descripcion="Principiante"),
            NivelIngles(codigo="A2", descripcion="Basico"),
            NivelIngles(codigo="B1", descripcion="Intermedio"),
            NivelIngles(codigo="B2", descripcion="Intermedio alto"),
            NivelIngles(codigo="C1", descripcion="Avanzado"),
            NivelIngles(codigo="C2", descripcion="Dominio (nativo o casi nativo)"),
        ]
        session.add_all(niveles)

    if session.query(TipoEmisor).count() == 0:
        emisores = [
            TipoEmisor(nombre="Usuario"),
            TipoEmisor(nombre="Tutor"),
        ]
        session.add_all(emisores)

    if session.query(TipoError).count() == 0:
        errores = [
            TipoError(nombre="Gramatica"),
            TipoError(nombre="Vocabulario"),
            TipoError(nombre="Pronunciacion"),
            TipoError(nombre="Uso y contexto"),
        ]
        session.add_all(errores)

    session.commit()
    print("Datos semilla insertados correctamente.")
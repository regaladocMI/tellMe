# tellMe

Tutor de ingles conversacional por voz. Practica hablado con correccion en tiempo real.

## Arquitectura

- `backend/` — API en Python (FastAPI) que orquesta Speech-to-Text, el LLM tutor, y
  Text-to-Speech.
- `app/` — Cliente movil en Flutter (Android primero).
- `database/` — Diseno del esquema de base de datos.

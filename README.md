# Prácticas de Sistemas Distribuidos - ESCOM

**Descripción:**
Repositorio oficial que contiene el código fuente y la documentación de las prácticas desarrolladas para la unidad de aprendizaje de Sistemas Distribuidos en la Escuela Superior de Cómputo (ESCOM).

---

## Práctica 7: Progressive Web App (PWA) & API REST

### Arquitectura del Sistema
El proyecto está dividido en dos capas principales totalmente desacopladas para garantizar la interoperabilidad:

1. **Backend (API REST):** Desarrollado en Python utilizando **FastAPI**, sirviendo datos estructurados en formato JSON y validando peticiones mediante **Pydantic**.
2. **Frontend (PWA):** Interfaz web construida con HTML/JS moderno. Implementa un **Service Worker** y un `manifest.json` para ser instalable en dispositivos de escritorio y móviles, permitiendo interactividad y resiliencia de red.

### Tecnologías Utilizadas
* **Lenguaje Core:** Python 3.11
* **Framework Backend:** FastAPI
* **Servidor Asíncrono:** Uvicorn
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **PWA:** Service Workers, Web App Manifest
* **Gestión de Entornos:** `venv` (Entornos Virtuales de Python)

### Ejecución Rápida
Para probar esta práctica en un entorno local, sigue estos pasos:
**Backend**
1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Proyecto_Distribuidos
2. **Activa el entorno virtual:**
   En Windows:
  .\entorno\Scripts\activate
3. **Instalar Dependencias**
  python -m pip install fastapi uvicorn pydantic
4. **Levantar la API (Backend)**
  uvicorn backend_api:app --reload

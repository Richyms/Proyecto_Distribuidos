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
Para probar esta práctica en un entorno local:
1. Activar el entorno virtual (`entorno`).
2. Instalar librerias: python -m pip install fastapi uvicorn pydantic
3. Levantar la API con: `uvicorn backend_api:app --reload`
4. Desplegar el cliente frontend utilizando un servidor local (ej. *Live Server* en el puerto 5500).

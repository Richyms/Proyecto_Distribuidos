from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Inicialización de la aplicación
app = FastAPI(title="API Rest - Tienda Geek PWA")

# CONFIGURACIÓN DE CORS: Vital para que la PWA pueda comunicarse con el servidor
# permitiendo peticiones desde el origen del frontend (ej. Live Server).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos para la validación de peticiones
class ItemPeticion(BaseModel):
    categoria: str
    precio: float

# Catálogo centralizado de la tienda
CATALOGO = {
    "Lego": {"ahorro": 15.0, "envio": 150.0},
    "TCG Pokemon": {"ahorro": 30.0, "envio": 50.0},
    "Albumes Kpop": {"ahorro": 25.0, "envio": 100.0},
    "Gunpla (Modelos Armables)": {"ahorro": 20.0, "envio": 130.0},
    "Consolas Retro": {"ahorro": 20.0, "envio": 250.0}
}

@app.get("/")
def home():
    return {"status": "online", "message": "Servidor REST de la Tienda Geek activo"}

@app.post("/calcular")
async def calcular(peticion: ItemPeticion, operacion: str = Query(..., enum=["ahorro", "envio"])):
    """
    Endpoint principal que recibe un JSON y devuelve el cálculo procesado.
    """
    datos = CATALOGO.get(peticion.categoria)
    
    if not datos:
        raise HTTPException(status_code=404, detail="Categoría no registrada en el catálogo")

    if operacion == "ahorro":
        porcentaje = datos["ahorro"]
        resultado = peticion.precio * (porcentaje / 100)
        detalle = f"Descuento del {porcentaje}% aplicado exitosamente."
    else:
        resultado = datos["envio"]
        detalle = f"Costo de envío calculado por fragilidad y volumen."

    return {
        "categoria": peticion.categoria,
        "operacion": operacion,
        "resultado": round(resultado, 2),
        "detalle": detalle,
        "moneda": "MXN"
    }

# Instrucción de ejecución:
# uvicorn backend_api:app --reload
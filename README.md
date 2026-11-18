# RestauControl

Proyecto académico de gestión de restaurantes con FastAPI, Pydantic, SQLAlchemy y pyodbc en el backend, y React, Vite y JavaScript en el frontend. Usa Microsoft SQL Server y un repositorio público en GitHub. El flujo de trabajo local usa Visual Studio Code y GitHub Desktop en Windows.

El alcance incluye productos, categorías, pedidos, mesas, reservaciones, pagos, inventario, ingredientes, proveedores, compras y usuarios. Los roles previstos son Administrador, Gerente, Mesero, Cocinero, Cajero y Cliente.

Esta etapa incluye una API con una ruta de salud y una pantalla de inicio. La integración de las 21 tablas de RestauControlDB está pendiente de revisar los scripts originales.

## Instalación en Windows

Instala Python 3.11 o posterior y Node.js 22.12 o posterior dentro de la rama 22, o Node.js 24 LTS. Abre el repositorio en VS Code y usa dos terminales PowerShell.

### Backend

Desde la raíz del repositorio:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

La documentación interactiva está en `http://127.0.0.1:8000/docs`. Comprueba la ruta de salud con `Invoke-RestMethod http://127.0.0.1:8000/api/v1/health`. La respuesta HTTP esperada es `{"status":"ok"}`.

### Frontend

Desde la raíz del repositorio, en la segunda terminal:

```powershell
cd frontend
npm.cmd install
npm.cmd run dev
```

Abre `http://127.0.0.1:5173` o la dirección que indique Vite. Para compilar, ejecuta `npm.cmd run build`.

### SQL Server

Esta etapa funciona sin servidor de base de datos ni credenciales. Para la futura integración, instala Microsoft ODBC Driver 18 para SQL Server y copia `backend/.env.example` a `backend/.env`. Completa el archivo local con los valores de una cuenta autorizada. Mantén las credenciales fuera de Git.

Consulta [la arquitectura](docs/arquitectura.md) y [el estado de los scripts](database/README.md).

# Arquitectura inicial

FastAPI registra la API versionada en `app/api/v1`. La configuración se carga en `app/core` y la fábrica de sesiones SQLAlchemy está en `app/db`. La ruta de salud comprueba la disponibilidad de la API sin abrir una conexión a SQL Server.

Los módulos se incorporarán en `app/modules` según los flujos de autenticación, usuarios, catálogo, mesas, reservaciones, pedidos, pagos, inventario y compras. Cada módulo incorporará rutas, modelos Pydantic, servicios y repositorios según sus necesidades. Los servicios coordinarán las operaciones que compartan una transacción.

React organiza las pantallas por funcionalidad en `src/features`. `src/app` compone la aplicación y alojará la navegación general.

La integración con las 21 tablas existentes requiere revisar los scripts originales. La autorización se implementará en FastAPI después de definir los permisos por operación para Administrador, Gerente, Mesero, Cocinero, Cajero y Cliente.

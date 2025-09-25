# JWT Token API

Esta API en Flask genera un JWT firmado con una clave privada de Google Service Account y obtiene un access token para autenticarse con BigQuery. Está diseñada para desplegarse fácilmente en [Render](https://render.com) usando `render.yaml`.

---

## 🚀 Despliegue en Render

### 1. Subí tu proyecto a GitHub

Asegurate de tener estos archivos en tu repositorio:

- `app.py`
- `requirements.txt`
- `render.yaml`
- `.env.example` (sin secretos)

---

### 2. Crear el servicio en Render

1. Iniciá sesión en [Render](https://dashboard.render.com).
2. Hacé clic en **New Web Service**.
3. Seleccioná tu repositorio.
4. Render detectará automáticamente el archivo `render.yaml`.

---

### 3. Configurar secretos (variables de entorno)

Render usará las claves definidas en `render.yaml`, pero necesitás ingresar los **valores reales** manualmente:

#### Variables requeridas:

| Clave           | Descripción                                      |
|-----------------|--------------------------------------------------|
| `CLIENT_EMAIL`  | Email del Service Account                        |
| `PRIVATE_KEY`   | Clave privada (usar `\n` para saltos de línea)  |
| `TOKEN_URI`     | URI del token (por defecto: `https://oauth2.googleapis.com/token`) |

#### Cómo configurarlas:

1. Ir a tu servicio en Render.
2. Abrí la pestaña **Environment**.
3. Agregá cada variable con su valor correspondiente.

---

## 🧪 Endpoints disponibles

| Endpoint     | Método | Descripción                                 |
|--------------|--------|---------------------------------------------|
| `/get-token` | GET    | Genera el JWT y devuelve el access token    |
| `/`          | GET    | Mensaje de bienvenida                       |
| `/health`    | GET    | Verifica que la API esté funcionando        |

---

## 📦 Archivos importantes

- `app.py`: lógica principal de la API.
- `requirements.txt`: dependencias.
- `render.yaml`: configuración para Render.
- `.env.example`: plantilla para variables de entorno (sin secretos).

---

## ✅ Recomendaciones

- Nunca subas tu `.env` real al repositorio.
- Usá `sync: false` en `render.yaml` para evitar exponer secretos.
- Podés usar `python-dotenv` para pruebas locales.

---

## 🛠 Autor

Leandro — API JWT Token Generator para BigQuery

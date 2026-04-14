### FakeBuster
FakeBuster es una aplicación web desarrollada con Django que ayuda a detectar posible desinformación en noticias. Permite analizar una noticia desde su URL o ingresando manualmente título, autor y fecha, y utiliza Inteligencia Artificial para evaluar su veracidad.

FakeBuster ofrece dos formas de entrada:

- Análisis automático por URL: se extrae el título, autor y fecha de publicación de la noticia usando la librería newspaper.
Luego se valida esa información con un modelo de IA.

- Análisis manual: el usuario ingresa directamente el título, autor y fecha.
Se envía esa información al mismo flujo de evaluación.

---

## Cómo funciona
views.py
- Define la vista mostrar_valor.
- Detecta si se envió el formulario con URL o el formulario manual.
- Si se envía la URL, llama a principalURL.obtener_datos_articulo(url).
- Si se envían datos manuales, usa esos valores directamente.

principalURL.py
- Usa newspaper.Article para descargar y analizar la noticia.
- Extrae autor, título y fecha.
- Usa caché simple para evitar consultas duplicadas por URL.

principal.py
- Genera los mensajes de consulta para verificar el título, obtener información del autor y validar la fecha del evento.
- Envía estas consultas a palm.py.

palm.py
- Se conecta a la API de Google Generative AI (gemini-1.5-flash).
- Traduce la solicitud a inglés con mtranslate, obtiene la respuesta del modelo y la vuelve a traducir al español.

traductor.py
- Traduce textos a inglés y español.
- Usa caché para evitar traducciones repetidas.

---

## Estructura principal del proyecto
´´´
FakeBuster/
├── __init__.py                # Inicializa la app Django
├── admin.py                   # Registro de modelos en el admin (vacío)
├── apps.py                    # Configuración de la app FakeBuster
├── models.py                  # Modelos Django (sin definiciones activas)
├── palm.py                    # Conexión con Google Generative AI y traducción de prompts
├── principal.py               # Genera consultas para título, autor y fecha
├── principalURL.py            # Analiza la URL de la noticia con newspaper
├── tests.py                   # Pruebas de la app (vacío o sin implementar)
├── traductor.py               # Traduce textos entre inglés y español
├── urls.py                    # Rutas internas de la app
├── views.py                   # Lógica de la vista principal y manejo de formularios
├── migrations/                # Migraciones de la base de datos
│   └── __init__.py
├── static/                    # Archivos estáticos (CSS, imágenes)
│   ├── styles.css
│   ├── stylesResultados.css
│   └── ...                    # Posibles otros recursos estáticos como fakebuster.png
└── templates/                 # Plantillas HTML de la app
    ├── index.html
    └── respuesta.html

FakeBusterWeb/
├── __init__.py                # Inicializa el paquete del proyecto
├── asgi.py                    # Configuración ASGI
├── settings.py                # Configuración general de Django
├── urls.py                    # Rutas globales del proyecto
└── wsgi.py                    # Configuración WSGI

manage.py                       # Comando estándar de Django
README.md                       # Documentación del proyecto
db.sqlite3                      # Base de datos SQLite usada por defecto
´´´

---

## Dependencias principales
Necesitas instalar:

- Django
- newspaper3k
- google-generativeai
- mtranslate

---

## Instalación rápida
1. Crear y activar un entorno virtual.
2. Instalar dependencias.
3. Ejecutar migraciones (aunque el proyecto no define modelos activos).
4. Iniciar el servidor:
´´´bash
python manage.py migrate
python manage.py runserver
´´´
5. Abrir en el navegador:
http://127.0.0.1:8000/fakebuster/

---

## Notas sobre db.sqlite3
- El proyecto usa la configuración SQLite por defecto en settings.py.
- Actualmente no hay modelos registrados en models.py, por lo que la base de datos no se utiliza activamente en la lógica principal de análisis.

---

## Consideraciones
- En palm.py hay una línea que configura la API key: genai.configure(api_key='api_key')
- Debe reemplazarse con la clave real de Google Cloud Console / Google AI Studio.

---

## Colaboradores del proyecto
<li>@danielisaisal</li>
<li>@memotas98</li>
<li>@OzielLM</li>
<li>@Rogelio-CC</li>
<li>@GerardoYael13</li>

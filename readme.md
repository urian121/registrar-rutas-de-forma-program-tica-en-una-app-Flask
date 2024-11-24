
# Mi Proyecto Flask con `add_url_rule`

Este es un ejemplo de cómo usar el método **`add_url_rule`** en Flask para registrar rutas de manera programática. Se incluye una estructura modular con funciones de vista y rutas separadas, además de un archivo `index.html` para la página principal.

## Características

- Uso de **`add_url_rule`** para registrar rutas de manera explícita.
- Separación de responsabilidades con módulos para vistas y rutas.
- Rutas dinámicas con parámetros.
- Plantilla HTML para la página principal.

## Estructura del Proyecto

```
mi_proyecto/
│
├── app/
│   ├── __init__.py         # Inicializa la aplicación Flask
│   ├── routes.py           # Define y registra las rutas
│   └── views.py            # Define las funciones de vista
│
├── templates/
│   └── index.html          # Página principal HTML
└── run.py                  # Archivo para correr la aplicación
```

## Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/urian121/registrar-rutas-de-forma-program-tica-en-una-app-Flask
   cd mi-proyecto-flask
   ```

2. Crea un entorno virtual y activa:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. Instala Flask:
   ```bash
   pip install flask
   ```

4. Ejecuta la aplicación:
   ```bash
   python run.py
   ```

5. Abre tu navegador y accede a: [http://localhost:5000](http://localhost:5000)

## Rutas Disponibles

- `/` : Página principal.
- `/about` : Acerca de la aplicación.
- `/contact` : Página de contacto.
- `/services` : Servicios ofrecidos.
- `/greet/<username>` : Saludo dinámico. Ejemplo: `/greet/Urian`.

## Ejemplo Visual de `index.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Proyecto Flask</title>
</head>
<body>
    <h1>Bienvenido a la Aplicación Flask</h1>
    <h2>Enlaces a las páginas:</h2>
    <ul>
        <li><a href="/">Página Principal</a></li>
        <li><a href="/about">Acerca de</a></li>
        <li><a href="/contact">Contáctanos</a></li>
        <li><a href="/services">Servicios</a></li>
        <li><a href="/greet/Urian">Saludo a Urian</a></li>
    </ul>
</body>
</html>
```

## Beneficios de Usar `add_url_rule`

- **Separación de responsabilidades**: Organiza las rutas y vistas en módulos separados.
- **Flexibilidad**: Permite agregar rutas de manera condicional o dinámica.
- **Escalabilidad**: Ideal para aplicaciones con muchas rutas y vistas.
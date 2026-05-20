# Generador del sitio web para ACEC Chile
# Ejecuta este script con: python generador_acec.py

def crear_archivo():
    contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ACEC Chile | Inclusión Alimentaria</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'celiac-green': '#2D6A4F',
                        'celiac-light': '#D8F3DC',
                        'celiac-sand': '#F8F9FA'
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-celiac-sand text-gray-800 font-sans">
    <header class="bg-celiac-green text-white py-12 px-6 text-center">
        <h1 class="text-4xl font-bold mb-2">ACEC Chile</h1>
        <p class="text-emerald-100 italic">Agrupación de Celíacos - Por un Chile Inclusivo</p>
    </header>

    <main class="max-w-4xl mx-auto p-6 md:p-10">
        <section class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-celiac-green mb-8">
            <h2 class="text-2xl font-bold text-celiac-green mb-4">Gestión Legislativa y Lobby</h2>
            <p class="leading-relaxed text-gray-700">
                Nuestra misión central es la visibilización y el acceso seguro a los alimentos. 
                Participamos activamente en audiencias legislativas en el Congreso, 
                promoviendo la correcta reglamentación de la Ley Celíaca y fiscalizando 
                la implementación efectiva de la Ley de Lobby para garantizar transparencia.
            </p>
        </section>

        <section class="bg-celiac-light p-8 rounded-xl">
            <h3 class="font-bold text-xl text-celiac-green mb-4">Contacto Ciudadano</h3>
            <p class="mb-6">Tu voz es fundamental. Si tienes dudas, requieres asesoría sobre inclusión alimentaria o quieres colaborar con la agrupación, escríbenos:</p>
            <a href="mailto:contacto@acec.cl" class="bg-celiac-green text-white px-8 py-3 rounded-full hover:bg-green-900 transition font-bold shadow-md">
                Enviar Correo a la Agrupación
            </a>
        </section>
    </main>
</body>
</html>"""
    
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(contenido_html)
        print("Archivo 'index.html' generado con éxito con la paleta de colores solicitada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    crear_archivo()
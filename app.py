from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola():
    return """
    <html>
    <head>
    <style>
        body { text-align:center; font-family: 'Comic Sans MS', Arial; background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: #ffffff; }
        h1 { color: #ff6f61; font-size: 60px; text-shadow: 2px 2px #000000; }
        p { font-size: 24px; color: #f4d03f; }
        .glow { text-shadow: 0 0 10px #ff6f61, 0 0 20px #ff6f61, 0 0 30px #ff6f61; }
    </style>
    </head>
    <body>
        <h1 class="glow">¡Hola Mundo 🚀! - Práctica de despliegue web</h1>
        <p>Que tal 😎✨</p>
    </body>
    </html>
    """

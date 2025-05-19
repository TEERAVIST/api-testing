from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello TOMO</title>
        <style>
            body {
                background: #0f172a;
                color: #f8fafc;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding-top: 20vh;
            }
            h1 {
                font-size: 4em;
                animation: glow 1.5s ease-in-out infinite alternate;
            }
            @keyframes glow {
                from {
                    text-shadow: 0 0 10px #38bdf8, 0 0 20px #0ea5e9;
                }
                to {
                    text-shadow: 0 0 20px #7dd3fc, 0 0 30px #38bdf8;
                }
            }
        </style>
    </head>
    <body>
        <h1>Hello TOMO 💫</h1>
        <p>Welcome to your custom AI API ✨</p>
    </body>
    </html>
    """


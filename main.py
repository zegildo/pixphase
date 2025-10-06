from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import qrcode

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

image = qrcode.make("https://www.youtube.com/watch?v=-11H6OS3RJA")
print(type(image))
image.save("static/qrcode.png")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    # Frase atual e pagamentos simulados
    phrase = "Se já rouba esse tanto com 9 dedos imagine com 10!!!"
    payments = [
        {"name": "Frase 1", "amount": "R$ 3,00"},
        {"name": "Frase 2", "amount": "R$ 3,50"},
        {"name": "Frase 3", "amount": "R$ 14,80"},
    ]
    qr_value = "R$ 15,00"  # valor sugerido
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "phrase": phrase,
            "qr_value": qr_value,
            "payments": payments
        }
    )

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import warnings

warnings.filterwarnings("ignore")

app = FastAPI()

regressor = joblib.load("app/regressor.joblib")

templates = Jinja2Templates(directory="app/static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submitform", response_class=HTMLResponse)
async def predict(request: Request, HoursStudied: int = Form(...), PreviousScores: int = Form(...), ExtracurricularActivities: int = Form(...), SleepHours: int = Form(...), SampleQuestionPapersPracticed: int = Form(...)):
    prediction = regressor.predict([[HoursStudied, PreviousScores, ExtracurricularActivities, SleepHours, SampleQuestionPapersPracticed]])
    return templates.TemplateResponse("index.html", {"request": request, "prediction": int(prediction[0])})

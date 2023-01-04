from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title='Azure Practise API')

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
def root():
	return "Welcome to AI-LifeBot"

@app.post("/predict")
def transcribe(text: str,response: Response):

    data = {"output":f"Azure API is getting hit {text} "}

    return JSONResponse(data)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
async def get_data():
    mock_data = [
        {"name": "Carlos Silva", "age_in_months": 348, "city": "São Paulo"},
        {"name": "Ana Souza", "age_in_months": 420, "city": "Rio de Janeiro"},
        {"name": "Pedro Oliveira", "age_in_months": 504, "city": "Belo Horizonte"}
    ]
    return {"users": mock_data}

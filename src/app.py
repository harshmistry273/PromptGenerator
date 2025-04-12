from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from src.endpoints.v1.prompt import router as prompt_router

app = FastAPI()

@app.get('/health')
def get_health_status():
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={
                            "message": "Working!",
                            "data": [],
                            "status": True,
                            "error": ""
                        })

app.include_router(prompt_router)
from fastapi import FastAPI
from fastapi import HTTPException
from mysql.connector import Error
from pydantic import BaseModel
from typing import Optional
import math

app = FastAPI()

@app.get("/quadrados/")
def quadrado_perfeito(max: Optional[int] = 5):
    if(max is None):
        return{
            "max":max,
            "quadrados": quadrados
        }
    else:
        quadrados = []
        for elementos in range(1,max+1):
            quadrados.append(int(math.pow(elementos,2)))
        return{
            "max":max,
            "quadrados": quadrados
        }

        
        


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
    
@app.get("/tabuada/{num}")
def calcula_tabuada(num:int, start: Optional[int] = 1 , end:Optional[int] = 10):
    if(start is None or end is None):
        return{
            "num":num,
            "start":start,
            "end":end,
            "tabuada": tabuada
        }
    elif(start > end):
        return {
           "erro": "Start não pode ser maior que o end padrão 10"
        }
    else:
        tabuada = []
        for i in range(start, end+1):
            resultado = num * i
            tabuada.append(resultado)
        return {
            "num":num,
            "start":start,
            "end":end,
            "tabuada": tabuada
        }
    
class calculo(BaseModel):
    a: int
    b: int
    c: int
@app.post("/bhaskara/")
def bhaskara(bhaskara: calculo):
    try:
        x =(bhaskara.b**2)-(4*bhaskara.a*bhaskara.c)
        x=(math.sqrt(x))
        x1=(-bhaskara.b+x)/(2*bhaskara.a)
        x2=(-bhaskara.b-x)/(2*bhaskara.a)
        return{
            "equation": f"{bhaskara.a:+}x²{bhaskara.b:+}x{bhaskara.c:+}",
            "x1": x1,
            "x2": x2,
        }
    except:
        return {
            "erro":"Impossível, não há solução real para essa equação"
        }

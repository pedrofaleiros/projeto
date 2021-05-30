from pydantic import BaseModel

class ProfessorCadastro(BaseModel):

    nome:str
    preco:float
    materia:str
    contato:str
    obs:str

class AlgoritmoEscolhido(BaseModel):
    id:str
    algorimo:str
    filtro:str
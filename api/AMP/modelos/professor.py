from pydantic import BaseModel

class ProfessorCadastro(BaseModel):

    nome:str
    preco:float
    materia:str
    contato:str
    obs:str

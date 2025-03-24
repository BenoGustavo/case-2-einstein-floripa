from pydantic import BaseModel
from typing import List


class AlunoEstatistica(BaseModel):
    nome: str
    acertos: int
    media: float


class ResultadoGeral(BaseModel):
    media_geral: float
    alunos: List[AlunoEstatistica]

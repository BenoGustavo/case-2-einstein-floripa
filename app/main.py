from fastapi import FastAPI, UploadFile, File, HTTPException
from .services.data_processor import process_files
from .models import ResultadoGeral

app = FastAPI()

# Armazena os dados processados temporariamente
processed_data = {}


@app.post("/upload-files/")
def upload_files(gabarito: UploadFile = File(...), respostas: UploadFile = File(...)):
    """Recebe e processa os arquivos CSV."""
    try:
        gabarito_csv = gabarito.file.read().decode("utf-8")
        respostas_csv = respostas.file.read().decode("utf-8")

        global processed_data
        processed_data = process_files(gabarito_csv, respostas_csv)

        return {"message": "Arquivos processados com sucesso!", "data": processed_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/results/", response_model=ResultadoGeral)
def get_results():
    """Retorna os resultados processados."""
    if not processed_data:
        raise HTTPException(
            status_code=400,
            detail="Nenhum dado processado ainda. Envie os arquivos primeiro.",
        )
    return ResultadoGeral(**processed_data)

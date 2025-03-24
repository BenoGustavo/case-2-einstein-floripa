from io import StringIO
import pandas as pd


def convert_csv_to_df(csv_data: str):
    return pd.read_csv(StringIO(csv_data))


def calculate_correct_answers(gabarito_df, respostas_df):
    # convert the dataframes to dictionaries
    gabarito = gabarito_df.set_index("Questão")["Gabarito"].to_dict()
    acertos_por_aluno = {}

    for _, row in respostas_df.iterrows():
        aluno = row["aluno_nome"]
        questao = row["num_exercicio"]
        resposta = str(row["resp_aluno"]).strip().upper()

        if aluno not in acertos_por_aluno:
            # initialize the student with 0 correct answers
            acertos_por_aluno[aluno] = 0
        if gabarito.get(questao) == resposta:
            acertos_por_aluno[aluno] += 1
    return acertos_por_aluno

from ..utils import calculate_correct_answers, convert_csv_to_df


def process_files(gabarito_csv: str, respostas_csv: str):
    """Processa os arquivos CSV e calcula as estatísticas."""
    gabarito_df = convert_csv_to_df(gabarito_csv)
    respostas_df = convert_csv_to_df(respostas_csv)

    acertos_por_aluno = calculate_correct_answers(gabarito_df, respostas_df)
    total_questoes = len(gabarito_df)

    # Soma os acertos de todos os alunos
    total_acertos = sum(acertos_por_aluno.values())

    # Pega o número de alunos
    num_alunos = len(acertos_por_aluno)

    # Calcula a média de acertos de todos os alunos
    media_todos_alunos = round((total_acertos / (num_alunos * total_questoes)) * 100, 2)

    estatisticas = {
        "media_geral": media_todos_alunos,
        "alunos": [
            {
                "nome": aluno,
                "acertos": acertos,
                "media": round((acertos / total_questoes) * 100, 2),
            }
            for aluno, acertos in acertos_por_aluno.items()
        ],
    }

    return estatisticas

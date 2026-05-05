from openai import OpenAI


def get_ai_context(title: str, movement: str, api_key: str) -> str:
    """
    Gera um contexto artístico usando a API da OpenAI.
    """
    if not api_key:
        return "Não foi possível gerar o contexto no momento."

    try:
        client = OpenAI(api_key=api_key)

        prompt = (
            f"Você é um curador de arte especializado. "
            f"Evite usar * * para colocar em negrito. "
            f'A obra se chama: "{title}". '
            f"O movimento artístico é: {movement}. "
            f"Em até 4 parágrafos curtos e envolventes, em português do Brasil, explique "
            f"o contexto histórico, características visuais, técnicas e importância cultural."
        )

        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt,
            max_output_tokens=700,
        )

        return response.output_text

    except Exception:
        return "Não foi possível gerar o contexto no momento."
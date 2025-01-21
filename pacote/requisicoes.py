import requests

def pesquisar(resposta1):
    """Faz uma pesquisa na Wikipédia e retorna o texto formatado."""
    resposta1 = resposta1.replace("o que é uma ", "")
    resposta1 = resposta1.replace("o que é um ", "")
    resposta1 = resposta1.replace("o que é o ", "")
    resposta1 = resposta1.replace("o que é a ", "")
    resposta1 = resposta1.replace("o que e uma ", "")
    resposta1 = resposta1.replace("o que e um ", "")
    resposta1 = resposta1.replace("o que e o ", "")
    resposta1 = resposta1.replace("o que e a ", "")
    resposta1 = resposta1.replace("o que e ", "")
    resposta1 = resposta1.replace("o que sao os ", "")
    resposta1 = resposta1.replace("o que sao as ", "")
    resposta1 = resposta1.replace("o que sao ", "")
    resposta1 = resposta1.replace("quem e os ", "")
    resposta1 = resposta1.replace("quem e as ", "")
    resposta1 = resposta1.replace("quem e ", "")
    resposta1 = resposta1.replace("quem é o ", "")
    resposta1 = resposta1.replace("quem é a ", "")
    resposta1 = resposta1.replace("quem é ", "")
    resposta1 = resposta1.replace("quem e o ", "")
    resposta1 = resposta1.replace("quem e a ", "")
    resposta1 = resposta1.replace("quem e ", "")
    resposta1 = resposta1.replace("quem são os ", "")
    resposta1 = resposta1.replace("quem são as ", "")
    resposta1 = resposta1.replace("quem são ", "")
    resposta1 = resposta1.replace("quem foi os ", "")
    resposta1 = resposta1.replace("quem foi as ", "")
    resposta1 = resposta1.replace("quem foi ", "")
    resposta1 = resposta1.replace("quem foram os ", "")
    resposta1 = resposta1.replace("quem foram as ", "")
    resposta1 = resposta1.replace("quem foram ", "")
    resposta1 = resposta1.replace("o que foi o ", "")
    resposta1 = resposta1.replace("o que foi a ", "")
    resposta1 = resposta1.replace("o que foi ", "")
    resposta1 = resposta1.replace(" ", "_")
    resposta1 = resposta1.replace(".", "")
    resposta1 = resposta1.replace("?", "")

    url = f"https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={resposta1}&exintro=true&explaintext=true"
    ir = requests.get(url)

    if ir.status_code == 200:
        data = ir.json()
        pages = data["query"]["pages"]
        page = list(pages.values())[0]

        if "missing" in page or not page.get("extract"):
            return f"não sei"
        else:
            return page["extract"]
    else:
        return "Erro ao acessar a Wikipédia. Tente novamente mais tarde."
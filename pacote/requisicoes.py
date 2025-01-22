import requests
from pacote.replace import hardcode

def pesquisar(resposta1):
    replace(resposta1)
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

import requests
from pacote.replace import hardcode

def pesquisar(respostamod):
    hardcode(respostamod)
    ir = requests.get("https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="+respostamod+"&exintro=true&explaintext=true")

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

import requests
from bs4 import BeautifulSoup
print("carregando. pode demorar um pouco. quando quiser desligar o programa digite \"desligar1\" e de enter")
falas = ["Qual foi a coisa mais legal que aconteceu com você essa semana?", "Se você pudesse viajar para qualquer lugar do mundo agora, para onde iria?", "Você gosta mais de praia ou montanha? Por quê?", "Já assistiu algum filme recentemente que recomendaria?", "Se pudesse escolher qualquer habilidade para aprender instantaneamente, qual seria?", "Você tem algum hobby que começou recentemente?", "Se você tivesse que comer apenas um prato pelo resto da vida, qual seria?", "Qual é a música que você não para de ouvir ultimamente?", "Você é do tipo que gosta de planejar tudo ou prefere deixar as coisas acontecerem?", "Já teve algum sonho engraçado ou estranho que lembra até hoje?", "Qual foi a coisa mais espontânea que você já fez?", "Você prefere um bom livro ou uma maratona de séries?", "Qual seria a sua ideia de um dia perfeito?", "Se você pudesse voltar no tempo, que momento você reviveria?", "Você é mais do time café ou chá? Alguma história engraçada envolvendo isso?", "Já teve vontade de aprender um idioma diferente? Qual seria?", "Qual foi a última coisa que te fez rir muito?", "Se fosse montar uma playlist agora, qual seria o tema?", "Qual foi o lugar mais bonito que você já visitou?", "Se você pudesse ter qualquer animal como pet, real ou fictício, qual seria?", "Tem algum talento oculto ou habilidade que pouca gente sabe que você tem?", "Qual é a sua comida favorita da infância que ainda ama hoje?", "Você é mais do time sair de casa ou curtir um dia tranquilo em casa?", "Qual foi o melhor conselho que já recebeu?", "Você acredita que a tecnologia está ajudando mais ou complicando a vida das pessoas?"]
piadas = ["Por que o livro de matemática estava triste? Porque tinha muitos problemas.", "O que o tomate foi fazer no banco? Tirar extrato.", "O que é um pontinho amarelo na parede? Um fandangos alpinista.", "Por que a vaca foi para o espaço? Para se encontrar com o vácuo.", "O que o pato falou para a pata? Vem Quá!", "Por que o computador foi preso? Porque ele executou um programa.", "Como o elétron atendeu ao telefone? Próton!", "Por que a ovelha foi para a escola? Para virar uma lã-pensante.", "Qual o lugar mais rápido do mundo? O banheiro, porque é lá que as necessidades correm.", "O que é um pontinho verde no alto da escada? Um ervilha alpinista.", "Por que as estrelas não fazem faculdade? Porque já são brilhantes.", "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano.", "Qual é o cúmulo da paciência? Esperar sentado por um exame de pé.", "O que é um pontinho azul no céu? Um smurf voador.", "Por que o músico foi ao banco? Sacar uma nota."]
respostas = ["legal : ","entendi : ","ok : ","real : ","boa","top : ","escolheu bém : "]
sorteio = 1, 2
from random import *
import time
chat = ""
resposta1 = input("olá : ")
while resposta1 != "desligar1":
    if resposta1.find("desligar") >-1:
        break
    elif resposta1.find("o que é ") >-1 or resposta1.find("o que foi ")>-1  or resposta1.find("quem foi ")>-1 or resposta1.find("quem é ")>-1 or resposta1.find("o que são ")>-1 or resposta1.find("o que e ")>-1 or resposta1.find("quem são ")>-1 or resposta1.find("o que foram ")>-1 or resposta1.find("quem e ") >-1:
        resposta1 = resposta1.replace("o que é uma ", "")
        resposta1 = resposta1.replace("o que é um ", "")
        resposta1 = resposta1.replace("o que é o ", "")
        resposta1 = resposta1.replace("o que é a ", "")
        resposta1 = resposta1.replace("o que e uma ", "")
        resposta1 = resposta1.replace("o que e um ", "")
        resposta1 = resposta1.replace("o que e o ", "")
        resposta1 = resposta1.replace("o que e a ", "")
        resposta1 = resposta1.replace("o que e ", "")
        resposta1 = resposta1.replace("o que sao os", "")
        resposta1 = resposta1.replace("o que sao as", "")
        resposta1 = resposta1.replace("o que sao ", "")
        resposta1 = resposta1.replace("quem e os", "")
        resposta1 = resposta1.replace("quem e as", "")
        resposta1 = resposta1.replace("quem e ", "")
        resposta1 = resposta1.replace("o que é ", "")
        resposta1 = resposta1.replace("o que são os", "")
        resposta1 = resposta1.replace("o que são as", "")
        resposta1 = resposta1.replace("o que são ", "")
        resposta1 = resposta1.replace("quem é o ", "")
        resposta1 = resposta1.replace("quem é a ", "")
        resposta1 = resposta1.replace("quem é ", "")
        resposta1 = resposta1.replace("quem são os ", "")
        resposta1 = resposta1.replace("quem são as ", "")
        resposta1 = resposta1.replace("quem são ", "")
        resposta1 = resposta1.replace("quem foi os ", "")
        resposta1 = resposta1.replace("quem foi as ", "")
        resposta1 = resposta1.replace("quem foi ", "")
        resposta1 = resposta1.replace("quem foram os ", "")
        resposta1 = resposta1.replace("quem foram as ", "")
        resposta1 = resposta1.replace("quem foram ", "")
        resposta1 = resposta1.replace("quem foi o ", "")
        resposta1 = resposta1.replace("quem foi a ", "")
        resposta1 = resposta1.replace("o que foi o ", "")
        resposta1 = resposta1.replace("o que foi a ", "")
        resposta1 = resposta1.replace("o que foi ", "")
        resposta1 = resposta1.replace(" ", "_")
        resposta1 = resposta1.replace(".", "")
        ir = requests.get("https://pt.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=" + resposta1 + "&exintro=true&explaintext=true")
        if ir.status_code == 200:
            data = ir.json()

            # Verifica se a página foi encontrada
            pages = data["query"]["pages"]
            page = list(pages.values())[0]

            if "missing" in page or not page.get("extract"):  # Verifica se a página não existe ou não tem 'extract'
                resposta1 = resposta1.replace(" ", "_")
                # Faz a requisição HTTP
                ir = requests.get("https://pt.wikipedia.org/wiki/" + resposta1.title())
                pesquisouja = ir.text
                posinicial = pesquisouja.find("<p><b>", 0)  # Localiza a abertura "<"     
                posfinal = pesquisouja.find(".", posinicial)  # Localiza o fechamento ">"
                pesquisouja = pesquisouja[posinicial:posfinal + 1]  # Inclui o ">"
                if "<b>A Wikipédia não possui um artigo com este nome exato.</b>" in ir.text or ir.text == "":
                    print("Página não encontrada")
                else:
                    html = []
                    start = 0

                    # Coleta os trechos entre "<" e ">" do HTML
                    while "<" in pesquisouja and ">" in pesquisouja:
                        posinicial = pesquisouja.find("<")
                        posfinal = pesquisouja.find(">", posinicial)
                        if posfinal == -1:
                            break  # Garante que não ocorra erro se não houver ">"
                        pesquisouja = pesquisouja[:posinicial] + pesquisouja[posfinal + 1:]
                    print(pesquisouja)
            else:
                # Exibe o primeiro parágrafo (extract)
                texto = page["extract"]
                print(texto)
        else:
            print("Erro ao acessar a página! tente resumir a pesquisa.")


    elif resposta1.find("oi") >-1 or resposta1.find("olá") >-1 or resposta1.find("opa") >-1:
        resposta1 = input("olá : ")
    elif resposta1.find("tudo bem") >-1:
        resposta1 = input("tudo bem e você : ")
    elif resposta1.find("conte") >-1 and resposta1.find("piada") >-1:
        resposta1 = input(choice(piadas))
    else:
        sorte = choice(sorteio)
        if sorte == 1:
            resposta1 = input(choice(piadas))
        else:
            resposta1 = input(choice(falas))
            resposta1 = input(choice(respostas))

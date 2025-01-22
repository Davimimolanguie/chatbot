from pacote.requisicoes import pesquisar
import requests
from bs4 import BeautifulSoup
print("carregando. pode demorar um pouco. quando quiser desligar o programa digite \"desligar1\" e de enter")
falas = ["Qual foi a coisa mais legal que aconteceu com você essa semana : ", "Se você pudesse viajar para qualquer lugar do mundo agora, para onde iria : ", "Você gosta mais de praia ou montanha? Por quê : ", "Já assistiu algum filme recentemente que recomendaria : ", "Se pudesse escolher qualquer habilidade para aprender instantaneamente, qual seria : ", "Você tem algum hobby que começou recentemente : ", "Se você tivesse que comer apenas um prato pelo resto da vida, qual seria : ", "Qual é a música que você não para de ouvir ultimamente : ", "Você é do tipo que gosta de planejar tudo ou prefere deixar as coisas acontecerem : ", "Já teve algum sonho engraçado ou estranho que lembra até hoje : ", "Qual foi a coisa mais espontânea que você já fez : ", "Você prefere um bom livro ou uma maratona de séries : ", "Qual seria a sua ideia de um dia perfeito : ", "Se você pudesse voltar no tempo, que momento você reviveria : ", "Você é mais do time café ou chá? Alguma história engraçada envolvendo isso : ", "Já teve vontade de aprender um idioma diferente? Qual seria : ", "Qual foi a última coisa que te fez rir muito : ", "Se fosse montar uma playlist agora, qual seria o tema : ", "Qual foi o lugar mais bonito que você já visitou : ", "Se você pudesse ter qualquer animal como pet, real ou fictício, qual seria : ", "Tem algum talento oculto ou habilidade que pouca gente sabe que você tem : ", "Qual é a sua comida favorita da infância que ainda ama hoje : ", "Você é mais do time sair de casa ou curtir um dia tranquilo em casa : ", "Qual foi o melhor conselho que já recebeu : ", "Você acredita que a tecnologia está ajudando mais ou complicando a vida das pessoas : "]
piadas = ["Por que o livro de matemática estava triste? Porque tinha muitos problemas : ", "O que o tomate foi fazer no banco? Tirar extrato : ", "O que é um pontinho amarelo na parede? Um fandangos alpinista : ", "Por que a vaca foi para o espaço? Para se encontrar com o vácuo : ", "O que o pato falou para a pata? Vem Quá : ", "Por que o computador foi preso? Porque ele executou um programa : ", "Como o elétron atendeu ao telefone? Próton : ", "Por que a ovelha foi para a escola? Para virar uma lã-pensante : ", "Qual o lugar mais rápido do mundo? O banheiro, porque é lá que as necessidades correm : ", "O que é um pontinho verde no alto da escada? Um ervilha alpinista : ", "Por que as estrelas não fazem faculdade? Porque já são brilhantes : ", "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano : ", "Qual é o cúmulo da paciência? Esperar sentado por um exame de pé : ", "O que é um pontinho azul no céu? Um smurf voador : ", "Por que o músico foi ao banco? Sacar uma nota : "]
respostas = ["legal : ","entendi : ","ok : ","real : ","boa","top : ","escolheu bém : "]
sorteio = 1, 2
from random import *
import time
chat = ""
resposta1 = input("olá : ")
while resposta1 != "desligar1":
    print()
    if resposta1.find("desligar") >-1:
        break
    elif any(keyword in resposta1.lower() for keyword in ["o que é ", "quem é ", "o que foi ", "quem foi ", "o que e", "quem e ", "quem foram ", "quem são ", "quem sao ", "quem foi "]):
        resultado = pesquisar(resposta1)
        resposta1 = input(f"Chatbot: {resultado}" + " : ")

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

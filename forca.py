import random

def escolher_palavra():
palavras = [
"python", "desenvolvedor", "programa", "computador", "algoritmo",
"teclado", "monitor", "internet", "software", "hardware"
]
return random.choice(palavras).lower()

def jogar():
palavra = escolher_palavra()
letras_descobertas = set()
tentativas = 6

print("=== Jogo da Forca ===")
print(f"A palavra tem {len(palavra)} letras.")

while tentativas > 0:
    exibicao = [letra if letra in letras_descobertas else "_" for letra in palavra]
    print("Palavra: " + " ".join(exibicao))
    print(f"Tentativas restantes: {tentativas}")

    palpite = input("Digite uma letra: ").lower()
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    if palpite in letras_descobertas:
        print("Você já tentou essa letra.")
        continue

    if palpite in palavra:
        letras_descobertas.add(palpite)
        print(f"Boa! A letra '{palpite}' está na palavra.")
    else:
        tentativas -= 1
        print(f"Ops! A letra '{palpite}' não está na palavra.")

    if all(letra in letras_descobertas for letra in palavra):
        print(f"Parabéns! Você adivinhou a palavra: {palavra}")
        break
    print()

else:
    print(f"Fim de jogo! A palavra era: {palavra}")
if name == "main":
jogar()

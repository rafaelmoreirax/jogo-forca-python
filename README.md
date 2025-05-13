# 🧩 Jogo de Forca Simples em Python

Um jogo clássico de forca implementado em Python para terminal, com interface simples e funcional. O usuário tenta adivinhar a palavra secreta letra por letra antes de esgotar as tentativas.

---

## 🚀 Como usar
```
1. Clone o repositório:
git clone https://github.com/rafaelmoreirax/jogo-forca-python.git
cd jogo-forca-python
```

2. Execute o script:
python3 forca.py


3. Siga as instruções no terminal para jogar.

---

## 🛠️ Tecnologias

- Python 3 (biblioteca padrão)

---

## 📋 Funcionalidades

- Escolha aleatória de palavra secreta de uma lista interna.
- Exibe progresso da palavra com letras descobertas e espaços.
- Contagem regressiva de tentativas restantes.
- Mensagens de vitória ou derrota.
- Entrada de letra com validação simples.

---

## forca.py

```
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
```

---

## 📋 Exemplo de uso
=== Jogo da Forca ===
A palavra tem 7 letras.
Palavra: _ _ _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: p
Boa! A letra 'p' está na palavra.

Palavra: p _ _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: z
Ops! A letra 'z' não está na palavra.

Palavra: p _ _ _ _ _ _
Tentativas restantes: 5
Digite uma letra: y
Boa! A letra 'y' está na palavra.

...

Parabéns! Você adivinhou a palavra: python

---

## 🏷️ Tags

`python` `jogo` `forca` `terminal` `simples` `iniciante` `diversão`

---

## 📜 Licença

MIT

---

## 🤝 Contribuição

Contribuições são bem-vindas! Abra issues ou pull requests para melhorias.

---

## 📞 Contato

Desenvolvido por [rafael moreira](https://github.com/rafaelmoreirax)


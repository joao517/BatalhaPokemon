from random import randint

# variáveis 
jogar = True
escolherPokemon = True
escolherPokemonAdversario = True
batalha = True

# funções
def criarMenu(texto):
    print("=" * 50)
    print(f"{texto:^50}")
    print("=" * 50)

def bulbasaur():
    pokemon = {
        "nome": "Bulbasaur",
        "vida": 150,
        "tipo": "planta",
        "ataques": [["Vine Whip", 35], ["Razor Leaf", 50]],
    }        
    return pokemon

def squirtle():
    pokemon = {
        "nome": "Squirtle",
        "vida": 150,
        "tipo": "agua",
        "ataques": [["Bubble", 20], ["Water Gun", 40]],
    }        
    return pokemon

def charmander():
    pokemon = {
        "nome": "Charmander",
        "vida": 150,
        "tipo": "fogo",
        "ataques": [["Ember", 40], ["Fire Spin", 10]],
    }        
    return pokemon

def vantagensDesvantagens(pok1, pok2):
    if pok1["tipo"] == "planta" and pok2["tipo"] == "planta":
        return 1
    elif pok1["tipo"] == "planta" and pok2["tipo"] == "fogo":
        return 1
    elif pok1["tipo"] == "planta" and pok2["tipo"] == "agua":
        return 2
    elif pok1["tipo"] == "fogo" and pok2["tipo"] == "fogo":
        return 1
    elif pok1["tipo"] == "fogo" and pok2["tipo"] == "agua":
        return 1
    elif pok1["tipo"] == "fogo" and pok2["tipo"] == "planta":
        return 2
    elif pok1["tipo"] == "agua" and pok2["tipo"] == "agua":
        return 1
    elif pok1["tipo"] == "agua" and pok2["tipo"] == "planta":
        return 1
    elif pok1["tipo"] == "agua" and pok2["tipo"] == "fogo":
        return 2

# código principal
criarMenu("BEM VINDO AO JOGO DE POKÉMON")
while jogar:
    while True:
        querJogar = str(input("Você quer jogar? s/n: ")).lower().strip()[0]
        if querJogar == "s":
            break
        elif querJogar == "n":
            jogar = False
            break
        else:
            print("ERRO! Responda apenas s ou n")
    print("""Escolha o pokémon que você deseja usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
    while escolherPokemon:
        try:
            escolherPokemonParaUsar = int(input("Sua escolha: "))
            if escolherPokemonParaUsar > 3 or escolherPokemonParaUsar < 1:
                print("ERRO! Pokémon não encontrado, digite novamente")
            else:
                if escolherPokemonParaUsar == 1:
                    while True:
                        escolherBulbasaur = str(input("Você quer escolher o bulbasaur? s/n: ")).lower().strip()[0]
                        if escolherBulbasaur == "s":
                            meuPokemon = bulbasaur()
                            escolherPokemon = False
                            break
                        elif escolherBulbasaur == "n":
                            print("""Escolha o pokémon que você deseja usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
                elif escolherPokemonParaUsar == 2:
                    while True:
                        escolherSquirtle = str(input("Você quer escolher o squirtle? s/n: ")).lower().strip()[0]
                        if escolherSquirtle == "s":
                            meuPokemon = squirtle()
                            escolherPokemon = False
                            break
                        elif escolherSquirtle == "n":
                            print("""Escolha o pokémon que você deseja usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
                elif escolherPokemonParaUsar == 3:
                    while True:
                        escolherCharmander = str(input("Você quer escolher o Charmander? s/n: ")).lower().strip()[0]
                        if escolherCharmander == "s":
                            meuPokemon = charmander()
                            escolherPokemon = False
                            break
                        elif escolherCharmander == "n":
                            print("""Escolha o pokémon que você deseja usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
        except ValueError:
            print("ERRO! Responda apenas com números")
    print("""Escolha o pokémon pro seu inimigo usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
    while escolherPokemonAdversario:
        try:
            escolherPokemonInimigo = int(input("Sua escolha: "))
            if escolherPokemonInimigo > 3 or escolherPokemonInimigo < 1:
                print("ERRO! Pokémon não encontrado, digite novamente")
            else:
                if escolherPokemonInimigo == 1:
                    while True:
                        escolherBulbasaurInimigo = str(input("Você quer escolher o bulbasaur? s/n: ")).lower().strip()[0]
                        if escolherBulbasaurInimigo == "s":
                            pokemonInimigo = bulbasaur()
                            escolherPokemonAdversario = False
                            break
                        elif escolherBulbasaurInimigo == "n":
                            print("""Escolha o pokémon pro seu inimigo usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
                elif escolherPokemonInimigo == 2:
                    while True:
                        escolherSquirtleInimigo = str(input("Você quer escolher o squirtle? s/n: ")).lower().strip()[0]
                        if escolherSquirtleInimigo == "s":
                            pokemonInimigo = squirtle()
                            escolherPokemonAdversario = False
                            break
                        elif escolherSquirtleInimigo == "n":
                            print("""Escolha o pokémon pro seu inimigo usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
                elif escolherPokemonInimigo == 3:
                    while True:
                        escolherCharmanderInimigo = str(input("Você quer escolher o Charmander? s/n: ")).lower().strip()[0]
                        if escolherCharmanderInimigo == "s":
                            pokemonInimigo = charmander()
                            escolherPokemonAdversario = False
                            break
                        elif escolherCharmanderInimigo == "n":
                            print("""Escolha o pokémon pro seu inimigo usar:
[ 1 ] - Bulbasaur
[ 2 ] - Squirtle
[ 3 ] - Charmander""")
                            break
                        else:
                            print("ERRO! Responda apenas s ou n")
        except ValueError:
            print("ERRO! Responda apenas com números")
    criarMenu("Gerando batalha...")
    vantagem = vantagensDesvantagens(meuPokemon, pokemonInimigo)
    while batalha:
        dano = 0
        danoInimigo = 0 
        if meuPokemon["vida"] <= 0:
            print("Poxa! Você perdeu, mais sorte na próxima")
            print("=" * 50)
            jogar = False
            batalha = False
        elif pokemonInimigo["vida"] <= 0:
            print("=" * 50)
            print("Parabéns! Você ganhou a batalha")
            print("=" * 50)
            jogar = False
            batalha = False
        else:
            print(f'{meuPokemon["nome"]} - Vida: {round(meuPokemon["vida"])}')
            print(f'{pokemonInimigo["nome"]} - Vida: {round(pokemonInimigo["vida"])}')
            print(f"Que ataque você deseja usar? \n[ 1 ] - {meuPokemon['ataques'][0][0]} - dano {meuPokemon['ataques'][0][1]} \n[ 2 ] - {meuPokemon['ataques'][1][0]} - dano {meuPokemon['ataques'][1][1]}")
            while True:
                try:
                    ataqueUsar = int(input("Sua escolha: "))
                    print("=" * 50)
                    if ataqueUsar < 1 or ataqueUsar > 2:
                        print("Erro! Digite apenas 1 ou 2")
                    elif ataqueUsar == 1:
                        print(f"Você escolheu o {meuPokemon['ataques'][0][0]}")
                        if vantagem == 1:
                            dano += meuPokemon["ataques"][0][1] / 2
                        elif vantagem == 2:
                            dano += meuPokemon["ataques"][0][1] * 2
                    elif ataqueUsar == 2:
                        print(f"Você escolheu o {meuPokemon['ataques'][1][0]}")
                        if vantagem == 1:
                            dano += meuPokemon["ataques"][1][1] / 2
                        elif vantagem == 2:
                            dano += meuPokemon["ataques"][1][1] * 2
                    print(f"Você deu {dano} de dano")
                    pokemonInimigo["vida"] = pokemonInimigo["vida"] - dano
                    if pokemonInimigo["vida"] > 0:
                        print(f'O pokémon inimigo ficou com {pokemonInimigo["vida"]} de vida')
                    else:
                        print('O pokémon inimigo ficou com 0 de vida')
                        break
                    print("=" * 50)
                    ataqueInimigo = randint(1,2)
                    if ataqueInimigo == 1:
                        print(f'O inimigo escolheu {pokemonInimigo["ataques"][0][0]}')
                        if vantagem == 1:
                            danoInimigo += pokemonInimigo["ataques"][0][1] * 2
                        if vantagem == 2:
                            danoInimigo += pokemonInimigo["ataques"][0][1] / 2
                    elif ataqueInimigo == 2:
                        print(f'O inimigo escolheu {pokemonInimigo["ataques"][1][0]}')
                        if vantagem == 1:
                            danoInimigo += pokemonInimigo["ataques"][1][1] * 2
                        if vantagem == 2:
                            danoInimigo += pokemonInimigo["ataques"][1][1] / 2
                    print(f'O inimigo deu {round(danoInimigo)}')
                    meuPokemon["vida"] = meuPokemon["vida"] - danoInimigo
                    if meuPokemon["vida"] > 0:
                        print(f'O {meuPokemon["nome"]} ficou com {round(meuPokemon["vida"])} de vida')
                    else:
                        print(f'O {meuPokemon["nome"]} inimigo ficou com 0 de vida')
                    print("=" * 50)
                    break
                except ValueError:
                    print("ERRO! Digite apenas números")
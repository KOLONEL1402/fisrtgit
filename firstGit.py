import random
print('bonjour')

def jeu_A():
    capital = 100
    while capital > 0:
        capital = capital - 1
        if random.random() < 0.49:
            capital += 2
    return capital


nb_parties = 100

# Simulation du jeu A
gains_A = [jeu_A() > 1000 for _ in range(nb_parties)]
proba_gagner_A = sum(gains_A) / nb_parties
print("Probabilité de gagner dans le jeu A :", proba_gagner_A)

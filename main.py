import random
import time
contador = 0
nivel = 3

Data = {
  "Alpha": "Ronaldo",
  "Beta": "54",
  "Omega": "Computer",
  "Delta": "Obama",
  "Omicron": "Milena",
  "Gamma": "Banana",
  "Theta": "Carne",
  "Iota": "Apple",
  "Kappa": "Computer",
  "Lambda": "Brasilia"
}

print("Bem Vindo a Mind Games!")
time.sleep(3)
print("Memorize os dados que aparecem na Tela")
time.sleep(3)
print("Ex: Delta = Obama. Você precisa memorizar e digitar somente Obama.")
time.sleep(5)
print("Agora é sua vez de testar sua memória com Mind Games!")
time.sleep(3)
print("Ready! Go!")
time.sleep(3)


# Get a random key from the dictionary
random_key = random.choice(list(Data.keys()))

# Access the value using the randomly selected key

while contador >= 0 and contador < 10:
  is_game_over = False
  random_keys = random.sample(list(Data.keys()), nivel)
  random_values = [Data[key] for key in random_keys]
  
  # Print the randomly selected key-value pair
  for i in range(nivel):
    print(f"Memoriza esses dados em ordem: {random_keys[i]} = {random_values[i]}")
    
  time.sleep(5)
  for _ in random_values:
    lines = random_values[i].count("\n") + 1  # Count the number of lines in the text
    print(f"\033[{lines}A\033[K", end='') 

  user_inputs = []
  for i in range(len(random_values)):
    user_input = input("Entre um valor e pressione Enter: ").capitalize()
    user_inputs.append(user_input)

  for i in range(len(random_values)):
    if user_inputs[i] == random_values[i]:
      correto = True
    else:
      correto = False
      break

  if correto:
    contador += 1
    print(f"Super! Você tem {contador} pontos")
  else: 
    contador -= 1
    nivel -= 1
    print(f"Não conseguiu! Você tem {contador} pontos")
  nivel += 1

if contador < 0 :
  is_game_over = True
  print("GAME OVER! Perdeu o Mind Games!")
elif contador == 10:
  is_game_over = True
  print("Parabéns! Você é Mestre do Mind Games")
  

from tkinter import *
import random
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

def start_game():
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

  print("Bem Vindo a Mind Games")
  print("Memorize os valores que aparecem na Tela\nVocê tem 5 segundos")

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
      user_input = input(f"Entre os valores memorizados na ordem correta: ").capitalize()
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
    

window = Tk()
window.title("Mind Games")
window.config(padx=100, pady=50, bg=YELLOW)

#We use canvas to insert an image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
brain_img = PhotoImage(file="/images/brain.png")
canvas.create_image(100, 112, image=brain_img)
timer = canvas.create_text(100, 130, text="0:0", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command= start_game, highlightthickness=0 )
start_button.grid(column=0, row=2)

#reset_button = Button(text="Reset", command= reset_timer, highlightthickness=0)
#reset_button.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)




window.mainloop()
  

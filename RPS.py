import pygame
import random
import time
pygame.init()

#variables and constants
BG_COLOR = "#8760C9"
player_1 = ""
running = True
processed = False
pause = False
spock_or_rock = False
game_type = False
screen = pygame.display.set_mode([1200,900])
type_dict = {"Rock": 1,"Paper": 2,"Scissors": 3,"Lizard": 4,"Spock": 5}
comp_choice_dict = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard",5:"Spock"}
Comp_Rock = {1: "Tie", 2: "Win", 3: "Lose", 4: "Lose", 5: "Win"}
Comp_Paper = {1: "Lose", 2: "Tie", 3: "Win", 4: "Win", 5: "Lose"}
Comp_Scissor = {1: "Win", 2: "Lose", 3: "Tie", 4: "Lose", 5: "Win"}
Comp_Lizard = {1: 'Win', 2: 'Lose', 3: 'Win', 4: 'Tie', 5: 'Lose'}
Comp_Spock = {1: "Lose", 2: "Win", 3: "Lose", 4: "Win", 5: "Tie"}
count_dict = {"Win": 0, "Lose": 0, "Tie": 0}

#assetes go here
RPS_image = pygame.image.load("assets/images/RPSImage.png")
RPS_image = pygame.transform.scale(RPS_image, (200,200))
RPSLSp_image = pygame.image.load("assets/images/RPSLSpImage.png")
RPSLSp_image = pygame.transform.scale(RPSLSp_image, (200,200))
rock_image = pygame.image.load("assets/images/rock.jpeg")
rock_image = pygame.transform.scale(rock_image, (200,200))
scissors_image = pygame.image.load("assets/images/scissors.jpeg")
scissors_image = pygame.transform.scale(scissors_image, (200,200))
paper_image = pygame.image.load("assets/images/paper.jpeg")
paper_image = pygame.transform.scale(paper_image, (200,200))
Lizard_image = pygame.image.load("assets/images/Lizard.jpg")
Lizard_image = pygame.transform.scale(Lizard_image, (200,200))
Spock_image = pygame.image.load("assets/images/Spock.jpg")
Spock_image = pygame.transform.scale(Spock_image, (200,200))
rps_blit = screen.blit(RPS_image, (400,200))
rpslSp_blit = screen.blit(RPSLSp_image, (200,200))
rocky = screen.blit(rock_image, (50,200))
scissorz = screen.blit(scissors_image, (550,200))
papers = screen.blit(paper_image, (300,200))
Lizard_blit = screen.blit(Lizard_image, (300,200))
Spock_blit = screen.blit(Spock_image, (300,200))

#functions to make interactable objects
def text_func(text,x,y,font,size,color):
   set_my_font = pygame.font.SysFont(font, size)
   textSurface = set_my_font.render(text, True, color)
   screen.blit(textSurface, (x,y))

def random_to_type(game_type):
 if not game_type:
  return random.randint(1,5)
 return random.randint(1,3)

def descision(rand_int, type):
  if rand_int == 1:
    winlosetie = f"{Comp_Rock[type]}"
  elif rand_int == 2:
    winlosetie = f"{Comp_Paper[type]}"
  elif rand_int == 3:
    winlosetie = f"{Comp_Scissor[type]}"
  elif rand_int == 4:
    winlosetie = f"{Comp_Lizard[type]}"
  else:
    winlosetie = f"{Comp_Spock[type]}"
  return winlosetie

def increment(g):
  count_dict[g] += 1
  return count_dict

while running:

 #get input
  for event in pygame.event.get():
    screen.fill(BG_COLOR)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pause = not pause
      if event.key == pygame.K_x:
        running = False
    if not pause:
      if not spock_or_rock:
        rps_blit = screen.blit(RPS_image, (200,600))
        rpslSp_blit = screen.blit(RPSLSp_image, (800,600))
        text_func("Would you like to play RPS or RPSLSp?",60,50,"arial",60,"black")
        text_func("Pick Left for RPS, and Right for RPSLSp",60,200,"arial",60,"black")
        text_func(f"Here is your Current Score: {count_dict}",100,350,"arial",40,"black")
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_x, mouse_y = event.pos
          if rps_blit.collidepoint(mouse_x,mouse_y):
            #RPS IS SELECTED, game_type = True
            game_type = True
            spock_or_rock = True
          elif rpslSp_blit.collidepoint(mouse_x,mouse_y):
            #RPSLSp IS SELECTED, game_type = False
            game_type = False
            spock_or_rock = True
      if spock_or_rock:
        if game_type:
          rocky = screen.blit(rock_image, (220,150))
          scissorz = screen.blit(scissors_image, (770,150))
          papers = screen.blit(paper_image, (495,150))
        if not game_type:
          rocky = screen.blit(rock_image, (220,150))
          scissorz = screen.blit(scissors_image, (770,150))
          papers = screen.blit(paper_image, (495,150))
          Lizard_blit = screen.blit(Lizard_image, (650,375))
          Spock_blit = screen.blit(Spock_image, (350,375))
        if player_1 == "":
          if event.type == pygame.QUIT:
              running = False
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_r:
                  player_1 = "Rock"
              elif event.key == pygame.K_p:
                  player_1 = "Paper"
              elif event.key == pygame.K_s:
                  player_1 = "Scissors"
              elif not game_type:
                if event.key == pygame.K_l:
                  player_1 = "Lizard"
                if event.key == pygame.K_s:
                  player_1 = "Spock"
          if event.type == pygame.MOUSEBUTTONDOWN:
              mouse_x, mouse_y = event.pos
              if rocky.collidepoint(mouse_x,mouse_y):
                  player_1 = "Rock"
              elif scissorz.collidepoint(mouse_x,mouse_y):
                  player_1 = "Scissors"
              elif papers.collidepoint(mouse_x,mouse_y):
                  player_1 = "Paper"
              if not game_type:
                if Lizard_blit.collidepoint(mouse_x,mouse_y):
                  player_1 = "Lizard"
                elif Spock_blit.collidepoint(mouse_x,mouse_y):
                  player_1 = "Spock"          
        if player_1 != "":
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
              running = False
            elif event.key == pygame.K_y:
              player_1 = ""
              processed = False
              spock_or_rock = False

      #process input
      if not pause:
        if player_1 != "" and processed == False:
          comp_rand_int = random_to_type(game_type)
          comp_choice = comp_choice_dict[comp_rand_int]
          result = descision(comp_rand_int, type_dict[player_1])
          count_dict = increment(result)
          processed = True

        #update game state
        if player_1 == "" and spock_or_rock:
          text_func("Select an Option",375,600,"arial",60,"black")
        if player_1 != "":
          text_func(f"You Selected {player_1}!",310,40,"arial",60,"black")
          text_func(f"You {result}!",475,675,"arial",60,"black")
          text_func(f"Computer Choose {comp_choice}!",260,600,"arial",60,"black")
          text_func("Play Again? Y or N",350,750,"arial",60,"black")
      
    else:
      text_func("Press Escape To Unpause",235,50,"arial",60,"black")
      text_func("Press X to Quit",375,125,"arial",60,"black")
  
  text_func("Press Esc To Pause",50,850,"arial",30,"black")
  
 #draw screen
  pygame.display.flip()

pygame.quit()





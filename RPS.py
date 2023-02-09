import pygame
import random
pygame.init()


#variables and constants
BG_COLOR = "#8760C9"
player_1 = ""
play_again = True
running = True
result_input = False
screen = pygame.display.set_mode([800,600])
type_dict = {"Rock": 1,"Paper": 2,"Scissors": 3}
Comp_Rock = {1: "Tie", 2: "Win", 3: "Lose"}
Comp_Paper = {1: "Lose", 2: "Tie", 3: "Win"}
Comp_Scissor = {1: "Win", 2: "Lose", 3: "Tie"}
count_dict = {"Win": 0, "Lose": 0, "Tie": 0}


#assetes go here
rock_image = pygame.image.load("assets/images/rock.jpeg")
rock_image = pygame.transform.scale(rock_image, (200,200))
scissors_image = pygame.image.load("assets/images/scissors.jpeg")
scissors_image = pygame.transform.scale(scissors_image, (200,200))
paper_image = pygame.image.load("assets/images/paper.jpeg")
paper_image = pygame.transform.scale(paper_image, (200,200))
rocky = screen.blit(rock_image, (50,200))
scissorz = screen.blit(scissors_image, (550,200))
papers = screen.blit(paper_image, (300,200))


#functions to make interactable objects
def rock(x,y):
   screen.blit(rock_image, (x,y))
   #unused


def scissors(x,y):
   screen.blit(scissors_image, (x,y))
   #unused


def paper(x,y):
   screen.blit(paper_image, (x,y))
   #unused


def text_func(text,x,y,font,size,color):
   set_my_font = pygame.font.SysFont(font, size)
   textSurface = set_my_font.render(text, True, color)
   screen.blit(textSurface, (x,y))


def random_to_type():
 computer_rand_int = random.randint(0,3)
 return computer_rand_int


def descision(rand_int, type):
 if rand_int == 1:
   #chose = (f"\nComputer Chose Rock \n{Comp_Rock[type]}\n")
   winlosetie = Comp_Rock[type]
 elif rand_int == 2:
   #chose = (f"\nComputer Chose Paper \n{Comp_Paper[type]}\n")
   winlosetie = Comp_Paper[type]
 else:
   #chose = (f"\nComputer Chose Scissors \n{Comp_Scissor[type]}\n")
   winlosetie = Comp_Scissor[type]
 return winlosetie


while running:


 #get input
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         running = False
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_r:
             player_1 = "Rock"
         elif event.key == pygame.K_p:
             player_1 = "Paper"
         elif event.key == pygame.K_s:
             player_1 = "Scissors"
     if event.type == pygame.MOUSEBUTTONDOWN:
         mouse_x, mouse_y = event.pos
         if rocky.collidepoint(mouse_x,mouse_y):
             player_1 = "Rock"
         elif scissorz.collidepoint(mouse_x,mouse_y):
             player_1 = "Scissors"
         elif papers.collidepoint(mouse_x,mouse_y):
             player_1 = "Paper"


 #process input
 if player_1 != "":
     result = descision(random_to_type(), type_dict[player_1])
 if result_input == True:
   text_func("Play Again? Y or N",135,500,"arial",60,"black")
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_n:
       running = False


 #update game state
 screen.fill(BG_COLOR)
 if player_1 == "":
   rocky
   scissorz
   papers
 if player_1 != "":
     text_func(f"You Selected {player_1}!",135,500,"arial",60,"black")
     while result_input == False:
       text_func("Are you ready to see your results? Type Y!",135,500,"arial",60,"black")
       if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_y:
           text_func(f"You {result}!",135,500,"arial",60,"black")
           result_input = True
        
 #draw screen
 pygame.display.flip()


pygame.quit()



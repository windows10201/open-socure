import os

def main():
	print(logo)
	print(menu)
	
	
logo = ("""\033[31;1m
                                         
                                         
____              ___ ___    __   ____   
`Mb(      db      )d' `MM    d'  @6MMMMb/ 
 YM.     ,PM.     ,P   MM   d'  8P    YM 
 `Mb     d'Mb     d'   MM  d'  6M      Y 
  YM.   ,P YM.   ,P    MM d'   MM        
  `Mb   d' `Mb   d'    MMd'    MM        
   YM. ,P   YM. ,P     MMYM.   MM        
   `Mb d'   `Mb d'     MM YM.  MM        
    YM,P     YM,P      MM  YM. YM      6 
    `MM'     `MM'      MM   YM. 8b    d9 
     YP       YP      _MM_   YM._YMMMM9  


\033[38;5;46m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★                                         

\033[31;1m══════════════════════════════════════════════
\033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱  
\033[38;5;46mNAME : SIAM
\033[38;5;46mGITHUB : WOLF-KING-21
\033[0;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱  
\033[31;1m══════════════════════════════════════════════
\033[38;5;46m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""")
menu = ("""[1]>RANDOM CLONE
[2]>FILE CLONE
[3]>FOLLOW MY FACEBOOK ID
\033[38;5;46m★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""")
def siam():
	os.system('espeak -a 500 " You are a motherfucker "')
	os.system('clear')
	print(logo)
	print(menu)
	ab = input("[√]CHOICE OPTION:--->>> ")
	if ab=='1':
		ai()
	if ab=='2':
		bi()
	if ab=='3':
		ci()
		
def ai():
	print(" random clone ad kori nsi ")
	
def bi():
	print(" fuck ")
	
def ci():
	print(" ki ")
	
	
siam()
	
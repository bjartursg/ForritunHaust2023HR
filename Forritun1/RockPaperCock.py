import math
import random
tie=""" 
   ITS A TIE! BORING!!! GAAA!!!
    ______
   /(    )\.
   \ \  / /
    \/[]\/
      /\.
     |  |
     |  |
     |  |
     |  |
     |  |
     \  /   
      \/"""
Bwins="""
             BJARTUR WINS!!!! YEEESS!!!YEEEESS!!!
                         .       .
                         |\_---_/|
                        /   o_o   \.
                        |    U    |
                        \  ._I_.  /
                         `-_____-'
 """
Fwins="""
          FRIKKI WIN!!!! YEEESESYESSSSYESYES!!!! YESS!
                        ^..^      /
                        /_/\_____/
                           /\   /\.
                         /  \ /  \.
    """
rock="""  
          ROCK!!!!!!
  .----.-----.-----.-----.
 /      \     \     \     \.
|  \/    |     |   __L_____L__
|   |    |     |  (           \.
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |"""

paper="""  
      PAPAER!!!    
       _.-._
     /| | | |_
     || | | | |
     || | | | |
    _||     ` |
   \.\`\       ;
    \.\        |
     \.\      /
     | |    |
     | |    |"""
Scissors="""  
        SCISSORS!!!!!   
     ."".    ."",
     |  |   /  /
     |  |  /  /
     |  | /  /
     |  |/  ;-._
     }  ` _/  / ;
     |  /` ) /  /
     | /  /_/\_/\.
     |/  /      |
     (  ' \ '-  |
      \    `.  /
       |      |
       |      |
"""
Fpoints=0
Bpoints=0
while (True):
    f=random.randint(1,3)
    b=random.randint(1,3)
    input("")

    if(Fpoints == 3 or Bpoints == 3): break

    if f==1:
        print ("Frikki Threw out!")
        print (rock)
    if f==2:
        print ("Frikki Threw out!")
        print (paper)
    if f==3:
        print ("Frikki Threw out!")
        print (Scissors)
    input ("")
    if b==1:
        print ("Bjartur Threw out!")
        print (rock)
    if b==2:
        print ("Bjartur Threw out!")
        print (paper)
    if b==3:
        print ("Bjartur Threw out!")
        print (Scissors)
    input ("")
    if b==f:
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print("NOONE GETS POINTS!! ITS A TIE!!")
        print (tie)
    if (b==1 and f==2):
        Fpoints=Fpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Fwins)
        
    if (f==1 and b==2):
        Bpoints=Bpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Bwins)
        
    if (b==1 and f==3):
        Bpoints=Bpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Bwins)
        
    if (f==1 and b==3):
        Fpoints=Fpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Fwins)
        
    if (b==2 and f==3):
        Fpoints=Fpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Fwins)
        
    if (f==2 and b==3):
        Bpoints=Bpoints+1
        print (f"Frikki has {Fpoints} points : Bjartur has {Bpoints} points")
        print (Bwins)

        
    
        


    
    


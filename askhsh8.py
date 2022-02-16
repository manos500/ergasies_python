import random

#declare x,y values based on board size
for boards in range(3):
    if boards == 0:
        x_range = 8
        y_range = 8
        board_size = '8x8'
    elif boards == 1:
         x_range = 7
         y_range = 7
         board_size = '7x7'
    else:
         x_range = 7
         y_range = 8 
         board_size = '7x8' 
  
    white_root_points = 0
    black_bishop_points = 0
      
    for times_played in range(100):
    #Place white root and black bishop in random posititons on board and check if they have the same position
        is_True = True
        while(is_True):
            random_root_positionX = random.randint(0,x_range-1)
            random_root_positionY = random.randint(0,y_range-1)
            random_bishop_positionX = random.randint(0,x_range-1)
            random_bishop_positionY = random.randint(0,y_range-1)
            if(random_root_positionX != random_bishop_positionX) or (random_root_positionY != random_bishop_positionY):
                is_True = False
        

        #find when white root kills black bishop
        if(random_root_positionX == random_bishop_positionX) or (random_root_positionY == random_bishop_positionY):
            white_root_points = white_root_points + 1

    #find when black bishop kills white root
        s = False
        
    # down and left
        i = 0
        while((random_bishop_positionX + i <= x_range-1) and (random_bishop_positionY - i >= 0)):
            if (random_root_positionX == random_bishop_positionX + i) and (random_root_positionY == random_bishop_positionY - i):
                s = True
            i = i + 1    


    # down and right
        i = 0
        if s == False:
            while((random_bishop_positionX + i <= x_range-1) and (random_bishop_positionY + i <= y_range-1)):
                if (random_root_positionX == random_bishop_positionX + i) and (random_root_positionY == random_bishop_positionY + i):
                    s = True
                i = i + 1    
                    

    # up and right
        i = 0
        if s == False:
            while((random_bishop_positionX - i >= 0) and (random_bishop_positionY + i <= y_range-1)):
                if (random_root_positionX == random_bishop_positionX - i) and (random_root_positionY == random_bishop_positionY + i):
                    s = True
                i = i + 1    

    # up and left 
        i = 0          
        if s == False:
            while((random_bishop_positionX - i >= 0) and (random_bishop_positionY - i >= 0)):
                if (random_root_positionX == random_bishop_positionX - i) and (random_root_positionY == random_bishop_positionY - i):
                    s = True
                i = i + 1  


        if s == True:
            black_bishop_points = black_bishop_points + 1

    print('Score after 100 games on ' + board_size + ' board')
    print('White root score: '+str(white_root_points))
    print('Black bishop score: '+str(black_bishop_points))
    print('----------------------------------')


 




 
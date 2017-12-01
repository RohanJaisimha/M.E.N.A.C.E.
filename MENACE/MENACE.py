from random import *
import os
import matplotlib.pyplot as plt

def pickWhereToPlay(box):
  return choice(box)

def compareGrid(grid1,grid2):
  for i in range(9):
    if(grid1[i]!=grid2[i]):
      return False
  return True

def checkRows():
  for i in range(3):
    if(main_grid[3*i]==main_grid[3*i+1] and main_grid[3*i]==main_grid[3*i+2] and main_grid[3*i]!='0'):
      return True
  return False

def checkCols():
  for i in range(3):
    if(main_grid[i]==main_grid[i+3] and main_grid[i]==main_grid[i+6] and main_grid[i]!='0'):
      return True
  return False

def checkDiags():
  #Check Principal Diagonal
  if(main_grid[0]==main_grid[4] and main_grid[0]==main_grid[8] and main_grid[0]!='0'):
    return True
  
  #Check Non-Principal Diagonal
  if(main_grid[2]==main_grid[4] and main_grid[2]==main_grid[6] and main_grid[2]!='0'):
    return True
  return False

def isSolved():
  return checkRows() or checkCols() or checkDiags()    

def letComputerPlay():
  fin=open("Combinations.txt","r")
  possible_moves=['TL','TC','TR','ML','MC','MR','BL','BC','BR']
  for i in range(2423):
    whereToPlay=fin.readline().strip().split()
    t_grid=list(whereToPlay.pop(0))
    if(len(whereToPlay)==0):
      return 0
    if(compareGrid(main_grid,t_grid)):
      positions_played.append(pickWhereToPlay(whereToPlay))    
      boxes_used.append(i) 
      break
  fin.close()
  main_grid[possible_moves.index(positions_played[len(positions_played)-1])]='1'   
  return 1

def printGrid():
  symbols=[' ','X','O']
  print("\n\n")
  for i in range(9):    
    if(i==3 or i==6):
      print("\n--+---+--")
    print(symbols[int(main_grid[i])],end="")
    if(i%3!=2):
      print(" | ",end="")

def letPlayerPlay():
  while(True):
    possible_moves=['TL','TC','TR','ML','MC','MR','BL','BC','BR']
    print("\n\nUse this for help as to where to play")
    for i in range(9):    
      if(i==3 or i==6):
        print("\n---+----+---")
      print(possible_moves[i],end="")
      if(i%3!=2):
        print(" | ",end="")
    print("\nWhere do you want to play?")
    choice=input()
    if(choice not in possible_moves or main_grid[possible_moves.index(choice)]!='0'):
      print("That is an illegal move")
    else:
      break
  
  main_grid[possible_moves.index(choice)]='2'
  
def main():
  win=3
  for i in range(6):
    if(letComputerPlay()==0):      
      print("\nComputer resigns")
      win=-1
      break
    printGrid()
    if(isSolved()):
      print("\nComputer wins")
      win=1
      break
    if('0' not in main_grid):
      print("\nDraw")
      win=0
      break
    letPlayerPlay()
    if(isSolved()):
      print("\nPlayer wins")
      win=-1
      break
    printGrid()
  if(win==1): #Win for Computer
    fin=open("Combinations.txt",'r')
    fout=open("Temp.txt",'w')
    for i in range(2423):
      t_line=fin.readline().strip()
      if(i not in boxes_used):
        fout.write(t_line+'\n')
      else:
        fout.write(t_line+' '+positions_played[boxes_used.index(i)]+' '+positions_played[boxes_used.index(i)]+' '+positions_played[boxes_used.index(i)]+'\n')
    fout.close()
    fin.close()
    os.remove("Combinations.txt")
    os.rename("Temp.txt","Combinations.txt")

  if(win==0): #Draw
    fin=open("Combinations.txt",'r')
    fout=open("Temp.txt",'w')
    for i in range(2423):
      t_line=fin.readline().strip()
      if(i not in boxes_used):
        fout.write(t_line+'\n')
      else:
        fout.write(t_line+' '+positions_played[boxes_used.index(i)]+'\n')
    fout.close()
    fin.close()
    os.remove("Combinations.txt")
    os.rename("Temp.txt","Combinations.txt")

  if(win==-1): #Win for player
    fin=open("Combinations.txt",'r')
    fout=open("Temp.txt",'w')
    for i in range(2423):
      t_line=fin.readline().strip()
      if(i not in boxes_used):
        fout.write(t_line+'\n')
      else:
        if(i==0 and len(t_line.split())==2):
          fout.write(t_line+'\n')
        else:
          fout.write(t_line.replace(positions_played[boxes_used.index(i)],"",1)+'\n')
    fout.close()
    fin.close()
    os.remove("Combinations.txt")
    os.rename("Temp.txt","Combinations.txt")    

  #put into data file
  fin=open("Data.txt",'r')
  num_times_played=len(fin.readlines())-1
  fin.close()
  fout=open("Data.txt",'a')
  fin1=open("Combinations.txt",'r')
  num_in_first_box=fin1.readline().strip().split()
  fin1.close()
  fout.write(str(num_times_played+1)+"\t"+str(len(num_in_first_box)-1)+"\n")
  fout.close()
  
  #plot on graph
  fin=open("Data.txt",'r')
  x_values=[]
  y_values=[]
  flag=True
  plt.xlabel("Number of games played")
  plt.ylabel("Number of possible moves in first position")
  for line in fin:
    line=line.strip().split()
    if(flag):
      flag=False
    else:
      x_values.append(int(line[0]))
      y_values.append(int(line[1]))
  plt.plot(x_values,y_values)
  plt.xlim(0)
  plt.ylim(0)
  plt.title('Data')
  plt.savefig('Data.pdf')

main_grid=['0','0','0','0','0','0','0','0','0']
boxes_used=[]
positions_played=[]
main()

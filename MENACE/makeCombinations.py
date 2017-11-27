import os

def count(text,char):
  count=0
  for i in text:
    if(i==char):
      count+=1
  return count

def checkRows(combination):
  for i in range(3):
    if(combination[3*i]==combination[3*i+1] and combination[3*i]==combination[3*i+2] and combination[3*i]!='0'):
      return True
  return False

def checkCols(combination):
  for i in range(3):
    if(combination[i]==combination[i+3] and combination[i]==combination[i+6] and combination[i]!='0'):
      return True
  return False

def checkDiags(combination):
  #Check Principal Diagonal
  if(combination[0]==combination[4] and combination[0]==combination[8] and combination[0]!='0'):
    return True
  
  #Check Non-Principal Diagonal
  if(combination[2]==combination[4] and combination[2]==combination[6] and combination[2]!='0'):
    return True
  return False

def isSolved(combination):
  return checkRows(combination) or checkCols(combination) or checkDiags(combination)    

def removeAllSolvedOnes():
  fin=open("Combinations.txt",'r')
  fout=open("Temp.txt",'w')
  for line in fin:
    t_line=line.strip()
    if(not isSolved(t_line)):
      fout.write(t_line+'\n')
  fout.close()
  fin.close()
  os.remove("Combinations.txt")
  os.rename("Temp.txt","Combinations.txt")
  
def removeBadOnes():
  fin=open("Combinations.txt",'r')
  fout=open("Temp.txt",'w')
  for line in fin:
    t_line=line.strip()
    count_0=count(t_line,'0')
    count_1=count(t_line,'1')
    count_2=count(t_line,'2')
    if(count_1==count_2):
      fout.write(t_line+'\n')
  fout.close()
  fin.close()
  os.remove("Combinations.txt")
  os.rename("Temp.txt","Combinations.txt")

def addPossibleMoves():
  fin=open("Combinations.txt",'r')
  fout=open("Temp.txt",'w')
  possible_moves=['TL','TC','TR','ML','MC','MR','BL','BC','BR']
  for line in fin:
    t_line=line.strip()
    fout.write(t_line+' ')
    for j in range(9):
      if(t_line[j]=='0'):
        fout.write(possible_moves[j]+' ')
    fout.write('\n')
  fout.close()
  fin.close()
  os.remove("Combinations.txt")
  os.rename("Temp.txt","Combinations.txt")

def main():
  fout=open("Combinations.txt",'w')
  for i1 in range(3):
    for i2 in range(3):
      for i3 in range(3):
        for i4 in range(3):
          for i5 in range(3):
            for i6 in range(3):
              for i7 in range(3):
                for i8 in range(3):
                  for i9 in range(3):
                    fout.write(str(i1)+str(i2)+str(i3)+str(i4)+str(i5)\
                    +str(i6)+str(i7)+str(i8)+str(i9)+"\n")
  fout.close()
  removeBadOnes()
  removeAllSolvedOnes()
  addPossibleMoves()

main()

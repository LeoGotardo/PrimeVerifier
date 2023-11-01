import tkinter

def verify(pri):
  if pri == 0:
    return True

  test = 0
  cont = 2

  while cont < pri and cont > 1:
    test = test + pri % cont
    cont =+ 1
  
  if test < 0:
    return False
  else:
    return True
  
def main():
  x = 1
  primo = []
  n = int(input(f"Digite a quantidade de números que deseja verificar"))
  TK().bind("Esc",Exit())

  while(x < n):
    num[x] = [int(input(f"Digite o {x}° número para verificação:"))]
    print("(Press ESC to exit)")
    
    if verify(num[x]) == True:
      num[x].append(primo)
    
    x+=1

  if len(primo) > 0:
    print(f"Esses são os números primos:{primo}")
  else:
    print(f"Não foi dado nenhum número primo.")


main()
print("Shopping list")

slist = []
quit = False
q = 0


def add_list(n, q):
    slist.append(n + " x " + str(q))
    return slist


print("\n\n'quit' to quit \n'delete' to delete a specific item \n'return' to delete the last entered item.\n 'finished' to print the finished list.\n")

while quit != True:

    n = input(" Enter your item you wish to add: ")

    if n == 'quit':
        quit = True
    elif n == 'delete':
      x = input(" Enter which item you would like to remove: ")
      slist.remove(x)
      print(slist)
    elif n == 'return':
      slist.pop()
      print(slist)
    elif n == 'finished':
      print(" ")
      for i in range(0, len(slist)):
        new = slist[i].capitalize()
        print(" " + new, sep=", ")
      quit = True
    else:
        q = int(input(" Enter quantity: "))
        add_list(n, q)
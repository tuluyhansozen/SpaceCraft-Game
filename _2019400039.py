
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
board = []
for i in range(x):
    board.append(list())
    for j in range(y):
        board[i].append('*')
for i in range(g):
    board.append(list())
    for j in range(y):
        board[i+x].append(' ')
board.append(list())
spacecraft_index = int((y+1)/2 if y%2==1 else y/2)-1
for j in range(y):
    if j==spacecraft_index:
        board[x+g].append('@')
    else:
        board[x+g].append(' ')

spacecraft_x = x+g
spacecraft_y = spacecraft_index
time :int = 0
count = 0
if x*y  == 0:
    print("YOU WON!")
    for i in range(x+g+1):
        for j in range(y):
            print(board[i][j], end = "")
        print()
    print("-" * 72)
    print("YOUR SCORE: 0")
else:
    for i in range(x+g+1):
        for j in range(y):
            print(board[i][j], end = "")
        print()
    print("-" * 72)
    print("Choose your action!")
    ilkinput = str(input()).lower()


    while True:

        time += 1
        if ilkinput == str("right"):
            spacecraft_y_old = spacecraft_y
            spacecraft_y = spacecraft_y + 1 if spacecraft_y != y-1 else spacecraft_y
            board[spacecraft_x][spacecraft_y_old] = ' '
            board[spacecraft_x][spacecraft_y] = '@'
            if time % 5 == 0:
                if ("*" in board[spacecraft_x-1]):
                    print("GAME OVER")
                    for i in range(x+g++1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
                    laststars = sum(x.count("*") for x in board)
                    score = x*y- laststars
                    print("YOUR SCORE:",score)
                    break

                else:
                    del board[spacecraft_x-1]
                    for i in range(1):
                        board.insert(0,list())
                        for j in range(y):
                            board[i].append(" ")
                    for i in range(x+g+1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
            else:
                for i in range(x+g+1):
                    for j in range(y):
                        print(board[i][j], end = "")
                    print()
                print("-" * 72)

        elif ilkinput == str("left"):
            spacecraft_y_old = spacecraft_y
            spacecraft_y = spacecraft_y - 1 if spacecraft_y != 0 else spacecraft_y
            board[spacecraft_x][spacecraft_y_old] = ' '
            board[spacecraft_x][spacecraft_y] = '@'
            if time % 5 == 0:
                if ("*" in board[spacecraft_x-1]):
                    print("GAME OVER")
                    for i in range(x+g++1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
                    laststars = sum(x.count("*") for x in board)
                    score = x*y- laststars
                    print("YOUR SCORE:",score)
                    break
                    exit(0)
                else:
                    del board[spacecraft_x-1]
                    for i in range(1):
                        board.insert(0,list())
                        for j in range(y):
                            board[i].append(" ")
                    for i in range(x+g+1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
            else:
                for i in range(x+g+1):
                    for j in range(y):
                        print(board[i][j], end = "")
                    print()
                print("-" * 72)

        elif ilkinput == str("fire"):
            if("*" in board[spacecraft_x-1]):
                if board[spacecraft_x-1][spacecraft_y] == "*":
                    count += 1
                    if count == x*y:
                        board[spacecraft_x-1][spacecraft_y] = " "
                        print("YOU WON!")
                        for i in range(x+g+1):
                            for j in range(y):
                                print(board[i][j], end = "")
                            print()
                        print("-" * 72)
                        print("YOUR SCORE:", count)
                        break

                    else:
                        board[spacecraft_x-1][spacecraft_y] = " "
                        if ("*" in board[spacecraft_x-1]):
                            if time % 5 == 0:
                                print("GAME OVER")
                                for i in range(x+g+1):
                                    for j in range(y):
                                        print(board[i][j], end = "")
                                    print()
                                print("-" * 72)
                                laststars = sum(x.count("*") for x in board)
                                score = x*y- laststars
                                print("YOUR SCORE:",score)
                                break

                        for i in range(x+g+1):
                            for j in range(y):
                                print(board[i][j], end = "")
                            print()
                        print("-" * 72)


                else:
                    if time % 5 == 0:
                        laser_x =spacecraft_x-1
                        laser_y =spacecraft_y
                        board[laser_x][laser_y]= "|"
                        for i in range(x+g+1):
                            for j in range(y):
                                print(board[i][j], end = "")
                            print()
                        print("-" * 72)
                        for i in range(x+g-1):
                            laser_x_old = laser_x
                            laser_x -= 1
                            if board[laser_x][laser_y] == "*":
                                count += 1
                                board[laser_x][laser_y] = " "
                                board[laser_x+1][laser_y] = " "
                                if count == x*y:
                                    print("YOU WON!")
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    print("YOUR SCORE:", count)
                                    break

                                else:
                                    print("GAME OVER")
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    laststars = sum(x.count("*") for x in board)
                                    score = x*y- laststars
                                    print("YOUR SCORE:",score)
                                    break
                            else:
                                if laser_x == 0:
                                    board[laser_x][laser_y]= "|"
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    board[laser_x][laser_y] = " "
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g++1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                else:
                                    board[laser_x][laser_y] = "|"
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                        break
                    else:
                        laser_x =spacecraft_x-1
                        laser_y =spacecraft_y
                        board[laser_x][laser_y]= "|"
                        for i in range(x+g+1):
                            for j in range(y):
                                print(board[i][j], end = "")
                            print()
                        print("-" * 72)
                        for i in range(x+g-1):
                            laser_x_old = laser_x
                            laser_x -= 1
                            if board[laser_x][laser_y] == "*":
                                count += 1
                                board[laser_x][laser_y] = " "
                                board[laser_x+1][laser_y] = " "
                                if count == x*y:
                                    print("YOU WON!")
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    print("YOUR SCORE:", count)
                                    break

                                else:
                                    if time % 5 == 0:
                                        for i in range(1):
                                            board.insert(0,list())
                                            for j in range(y):
                                                board[i].append(" ")
                                        del board[spacecraft_x]
                                    else:
                                        pass

                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    break
                            else:
                                if laser_x == 0:
                                    board[laser_x][laser_y]= "|"
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
                                    if time % 5 == 0:
                                        for i in range(1):
                                            board.insert(0,list())
                                            for j in range(y):
                                                board[i].append(" ")
                                        del board[spacecraft_x]
                                    else:
                                        pass
                                    board[laser_x][laser_y] = " "
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g++1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)

                                else:
                                    if time % 5 == 0:
                                        for i in range(1):
                                            board.insert(0,list())
                                            for j in range(y):
                                                board[i].append(" ")
                                        del board[spacecraft_x]
                                    else:
                                        pass
                                    board[laser_x][laser_y] = "|"
                                    board[laser_x_old][laser_y] = " "
                                    for i in range(x+g+1):
                                        for j in range(y):
                                            print(board[i][j], end = "")
                                        print()
                                    print("-" * 72)
            else:
                laser_x =spacecraft_x-1
                laser_y =spacecraft_y
                board[laser_x][laser_y]= "|"
                for i in range(x+g+1):
                    for j in range(y):
                        print(board[i][j], end = "")
                    print()
                print("-" * 72)
                for i in range(x+g-1):
                    laser_x_old = laser_x
                    laser_x -= 1
                    if board[laser_x][laser_y] == "*":
                        count += 1
                        board[laser_x][laser_y] = " "
                        board[laser_x+1][laser_y] = " "
                        if count == x*y:
                            print("YOU WON!")
                            for i in range(x+g+1):
                                for j in range(y):
                                    print(board[i][j], end = "")
                                print()
                            print("-" * 72)
                            print("YOUR SCORE:", count)
                            break

                        else:
                            if time % 5 == 0:
                                for i in range(1):
                                    board.insert(0,list())
                                    for j in range(y):
                                        board[i].append(" ")
                                del board[spacecraft_x]
                            else:
                                pass

                            for i in range(x+g+1):
                                for j in range(y):
                                    print(board[i][j], end = "")
                                print()
                            print("-" * 72)
                            break
                    else:
                        if laser_x == 0:
                            board[laser_x][laser_y]= "|"
                            board[laser_x_old][laser_y] = " "
                            for i in range(x+g+1):
                                for j in range(y):
                                    print(board[i][j], end = "")
                                print()
                            print("-" * 72)
                            board[laser_x][laser_y] = " "
                            board[laser_x_old][laser_y] = " "
                            for i in range(x+g++1):
                                for j in range(y):
                                    print(board[i][j], end = "")
                                print()
                            print("-" * 72)
                        else:
                            board[laser_x][laser_y] = "|"
                            board[laser_x_old][laser_y] = " "
                            for i in range(x+g+1):
                                for j in range(y):
                                    print(board[i][j], end = "")
                                print()
                            print("-" * 72)


        elif ilkinput == str("exit"):
            for i in range(x+g++1):
                for j in range(y):
                    print(board[i][j], end = "")
                print()
            print("-" * 72)
            laststars = sum(x.count("*") for x in board)
            score = x*y- laststars
            print("YOUR SCORE:",score)
            break

        else:
            if time % 5 == 0:
                if ("*" in board[spacecraft_x-1]):
                    print("GAME OVER")
                    for i in range(x+g++1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
                    laststars = sum(x.count("*") for x in board)
                    score = x*y- laststars
                    print("YOUR SCORE:",score)
                    break

                else:
                    for i in range(1):
                        board.insert(0,list())
                        for j in range(y):
                            board[i].append(" ")
                    del board[spacecraft_x]
                    for i in range(x+g+1):
                        for j in range(y):
                            print(board[i][j], end = "")
                        print()
                    print("-" * 72)
            else:
                for i in range(x+g+1):
                    for j in range(y):
                        print(board[i][j], end = "")
                    print()
                print("-" * 72)




        if count == x*y:
            break
        else:
            ilkinput = input("Choose your action!\n").lower()






# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


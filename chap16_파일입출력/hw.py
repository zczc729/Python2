with open("proverb.txt", "r") as file:
    while True:
        fList = file.readlines()

        if not fList:
            break
        else :
            print(fList)
            
            for str in fList:
                a_count = 0         
                print(str ,end="")

                for j in str :
                    if j in "aA" :
                        a_count += 1
                print(f"a(A)의 개수 : {a_count}\n")
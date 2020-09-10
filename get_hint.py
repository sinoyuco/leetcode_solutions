 def getHint(self, secret: str, guess: str) -> str:
    letters = {}
    bullcount, cowcount = 0,0
    for i in range(len(guess)):
        
        if guess[i] in letters:
            letters[guess[i]].append(i)
        else:
            letters[guess[i]] = [i]
        
        if secret[i] == guess[i]:
            bullcount+=1
    
    for j in letters.keys():
        cowcount += min(len(letters[j]), secret.count(j))
                

    return f'{bullcount}A{cowcount-bullcount}B'
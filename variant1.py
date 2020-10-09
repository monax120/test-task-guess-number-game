
numberOfTries = 0

def numberGuess(startRange, endRange):
    """Generates random number from given range

    Args:
        startRange (int): Starting number of the range
        endRange (int): End point of the range
    """
    if startRange > endRange:
        return True
     
    midRange = (startRange + endRange)//2
   
    global numberOfTries
    
    print('Is your number ', midRange,'?', end=' ')
    user = input().lower()
    
    if user == 'y':
        print("Yey, I've guessed your number in ", numberOfTries," tries, not bad at all!")
        
    elif user == 'n':
        
        print('Is your number Greater than ', midRange, ' ?', end=' ')
        
        user = input().lower()
        print(user)
        if user == 'y':
            numberOfTries = numberOfTries + 1
            return numberGuess(midRange+1, endRange)
        elif user == 'n':
            numberOfTries = numberOfTries + 1
            return numberGuess(startRange, midRange-1)
        else:
            print('Please answer only "Y" or "N"')
            return numberGuess(startRange, endRange)
            
    else: 
        print('Please answer only "Y" or "N"')
        return numberGuess(startRange, endRange)
        
if __name__ == '__main__':
    print('Number guessing game, Guess a number in range (1 to 100)')
    startRange = 1
    endRange = 100
    
    out = numberGuess(startRange, endRange)
    
    if out:
        print('Bad choices')
            
            
        
    
    
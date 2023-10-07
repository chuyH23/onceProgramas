def convertInputString():
    rawInput = input("\ningresa una palabra para poder saber si se puede leer alrevez y sea lo mismo: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "siempre si es palindrome!" 
    else: 
        return "siempre no lo es palindrome." 

def main(): 
    print("\nchecador") 
    originalList = convertInputString()  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main() 
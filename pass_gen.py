import random
#2#1.7 each length taken and password generation begins
def generatePassword(pwlength):
#2.1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
#2.2 list to store indiividual passwords in list
    passwords = [] 
#2.3 password legth takenand used here 
    for i in pwlength:
        #2.4 empty string initialised
        password = "" 
        #2.5 "i" will basically carry length so it is taken below as range
        for j in range(i):
            #2.6 getting rand number from a to z with len
            next_letter_index = random.randrange(len(alphabet))
            #2.7 using the number to get a alphabet and append to the string
            password = password + alphabet[next_letter_index]
        #2.8 string will be sent to convert a alphabet to string
        password = replaceWithNumber(password)
        #2.9 string sent to covert a letter to upper case
        password = replaceWithUppercaseLetter(password)
        password = replaceWithSymbol(password)
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword

def replaceWithSymbol(pword):
    symbol=["~","`","!","@","#","$","%","^","&","*","(",'"',")","_","-","+","=","{","[","}","]","|",":",";","'","<",">",".","?","/"]
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + symbol[random.randrange(len(symbol))] + pword[replace_index+1:]
        return pword 
#code starts here with input
#1
def main():
    #1.1
    numPasswords = int(input("How many passwords do you want to generate? "))
    #1.2
    print("Generating " +str(numPasswords)+" passwords")
    #1.3
    passwordLengths = []
#1.4
    print("Minimum length of password should be 3")
#1.5 gets input from #1.1
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        #inner loop for verification
        if length<3:
            length = 3
        #1.6 after each input verification length int added to the list in #1.3
        passwordLengths.append(length)
    
    #1.6 after loops the password generation function looped with each length in the list
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])



main()

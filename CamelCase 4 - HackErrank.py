import re

def camelCase(string):
    if(string[0] == 'C'):
        #Primer Caso
        if(string[2] == 'M'):
            
            array = string[4::].split()
            newArray = array[1::]

            stringSolo = ' '.join(array[0:1])
            
            newString = ' '.join(newArray)
            newString = newString.title()
            newString = stringSolo + ''.join(newString.split()) + "()"

            return print(newString)


        #Segundo Caso
        elif(string[2] == 'C'):
            array = string[4::].split()
            
            newString = ' '.join(array)
            newString = newString.title()
            newString = ''.join(newString.split())
            
            return print(newString)

    
        #Tercer Caso
        elif(string[2] == 'V'):
            array = string[4::].split()
            newArray = array[1::]

            stringSolo = ' '.join(array[0:1])
            
            newString = ' '.join(newArray)
            newString = newString.title()
            newString = stringSolo + ''.join(newString.split())

            return print(newString)

    elif(string[0] == 'S'):
        #Primer Caso
        if(string[2] == 'M'):
            
            newStringTwo = ''
            newString = string[4::]
            splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', newString)).split()

            newString = ' '.join(splitted)
            newString = newString[:-2:]

            return print(newString.lower())


        #Segundo Caso
        elif(string[2] == 'C'):
            
            newStringTwo = ''
            newString = string[4::]
            splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', newString)).split()

            newString = ' '.join(splitted)

            return print(newString.lower())

    
        #Tercer Caso
        elif(string[2] == 'V'):
            
            newStringTwo = ''
            newString = string[4::]
            splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', newString)).split()

            newString = ' '.join(splitted)

            return print(newString.lower())
        
            
camelCase('S;V;iPad')
camelCase('C;M;mouse pad')
camelCase('C;C;code swarm')
camelCase('S;C;OrangeHighlighter')
print()
print()
print()
camelCase('C;V;can of coke')
camelCase('S;M;sweatTea()')
camelCase('S;V;epsonPrinter')
camelCase('C;M;santa claus')
camelCase('C;C;mirror')





from functions import*

#startup
printspeak("Initializing Techno...")
print("")
print("")
greetMe()
time.sleep(1)
printspeak('Hello ' + Master)
#todolist() #list the things i need to do to improve Techno
printspeak('')
printspeak('I am your digital assistant Techno.')

loop = True
while loop == True:
    query = myCommand()
    printspeak(f"You said: {query}")
    losantsend(query, Master)
    if 'quit' in query or 'exit' in query:
        loop = False

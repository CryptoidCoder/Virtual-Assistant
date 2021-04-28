from functions import losantsend


query = input("What's the query: ")
sender = input("Who's the sender: ")
destination = input("Where's the destination: ")


print(losantsend(query.lower(), sender.lower(), destination.lower()))

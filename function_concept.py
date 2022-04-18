# Why we use function in programming??

# If you are not using Funtion
print("Hello Lithium3")
print("Premium services is 30 days away")

print("Hello clock123")
print("Premium services is 15 days away")

print("Hello Smith.")
print("Premium services is 7 days away")

print("======================================")

# If we use function...
def printMsg(name, date):
    print("Hello. ", name , "Client")
    print("Premium services is ", date, "days away.")
    
printMsg("Lithium3", 30)
printMsg("clock123", 15)
printMsg("Smith", 7)
# 1. Good code reusabilty
printMsg("pinkpaper", 111)
# 2. convenient maintenance
print("change printMsg part little.")
# 3. better readability
print("more arrangement than when we don't use function")

import pywhatkit as py
print("1.Youtube")
print("2.Search from web")
print("3.Get info about")
print()
select = int(input("Enter selection number: "))

if select==1:
    string  = input("What do you want to play on youtube: ? ")
    py.playonyt("Shape Of You Song")
elif select==2:
    string  = input("What do you want to search about: ?")
    py.search(string)
elif select==3:
    string  = input("What do you want info about: ? ")
    py.info("Python means")
else:
    print("No valid command given")
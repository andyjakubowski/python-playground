try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("I’m going to need you to give me a number.")
except KeyboardInterrupt:
    print("\nWhoa! You interrupted me?!")
else:
    print("Nice, thanks!")
finally:
    print("Alright, this is the end.")

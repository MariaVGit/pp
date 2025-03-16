def countdown(wishes = True):
    print("Trzy")
    print("Dwa")
    print("Jeden")
    if not wishes:
        return
    print("Szczęśliwego nowego roku!")
countdown(wishes=False)
countdown()
countdown(0)
countdown(None)


working_dividers = []

while True:
    inp_number = int(input("Input your number : "))

    divider = 1

    while divider <= inp_number:
        if inp_number % divider == 0:
            working_dividers.append(divider)
        divider += 1

    if len(working_dividers) == 2:
        print(f"{inp_number} est premier ! Voici ses viseurs : {working_dividers}")
    else:
        print(f"{inp_number} n'est pas premier ! Voici ses viseurs : {working_dividers}")
        
    working_dividers = []

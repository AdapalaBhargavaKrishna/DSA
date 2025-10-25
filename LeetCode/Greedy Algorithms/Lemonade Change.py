def lemonadeChange(bills):
    fives = tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))      # True
print(lemonadeChange([5,5,10,10,20]))     # False
print(lemonadeChange([5,5,5,5,10,5,10,10,10,20]))  # False
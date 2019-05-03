base = int(input('Type in the base number : '))
power = int(input('Type in the power number : '))

def powerFunc(base, power):
    if power == 0:
        return 1
    else:
        if power == 1:
            return base
        else:
            result = base
            for i in range(1, power):
                result *= base
                i += 1
            return result
            
print(powerFunc(base, power))
        
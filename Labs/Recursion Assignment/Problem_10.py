def lcm(x, y, counter=1):
    return counter if (counter%x == 0 and counter%y == 0) else lcm(x, y, counter+1)
print(lcm(int(input()), int(input())))
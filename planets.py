def weight_on_planets():
    age = input('What do you weigh on earth? ')
    age = int(age)   
    
    marsweight = age * 0.38
    jupiterweight = age * 2.34
    
    printstring = '\nOn Mars you would weigh ' + str(marsweight) + ' pounds.\nOn Jupiter you would weigh ' + str(jupiterweight) + ' pounds.'
    
    print(printstring)
    
if __name__ == '__main__':
   weight_on_planets()

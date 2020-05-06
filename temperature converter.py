train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

print('To convert temperature, use the following: f_to_c(x) for fahrenheit to celsius, and c_to_f(y) for celsius to fahrenheit. X and y are the numbers to convert.')

def f_to_c(x):
  tempC=((x-32)*5/9)
  return tempC
def c_to_f(y):
    tempF=(y*(9/5)+32)
    return tempF
f100_in_celsius=f_to_c(100)
c0_in_fahrenheit=c_to_f(0)
#maybe additional features, someday
#def get_force(mass,acceleration):
#    mass*acceleration
#    return(mass*acceleration)
#train_force=get_force(22680,10)
#def get_energy(mass,c=3*10**8):
#    return mass*c**2
#bomb_energy=get_energy(1)
#def get_work(mass,acceleration,distance):
#    result=get_force(mass,acceleration)*distance
#    return result
#train_work=get_work(22680,10,100)

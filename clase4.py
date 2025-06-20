mix = ["uno", 2 , 3.14, [1,2,3]]
print(mix)
print(type(mix))
print(mix[0:2])
mix.append(False)
print(mix)
mix.insert(1,[True])
print(mix)
print(mix.index(3.14))
number = [1,800,300,50,87,99,90]
print("numero mayor es: ",max(number))
print("numero menor es: ",min(number))
del number[-1]
print(number)
del number[:2]
print(number)
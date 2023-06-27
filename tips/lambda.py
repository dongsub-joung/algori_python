pluse= lambda x: x+10

a= pluse(1);
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b= list(map(lambda x: str(x) if x%3 == 0 else x, a))
print(b)
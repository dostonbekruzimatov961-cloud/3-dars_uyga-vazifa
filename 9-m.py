names = {
"Eshmat" ,
"Toshmat" ,
"Ali",
"Eshmat" ,
"Vali",
"Ali"
}
names_set = set(names)

count = 0
for ism in names_set:
    if names.count(ism) == 1:
        count +=1
        print(ism)

print(count)
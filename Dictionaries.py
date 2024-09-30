#dictionary
D={
    'name': 'jesse',
    'sqare_root_of_2': 1.41421356237309504880148872420985,
}
print(D)
print(D.keys())
print(D.values())

for i in D.keys():
    print(i,D[i])

D['gender']= 'male'
print(D)
del(D["gender"])
print(D)

D["name"]= "guy_who_is_interested_in_the_theory_of _general_relativity"
print(D)
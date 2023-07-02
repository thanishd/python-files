#single key single values
a={"shiva":"id001","ram":"id002","abdul":"id003"}
a.update({"varun":"id004"})
a["thani"]="id005"
print(a)
print(a["abdul"])
print(a.keys())
print(a.values())


#single key multipe values
b={"abi":["11th",22,"chennai"],
   "jebin":["12th",23,"madurai"],
   "rahul":["10th",19,"nagercoil"]}
print(b)
print(b["rahul"])

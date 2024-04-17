#for,while,dict,a=[];-массив,str

a={
    "car":"Toyoth",
    "model":"camry",
    "image":["https://www.toyotakz.com/?ysclid=lv0noozwl771248892"]
}


b={
    "car":"Toyoth",
    "model":"camry",
    "images":["https://www.toyotakz.com/?ysclid=lv0noozwl771248892,http://www.motorpage.ru/Toyota/photos.html?ysclid=lv0o41h0sq153109485"],
    "price":25000000,
    "is_published":True
}

c={"name":"Erbol","surname":"Askarov"}
b=c["name"]
b=c.get("name")
b=None
c["middle_name"]="Erzhanuly"
print(c)
#
#person_data=dict
#person_data["name"]="Askar"
#last_name="Erlanov"
#person_data["last_name"]=last_name


d={"name":"Askar","last_name":"Erlanov"}
for k,v in d.items():
    print("key",k)
    print("value",v)


list_1=[ {
    "name":"Kanat",
    "last_name":"Erbolov",
    "age":20
},
{
   "name":"Askar",
    "last_name":"Erzhanov",
    "age":15
},
{
    "name":"Kairat",
    "last_name":"Zhandosov",
    "age":45
}
]

list_1 = [
    {"name": "Kanat", "last_name": "Erbolov", "age": 20},
    {"name": "Askar", "last_name": "Erzhanov", "age": 15},
    {"name": "Kairat", "last_name": "Zhandosov", "age": 45}
]

total_age = 0
for person in list_1:
    total_age += person["age"]
    
count = len(list_1)


average_age = total_age / count

print("Average age:", average_age)
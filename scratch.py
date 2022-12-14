from pprint import pprint

names = ["miguel","jose","altagracia","peter"]
persons =[{"name":"miguel", "location":"New York"},
          {"name":"jose", "location": "Dominican Republic"}]

device = {
    "name": "Mikrotik",
    "vendor":"Mikrotik.com",
    "os": "RouterOS",
    "version": "7.6",
    'ip':"19.168.1.45"
}
# for name in names:
#     print(name)
pprint(persons)

for person in persons:
    print(f'this person is {person["name"]}')    

print("\n____ For loop, using F string ------")
print("16s justify to rigth 16 carateres")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
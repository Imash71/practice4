import json
with open("../sample-data.json", "r") as file:
   data = json.load(file)
print("Read JSON:")
print(data)
new_student = {"name": "Dias", "age": 19, "city": "Shymkent"}
json_string = json.dumps(new_student, indent=4)
print("\nConverted to JSON string:")
print(json_string)
with open("new-data.json", "w") as file:
   json.dump(new_student, file, indent=4)
print("\nNew JSON file created.")

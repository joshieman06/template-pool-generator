
import os
import json

directory = r'STRUCTURE FILE DIRECTORY'
dir = "STRUCTURE NAMESPACE LOCATION"
startjson = {
  "fallback": "minecraft:empty",
  "elements": []
}

json_object = json.loads(json.dumps(startjson, indent=2))

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if filename.split('.')[1] != "nbt":
            break
        json_new = {
        "weight": 1,
        "element": {
        "element_type": "minecraft:single_pool_element",
        "projection": "rigid",
        "location": dir + "/" + filename.split('.')[0],
        "processors": "minecraft:empty"
      }
    }
        json_object["elements"].append(json_new)

print(json_object)

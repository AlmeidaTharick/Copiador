import sys
import clipboard
import json

saved_data = "clipboard.json"

def save_data(filepath, data):
  with open(filepath, "w") as f:
    json.dump(data, f)

def load_data(filepath):
  try:
    with open(filepath, "r"):
      data = json.load(f)
  except:
    return {}


'''data = clipboard.paste() #pega o que ta no Ctrl + V
clipboard.copy("abc") # é o Ctrl + C
print(data)'''

if len(sys.argv) == 2:
  command = sys.argv[1]
  data = load_data(saved_data)

  if command == "Save":
    key = input("Enter a key: ")
    data [key] = clipboard.paste()
    save_data(saved_data, data)
    print("Data saved")
    print("Save")
  elif command == "Load":
    key = input("Enter a key: ")
    if key in data:
      clipboard.copy(data[key])
      print("Data copied to clipboard!")
    else:
      print("Key does not exist.")
    print("Load")
  elif command == "List":
    print(data)
  else: 
    print("Unknown command")
else:
  print("Please pass exactly one command.")
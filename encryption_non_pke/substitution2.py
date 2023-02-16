def decrypt(message):
  key = { #This is a dictionary that holds the substitution key
    "E": "A",
    "A": "B",
    "G": "C",
    "S": "D",
    "F": "E",
    "U": "F",
    "B": "G",
    "I": "H",
    "H": "I",
    "D": "J",
    "T": "K",
    "J": "L",
    "X": "M",
    "W": "N",
    "Y": "O",
    "V": "P",
    "N": "Q",
    "O": "R",
    "R": "S",
    "K": "T",
    "Z": "U",
    "L": "V",
    "P": "W",
    "C": "X",
    "Q": "Y",
    "M": "Z"
  }
  listKeys = key.keys() #makes a list of the key elements in the dictionary
  message = message.upper() #converts the message into all caps
  result = "" #sets a place holder where we can store the final string
  
  for char in message: #loops through the original message and checks each letter
    if char not in listKeys: #if the letter is not in the list of keys then it is a symbol (or space or number) and needs to be added
      result += char
    else: #Add the associated value to the result and return
      result += key[char]
  return result
    
  
  
test1 = decrypt("IFJJY IYP EOF CYZ?")

print(test1)
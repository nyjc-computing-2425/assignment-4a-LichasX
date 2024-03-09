nric = input('Enter an NRIC number: ').upper()
output = "invalid"
lst = ["S", "T", "F", "G"]
weight = "2765432"
total = 0
for x, y in enumerate(weight):
  if not nric[x+1].isalpha():
    total += int(nric[x+1]) * int(y)
if nric[0] == "T" or nric[0] == "G":
  total += 4
total = total % 11
dict_st = {0:"J", 1:"Z", 2:"I", 3:"H", 4:"G", 5:"F", 6:"E", 7:"D", 8:"C", 9:"B", 10:"A"}
dict_fg = {0:"X", 1:"W", 2:"U", 3:"T", 4:"R", 5:"Q", 6:"P", 7:"N", 8:"M", 9:"L", 10:"K"}
if nric[0] in lst and len(nric[1:-1]) == 7 and nric[1:-1].isdigit() and nric[-1].isalpha():
  if nric[0] == "T" or nric[0] == "S":
    if nric[-1] == dict_st[total]:
      output = "valid"
  elif nric[0] == "F" or nric[0] == "G":
    if nric[-1] == dict_fg[total]:
      output = "valid"
print(f"NRIC is {output}.")

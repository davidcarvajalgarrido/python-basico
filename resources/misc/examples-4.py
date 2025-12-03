
def find_number(number_list):
  """
  Dada una lista de números, devuelve la posición de la primera aparición del número 42 en dicha lista. Si no está, devuelve -1
  """
  found_number = False
  i = 0
  
  while i < len(number_list) and not found_number:
    if number_list[i] == 42:
      found_number = True
    
    i += 1
  
  if found_number:
    return i-1
  else:
    return -1 

def find_number_alt(number_list):
  """
  Dada una lista de números, devuelve la posición de la primera aparición del número 42 en dicha lista. Si no está, devuelve -1
  """
  i = 0
  
  while i < len(number_list):
    if number_list[i] == 42:
      break

    i += 1

  if i < len(number_list):
    return i

  return -1

def find_number_alt_multiple(number_list, target):
  """
  Dada una lista de números, devuelve otra lista con las posiciones de las apariciones del número target en lista de entrada. Si no está, devuelve -1
  """
  output_list = []

  for index, elem in enumerate(number_list):
    if elem == target:
      output_list.append(index)

  return output_list

print(find_number_alt_multiple([12, 34, 42, 78, 42, 90], 42))

def unique_elements(data):

  seen = set()  
  unique_data = []
  for item in data:
    if item not in seen:
      seen.add(item)
      unique_data.append(item)
  return unique_data

n=[x for x in map(int,input().split())]
print(unique_elements(n))
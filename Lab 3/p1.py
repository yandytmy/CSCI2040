#python_version == '3.7'

def non_unique(list):
  result = []
  for x in list:
    if x not in result:
      if list.count(x) > 1:
        result.append(x)
        result.append(list.count(x))
  return result # ‘result’ is a list.
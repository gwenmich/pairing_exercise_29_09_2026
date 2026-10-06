def group_chat(names_list):
  names_string = ""
  length = len(names_list)
  if length <= 2:
    return " & ".join(names_list)
  elif length > 2:
    for name in names_list:
      names_string += name
      if names_list.index(name) == length -2:
        names_string += " & "
      else:
        names_string += ", "
    return names_string[:-2]
  return names_string
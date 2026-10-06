from lib.group_chat import *

def test_when_list_is_empty():
  result = group_chat([])
  assert result == ""

def test_when_one_item():
  result = group_chat(["Bart"])
  assert result == "Bart"
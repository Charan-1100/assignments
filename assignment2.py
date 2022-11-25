data_list=[545,5646,566,56161,161,651561,6161,651]
operation=input(("Select the operation to be performed : "))
if operation == "1":
  print("smallest number from the list is ",min(data_list))
elif operation == "2":
  print("largest number from the list is ", max(data_list))
elif operation == "3":
  def remove_elements():
    i=0
  for x in data_list:
    if x %2==0:
      pass
    else:
      data_list.remove(x)
  print(data_list)
elif operation == "4":
  for y in data_list:
    if y %2 !=0:
      print("odd numbers  : ",y)
    else:
      print("even numbers : ",y)
else:
  print("invalid")

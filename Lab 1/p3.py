CGPA = 0
HonGPA = 0
CcurCred = 0
CtotCred = 0
HoncurCred = 0
HontotCred = 0

input_string = input()
input_list = input_string.split()
while input_list[0] != '-1' :
  if float(input_list[0]) <= 5.0 and float(input_list[0]) >= 0.0 :
    if int(input_list[2]) == 1:
      HontotCred += float(input_list[1])
      HonGPA = HonGPA*HoncurCred/HontotCred+float(input_list[0])*float(input_list[1])/HontotCred
      HoncurCred = HontotCred
    CtotCred += float(input_list[1])
    CGPA = CGPA*CcurCred/CtotCred+float(input_list[0])*float(input_list[1])/CtotCred
    CcurCred = CtotCred
    print("Current GPA:  {0:.2f}".format(CGPA))
    print("Current major GPA:  {0:.2f}".format(HonGPA))
  else : print('Wrong input!')
  input_string = input()
  input_list = input_string.split() 
print('Program ends.')
dict_=dict(input('enter the input'))
i=input('enter')
for key,values in dict_.items():
    if key[2].lower()== i  :
        print(f"the value of '{key}' is'{value}")
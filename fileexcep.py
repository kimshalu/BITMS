file_path=('sh.txt')
try:
    with open(file_path,'r') as file:
        content=file.read()
        print(content)
        
except FileNotFoundError:
    print("file not found")
    
except Exception as e:
    print(f'an error occured:{e}')
finally:
    print('closing the file')

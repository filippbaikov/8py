from choice_file import choice_number_file


def copyInfoInFiles():
   n= choice_number_file()
   def secondfile(n):
       if n==1:
         return 2
       else:
          return 1
   def append_or_rewrite():
     number = int(input("если хочешь дописать в файл нажми 1\n если перезаписать нажми 2: "))
     while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
     if number==1:
         with open (f'db/data_{secondfile(n)}.txt','a',encoding='utf-8') as file_set_info:
          data1 = file_set_info.writelines( f"{''.join(data)}")   
     elif number==2 :    
        with open (f'db/data_{secondfile(n)}.txt','w',encoding='utf-8') as file_set_info:
         data1 = file_set_info.write( f"{''.join(data)}")  
           
   with open (f'db/data_{n}.txt','r', encoding='utf-8') as file_get_info:
       data = file_get_info.readlines()
   append_or_rewrite()
   print('ну на, получи!!! доволен?! чё еще тебе надо?')     
"""print("и так это должно вывестись на экран текстом") # игнор?
user_name = "Nasar"
print (user_name)
user_name = "alex"
print (user_name)
print ("now the user is:")
print(user_name)
favorite_language = "python"
print (favorite_language)
release_year = "1991"
print(release_year)
print(favorite_language, release_year)
release_year = "2024"
print(release_year)
product_name = "iphone 15"
pruduct_count = 2
pruduct_price = 999.99
is_in_stock = True
print(product_name,pruduct_count,pruduct_price,is_in_stock)
print( type(product_name) )
print( type(pruduct_count) )
print( type(pruduct_price) )
print( type(is_in_stock) )
a = 10
b = 3
sum_result  = a + b
print(sum_result) #суммирование
diff_result = a - b
print(diff_result)#вычитание
prod_result = a * b
print(prod_result)#умножение
div_result = a/b
print(div_result)#деление
div_result=a/b
print(div_result)#
floor_div_result=a//b
print(floor_div_result)#цилочисленное деление
reminder_result=a%b
print(reminder_result)#остаток от деления
power_result=a**b
print(power_result)#возведение в степень
first_name = "Кокос"
last_name = "Арбузович"
full_name = first_name + last_name
print(full_name)
divider="щ"*20
print(divider)
user_age=23
age_info_correct="возраст: " + str(user_age)
print(age_info_correct)
user_name="Хышы"
user_age=25
city="Шяньхай"
user_info=f"пользователь: {user_name}, возраст: {user_age}, город: {city}."
print(user_info)
item_price=120
item_count=3
total_info=f"сумма заказа: {item_price * item_count}"
print(total_info)
print("--- Ohayo kuzaimas ---") """

#практическое задание
""" first_number=input("введите первое число ")
sec_number=input("введите второе число ")
first_number=int(first_number)
sec_number=int(sec_number)
sum_result=first_number+sec_number
diff_result=first_number-sec_number
prod_result=first_number*sec_number
div_result=first_number/sec_number
print(f"Значение суммы: {sum_result}, Разница: {diff_result}, их произведение: {prod_result}, их частное:{div_result}") """
 
"""user_age=int(input("сколько тебе лет?"))
if user_age>=18:
    print("залетай богатырь.")
else:
    print("иди подрасти мелочь пузатая, рановато тебе сюда входить")
live_temperature=int(input("сколько сейчас на улице градусов?"))
if live_temperature>20:
    print("жарковато, советую надеть майку")
elif live_temperature>5:
    print("ну вообще прохладно, советую утеплиться")
else:
    print("не светую вообще выходить на улицу но если приспичило, надевай шубу или пуховик") """

"""user_age=23
has_permission=True
if user_age >= 18 and has_permission == True:
    print("доставай валыну, тебе уже можно")
else:
    print("катись отсюда")
number=int(input("введи число:"))
if number%2==0:
    print("число четное.")
else:
    print("число нечетное.")"""

"""correct_pass="qwerty123"
user_pass=(input("введите пароль "))
if user_pass==correct_pass:
    print("доступ разрешен")
else:
    print("доступ запрещен")"""

user_numb=int(input("введите целое число "))
if user_numb > 0:
    print("число положительное")
    if user_numb%2==0:
        print("число четное")
    else: 
        print("число нечетное")
elif user_numb < 0:
    print("число отрицательное")
else:
    print("число равно нулю")

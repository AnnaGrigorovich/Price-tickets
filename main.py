print ("Введите количество необходимых билетов:")
price = 0
num_tikets = int(input())
for i in range (num_tikets):
    i += 1
    age_for_ticket = input(f'Возраст участника билета №{i}? ')
    age_for_ticket = int(age_for_ticket)
    if age_for_ticket < 18:
        print("Билет бесплатный")
    elif age_for_ticket >= 18 and age_for_ticket < 25:
        price += 990
        print('Стоимость билета: 990 руб.')
    else:
        price += 1390
        print('Стоимость билета: 1390 руб.')
if num_tikets > 3:
    price = price - ((price / 100) * 10)
    print(f'Сумма к оплате {price} руб. с учетом скидки за регистрацию более трех человек')
else:
    print(f'Сумма к оплате {price} руб.')
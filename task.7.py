#задачи 7.1
month = 15
spring_month = [3, 4, 5]
autmn_month = [6, 7, 8]
summer_month = [9, 10,11]
winter_month = [12, 1 ,2]
if month in spring_month:
    print("весна")
elif month  in autmn_month:
    print("осень")
elif month in summer_month:
    print("лето")
elif month in winter_month:
    print("зима")
else:
    print("некорректный номер месяца")

#задачи 7.2
#Логика_оформления_заказа
is_logged_in = True
has_items_in_cart = True
has_shipping_address = True
has_order = False
if is_logged_in and has_items_in_cart and has_shipping_address:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен")
    has_order = True
else:
    print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")
total_purchase  = 1001
min_purchase = 1000
is_first_order = True
if has_order and (is_first_order or total_purchase > min_purchase):
    print("Вы получаете скидку!")

# задачи 7.3
# number = 16
# if number = [7, 13, 21]
# print("счастливое число")



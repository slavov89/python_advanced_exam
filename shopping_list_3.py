def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    shop_list = {}
    for item in kwargs:
        shop_list[item] = kwargs[item]
    basket_items = 0
    to_print = []
    for key, value in shop_list.items():
        if (budget - (float(value[0])*int(value[1]))) > 0 and basket_items < 5:
            total = (float(value[0]) * int(value[1]))
            basket_items +=1
            budget -= total
            to_print.append(f"You bought {key} for {total:.2f} leva.")

    return "\n".join(to_print)


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
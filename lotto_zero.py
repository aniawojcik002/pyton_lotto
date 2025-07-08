from random import randint

my_numbers = {1, 16, 49, 44, 2, 6}

def generate_lotto():
    lotto_number = { randint(1,49), randint(1,49), randint(1,49), randint(1,49), randint(1,49), randint(1,49) }
    while len(lotto_number) != 6:
        lotto_number = generate_lotto()
    return lotto_number


def count_lotto():
    lotto_numbers = generate_lotto()

    price_lotto = 3
    total_lotto = 0
    counter_lotto = 0
    while my_numbers != lotto_numbers:
        total_lotto += price_lotto
        counter_lotto += 1
        lotto_numbers = generate_lotto()


    print (f"Trzeba wydać {total_lotto} zł")
    # 3 razy w tygodniu, 4 razy w miesiącu, 12 miesiecy
    years = counter_lotto / 12 / 12
    print (f"{years:.0f} - tyle lat trzeba grać")

count_lotto()

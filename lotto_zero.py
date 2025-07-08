from random import sample

MY_NUMBERS = {1, 16, 49, 44, 2, 6}
PRICE_LOTTO = 3

def generate_lotto():
    lotto_number = set(sample(range(1,50), k=6))
    return lotto_number

def count_lotto():
    lotto_numbers = generate_lotto()

    counter_lotto = 1
    while MY_NUMBERS != lotto_numbers:
        counter_lotto += 1
        lotto_numbers = generate_lotto()


    print (f"Trzeba wydać {counter_lotto * PRICE_LOTTO} zł")
    # 3 razy w tygodniu, 4 razy w miesiącu, 12 miesiecy
    print (f"{counter_lotto/144:.0f} - tyle lat trzeba grać")

count_lotto()

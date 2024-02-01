import re


def run():
    print("\n","Tast_01","\n")
    text = "Our phone number + 38 (067) 125 67 92 and we are open from 9:00 to 18:00."
    text_list = re.split("[,: ().]", text)

    num_list = []
    for text in text_list:
        if text.isnumeric():
            num_list.append(int(text))
    print()

    sum_numbers = 0
    sum_even_numbers = 0
    sum_odd_numbers = 0
    sum_numbers_multiples_three = 0

    for num in num_list:
        sum_numbers = sum_numbers + num

        match num % 2:
            case 0:
                sum_even_numbers = sum_even_numbers + num
            case _:
                sum_odd_numbers = sum_odd_numbers + num
                if num % 3 == 0:
                    sum_numbers_multiples_three = sum_numbers_multiples_three + num

    enter = "\n\n"
    print(f"sum of all numbers : {sum_numbers}{enter}"
          f"sum of all even numbers :  {sum_even_numbers}{enter}"
          f"sum of all odd numbers : {sum_odd_numbers}{enter}"
          f"the sum of all numbers dividable by three : {sum_numbers_multiples_three}{enter}")

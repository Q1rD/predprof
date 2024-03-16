import csv


def main() -> None:
    """
    основная функция программы
    :return: None
    """
    with open("magical.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))
        for i in reader[1:]:
            row = f"{i[0]} в запасах еще есть - {i[1]}\n"
            print(row)
            with open('magicaPotions.txt', 'a') as output:
                output.write(row)



main()

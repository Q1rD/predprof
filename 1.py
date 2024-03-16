import csv


def main() -> None:
    with open("magical.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))
        for i in reader[1:]:
            if i[1] == -1:
                i[1] = 0
            row = f"{i[0]} в запасах еще есть - {i[1]}\n"
            with open('magicaPotions.txt', 'a') as output:
                output.write(row)



main()

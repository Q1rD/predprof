import csv


def main(name):
    """
    основная функция программы
    :param name: str
    :return: None
    """
    result = ['name', 0]
    with open("magical.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))[1:]
        for i in reader:
            if name == i[4]:
                if int(i[1]) > result[1]:
                    result[0] = i[0]
                    result[1] = int(i[1])
    if result[0] == 'name':
        print('Такую траву мы не используем')
    else:
        print(f"По вашему запросу {name} найден следующий вариант: {name} используется в {result[0]}, его количество составляет : {result[1]}")


name = ''
while True:
    name = input('Введите название травы: ')
    if name == 'стоп':
        break
    main(name)

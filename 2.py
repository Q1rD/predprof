import csv


def bubble_sort(collection):
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


def main():
    nums = {}
    with open("magical.csv") as input_file:
        reader = list(csv.reader(input_file, delimiter=","))[1:]
        for i in reader:
            nums[int(i[1])] = i[0]
        print(nums)
        sorted_nums = bubble_sort([i for i in nums])
        for i in sorted_nums:
            print(f"Зелья {nums[i]} осталось {i}")


main()
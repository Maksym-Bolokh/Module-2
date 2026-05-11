arr = [2, 5, 7, 9, 11, 10, 15, 18, 20, 22, 25, 30]

print("Масив 12 елементів:")
for x in arr:
    print(x, end=" ")

print()


k = int(input("Введіть номер елемента масиву: "))


if k < 1 or k > len(arr):
    print("Неправильний номер елемента")
else:
    new_arr = arr[:k]

    print(f"Масив {len(new_arr)} елементів:")

    for x in new_arr:
        print(x, end=" ")

    print()

    
    is_sorted = True

    for i in range(len(new_arr) - 1):
        if new_arr[i] > new_arr[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print("Впорядковано за зростанням")
    else:
        print("НЕ впорядковано за зростанням")
        
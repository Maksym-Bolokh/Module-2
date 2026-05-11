import os

surname = os.getenv("SURNAME")

if surname:
    print("Значення змінної SURNAME:", surname)
else:
    print("Змінна SURNAME відсутня")
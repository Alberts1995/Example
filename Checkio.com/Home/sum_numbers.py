def sum_numbers(text: str) -> int:
    b = 0
    for i in text.split():
        if i.isdigit():
            b += int(i)
    print(b)
            
sum_numbers('2 asd2as 2')


def count_digits(text: str) -> int:
    b = 0
    for x in text:
        if x.isdigit():
            b +=1
    print(b)


count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')

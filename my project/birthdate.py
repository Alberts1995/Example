import re

while True:
    spefic_date = input('Впиши сегоднешнее число (такого формата: день.месяц.год): ')
    birth_date = input('Впиши дату рождения (такого формата: день.месяц.год): ')

    if re.search(r'\d{1,2}/\d{1,2}/\d{4}', spefic_date) is None or re.search(r'\d{1,2}/\d{1,2}/\d{4}', birth_date) is None:
      
        spefic_date = spefic_date.split('.')
        birth_date = birth_date.split('.')

    spefic_year, spefic_month, spefic_day = int(spefic_date[2]), int(spefic_date[1]), int(spefic_date[0])
    birth_year, birth_month, birth_day = int(birth_date[2]), int(birth_date[1]), int(birth_date[0])
      
    if spefic_day < birth_day:
        spefic_day += 30
        spefic_month -= 1
    if spefic_month < birth_month:
        spefic_month += 12
        spefic_year -= 1
         
    year = str(spefic_year - birth_year) + ' лет, '
    month = str(spefic_month - birth_month) + ' месяцов, '
    day = str(spefic_day - birth_day) + ' дней. '
      
    if spefic_year - birth_year < 2:
        year = year.replace('лет', 'год')
    if spefic_month - birth_month < 2:
        month = month.replace('месяцов', 'месяц')
    if spefic_day - birth_day < 2:
        day = day.replace('дней', 'день')
    print('Тебе: ' + year + month + day)
       
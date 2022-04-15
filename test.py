from datetime import datetime, date, time

def get_date(date):
    day_list = ['1', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20',
        '21', '22', '23',
        '24', '25', '26',
        '27', '28', '29',
        '30', '31']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' +
        month_list[int(date_list[1]) - 1] + ' ' +
        date_list[2] + ' года')
date = datetime.now()
print(get_date(date))

from datetime import datetime


def get_days_date_difference(date_a: str, date_b: str, date_format: str = "%d/%m/%Y") -> int:
    datetime_a = datetime.strptime(date_a, date_format)
    datetime_b = datetime.strptime(date_b, date_format)
    delta_time_days = (datetime_b - datetime_a).days
    return abs(delta_time_days)


a = "01/01/2023"
b = "01/01/2024"
days_difference = get_days_date_difference(a, b)
print(days_difference)

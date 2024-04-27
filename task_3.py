from datetime import datetime


def get_date_difference_days(date_a: str, date_b: str, date_format: str = "%d/%m/%Y") -> int:
    datetime_a = datetime.strptime(date_a, date_format)
    datetime_b = datetime.strptime(date_b, date_format)
    delta_time_days = (datetime_b - datetime_a).days
    return delta_time_days


a = "01/01/2024"
b = "01/01/2023"
date_difference_days = get_date_difference_days(a, b)
print(f"The difference between the dates {b} and {a} is {abs(date_difference_days)} days.")

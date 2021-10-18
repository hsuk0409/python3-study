from datetime import datetime


def convert_date_str_to_datetime(date_str):
    datetime_str = datetime.strptime(date_str, "%Y%m%d%H%M%S")

    return datetime_str.strftime("%Y-%m-%d %H:%M:%S")


date_param_str = "20211018000000"
converted_datetime = convert_date_str_to_datetime(date_param_str)
print(converted_datetime)

from datetime import datetime


def convert_date_to_formatted_string(date) -> str:
    try:
        date_time = datetime.strptime(date, '%Y%m%d')

        return str(date_time.date())
    except Exception as ex:
        print(f"datatime strptime error!!, message= {ex}")

        return ""

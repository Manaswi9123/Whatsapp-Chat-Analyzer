import re
import pandas as pd
def preprocess(data):
    pattern = r"^\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s"

    msgs = re.split(pattern, data, flags=re.MULTILINE)[1:]

    date = re.findall(pattern, data, flags=re.M)
    clean_dates = [d.replace('\u202f', ' ') for d in date]
    df = pd.DataFrame({'user_message': msgs, 'message_date': clean_dates})
    df['message_date'] = df['message_date'].str.replace(' - ', '', regex=False).str.strip()
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('^([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []

    for hour in df['date'].dt.hour:
        start_suffix = "AM" if hour < 12 else "PM"
        start_h = hour % 12
        if start_h == 0: start_h = 12
        next_hour_24 = (hour + 1) % 24
        end_suffix = "AM" if next_hour_24 < 12 else "PM"
        end_h = next_hour_24 % 12
        if end_h == 0: end_h = 12
        period.append(f"{start_h} {start_suffix}-{end_h} {end_suffix}")

    df['period'] = period

    return df
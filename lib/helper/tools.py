import re
from datetime import timedelta, datetime


class Tools:
    def __init__(self):
        pass

    def getValueDias(self, text):
        dias_m = re.search(r'(\d+)\s*dias', text)
        dias = int(dias_m.group(1)) if dias_m else None
        return dias

    def getValueDates(self, text):
        date_m = re.search(r'(\d{2}/\d{2}/\d{4})', text)
        date = date_m.group(1) if date_m else None
        if date:
            fetchall = datetime.strptime(date, '%d/%m/%Y')
            return fetchall
        return None

    def restarValues(self, dias, fecha):
        new_date = fecha - timedelta(days=dias)
        return new_date

    def searchEmoji(self, text):
        emoji_pattern = re.compile(r'[^\w\s,]')
        emoji = emoji_pattern.search(text)
        return emoji.group(0) if emoji else None

    def countEmoji(self, text, ToLoking):
        count = text.count(ToLoking)
        return count

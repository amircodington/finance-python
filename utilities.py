
from datetime import timedelta

def past_days(date, days):
    return date - timedelta(days=days)
    
from datetime import datetime, timedelta


def time_filter(obj):
    if obj.get('month'):
        return datetime.now() - timedelta(weeks=4)
    elif obj.get('week'):
        return datetime.now() - timedelta(weeks=1)
    elif obj.get('day'):
        return datetime.now() - timedelta(days=1)

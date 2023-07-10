from datetime import datetime, timedelta


def time_filter(obj):
    time_filters = ['day', 'month', 'week']

    if obj.get('month') in time_filters:
        return datetime.now() - timedelta(weeks=4)
    elif obj.get('week') in time_filters:
        return datetime.now() - timedelta(weeks=1)
    elif obj.get('day') in time_filters:
        return datetime.now() - timedelta(days=1)

    return False

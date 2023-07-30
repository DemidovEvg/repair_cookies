from core.models import Price


def get_repair_price(category: str, repair_level: int):
    return Price.objects.filter(category=category, repair_lvl=repair_level).first()

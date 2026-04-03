def validate_positive_amount(value: float) -> float:
    if value <= 0:
        raise ValueError("amount must be positive")
    return value



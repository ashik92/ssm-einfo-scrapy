import argparse
import re


def validate_date(value):
    if value and not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        raise argparse.ArgumentTypeError(f"{value} not in yyyy-mm-dd format")
    return value


def validate_natural_num(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError(f"{value} must be a natural number")
    return value

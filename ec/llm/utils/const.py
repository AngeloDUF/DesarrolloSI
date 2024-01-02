import re

TEMPERATURE = 0.2
MAX_TOKENS = 30

def CLEAN_TEXT(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)


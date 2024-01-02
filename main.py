from dotenv import load_dotenv
import os
from ec.llm.service.InferenceService import InferenceService
from ec.llm.utils.const import CLEAN_TEXT
from ec.llm.utils.const import decimal_to_binary, binary_to_decimal


def load_environment_variables():
    load_dotenv('secrets/.env')
    print(os.getenv('OPENAI_API_KEY'))


if __name__ == '__main__':
    load_environment_variables()
    # custom_dict = {'a': 'b'}
    # print(custom_dict['c'])
    # print(custom_dict.get('c', 'kepler'))

    binary_value = '1101'
    decimal_value = binary_to_decimal(binary_value)
    print(f'{binary_value} en decimal es: {decimal_value}')

    decimal_value = 13
    binary_value = decimal_to_binary(decimal_value)
    print(f'{decimal_value} en binario es: {binary_value}')

    print(InferenceService().invoke('2017'))


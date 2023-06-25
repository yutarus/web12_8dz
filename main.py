import re
from typing import Union, List
from src.models import Quotes

import redis
from redis_lru import RedisLRU


client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


@cache
def parser(string: str) -> Union[str, List[str]]:
    """
     Parses the input string and returns either a string or a list of strings.
    :param string:  Input string to parse.
    :return: Either a string or a list of strings.
    """
    if ',' in string:
        string = string.strip().replace(' ', '').split(',')
    return string


@cache
def find_match(param: Union[str, List[str]]) -> List[str]:
    """
    Finds quotes that match the specified parameter.
    :param param: The parameter to match against.
    :return: A list of quotes that match the parameter.
    """
    quotes = Quotes.objects()
    result = ["List of quotes: "]
    if isinstance(param, list):
        for el in param:
            for quote in quotes:
                tags = quote.tags
                matches = re.match(el, str(quote.author.fullname), re.IGNORECASE) \
                          or re.match(el, str(quote.quote), re.IGNORECASE)
                if any(re.match(el, tag, re.IGNORECASE) for tag in tags):
                    result.append(quote.quote)
                if matches:
                    result.append(matches)
    else:
        for quote in quotes:
            tags = quote.tags
            matches = re.match(param, str(quote.author.fullname), re.IGNORECASE) \
                      or re.match(param, str(quote.quote), re.IGNORECASE)
            if any(re.match(param, tag, re.IGNORECASE) for tag in tags):
                result.append(quote.quote)
            if matches:
                result.append(quote.quote)
    return result


if __name__ == '__main__':

    while True:
        arg = input('-->').strip().split(':')
        command = arg[0]
        try:
            arg = parser(arg[1].strip())
            match = find_match(arg)
            for m in match:
                print(m)
        except IndexError:
            pass
        if command == 'exit':
            break


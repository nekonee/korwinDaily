import random
import quotes


def get_daily(fst, secnd, trd):
    return (random.choice(fst) + random.choice(secnd) + random.choice(trd))


print(get_daily(quotes.first, quotes.second, quotes.third))



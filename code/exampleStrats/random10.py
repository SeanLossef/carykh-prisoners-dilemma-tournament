import random

def strategy(history, memory):
    if random.random() < 0.10:
        return 0, None
    return 1, None
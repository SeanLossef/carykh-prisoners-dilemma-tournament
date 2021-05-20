import random

def strategy(history, memory):
    if history.shape[1] == 0:
        return 1, None
    if random.random() < 0.90:
        return history[1,-1], None
    return (history[1,-1] + 1) % 2, None
import random
from main import *


def announce_counter():
        Counter = random.randrange(1, 10)
        counters = []

        if Counter not in counters:
            print("Please proceed to counter number:", Counter)
        else:
            counters.append[Counter]

def report_stats():
    print("Total tokens printed today:", total_tokens)
    print("Expected waiting time is:", waiting_time, "minutes")
    print("There are:", queue_length, "people in the queue")
    print("Time needed to clean up the queue is:", time_needed, "minutes")

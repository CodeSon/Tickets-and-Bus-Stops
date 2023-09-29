import random
import pandas as pd

#Function for generating random bus ids


def generate_bus_ids(num_ids):
    bus_ids = [random.randint(300, 415) for _ in range(num_ids)]
    df = pd.DataFrame(bus_ids, columns=['BUS ID'])
    return df

#busses = generate_bus_ids(30)
#print(busses)
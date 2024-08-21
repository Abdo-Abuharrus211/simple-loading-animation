from random import random, randint

from tqdm import tqdm, trange
from time import sleep

progress_descriptions = ["Initializing system...",
                         "Loading modules...",
                         "Connecting to server...",
                         "Fetching data...",
                         "Loading User Profile...",
                         "Loading User Group policies...",
                         "Setting User config...",
                         "Applying Security measures", "Booting up..."]

for txt in progress_descriptions:
    bar = trange(10, desc=f'Processing task: {txt}', leave=True)
    for i in bar:
        sleep(randint(0, 4) / 10)
    tqdm.write(f'Completed: {txt}\r', end='')

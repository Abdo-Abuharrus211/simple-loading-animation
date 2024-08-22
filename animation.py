import os
import subprocess
import time
from random import randint
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress, track
from time import sleep

MY_THEME = Theme({'cyber_process': 'bold #fdf800', 'ready': 'bold underline green'})
console = Console(theme=MY_THEME)
progress_descriptions = ["Initializing system...",
                         "Loading modules...",
                         "Connecting to server...",
                         "Fetching data...",
                         "Loading User Profile...",
                         "Loading User Group policies...",
                         "Setting User config...",
                         "Applying Security measures", "Booting up..."]


def begin():
    console.print(f'Start boot cycle :rocket:')
    for i in track(range(7), description='Processing: ', style='white'):
        console.print(f'\n{progress_descriptions[i]}', style='cyber_process')
        sleep(randint(4, 9) / 10)
    console.print(f'Ready to launch!', style='ready')


def launch_slideshow(file_path):
    if os.path.exists(file_path):
        if os.name == 'nt':
            os.startfile(file_path)
        print(f"Opening {file_path}")
    else:
        print(f"File not found: {file_path}")


if __name__ == '__main__':
    begin()
    launch_slideshow('D:\Documents\My projects\Marp proj\phsa-co-op-presentation\exports\Goodbye pres.pdf')

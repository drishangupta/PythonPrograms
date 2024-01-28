# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:17:20 2023

@author: drish
"""

import psutil

def get_memory_info():

    virtual_memory = psutil.virtual_memory()

    swap_memory = psutil.swap_memory()

    total_memory = virtual_memory.total

    available_memory = virtual_memory.available

    used_memory = virtual_memory.used

    memory_percent = virtual_memory.percent

    total_swap = swap_memory.total

    used_swap = swap_memory.used

    swap_percent = swap_memory.percent

    return {

"Total Memory": total_memory,

"Available Memory": available_memory,

"Used Memory": used_memory,

"Memory Percent": memory_percent,

"Total Swap": total_swap,

"Used Swap": used_swap,

"Swap Percent": swap_percent

}

memory_info = get_memory_info()

print(memory_info)
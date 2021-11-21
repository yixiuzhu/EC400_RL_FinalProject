import sys
import subprocess

print(f'== Testing Coding Assignment 4 ==')
map_times = {
    'zengarden' : 50,
    'lighthouse' : 50,
    'hacienda' : 60,
    'snowtuxpeak' : 60,
    'cornfield_crossing' : 70,
    'scotland' : 70
}

cmd = "python -m controller " # change if error occurs (could have python as python3)

for key in map_times.keys():   
    res = subprocess.check_output(f"{cmd} {key}", universal_newlines=True)
    res_steps = int(res.split(' ')[0])
    if res_steps < map_times[key]:
        print(f"[+] {key} passed with {res_steps / 10}s")
    else:
        print(f"[-] {key} failed with {res_steps / 10}s")
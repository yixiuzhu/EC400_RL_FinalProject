import subprocess
import multiprocessing

map_times = {
    'zengarden' : 500,
    'lighthouse' : 500,
    'hacienda' : 600,
    'snowtuxpeak' : 600,
    'cornfield_crossing' : 700,
    'scotland' : 700
}

cmd_1 = "python3 controller_zengarden.py"
cmd_2 = "python3 controller_lighthouse.py"
cmd_3 = "python3 controller_hacienda.py"
cmd_4 = "python3 controller_snowtuxpeak.py"
cmd_5 = "python3 controller_cornfield_crossing.py"
cmd_6 = "python3 controller_scotland.py"

def test_track(track: str):
    if track == 'zengarden':
        res = subprocess.check_output(f"{cmd_1} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

    if track == 'lighthouse':
        res = subprocess.check_output(f"{cmd_2} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

    if track == 'hacienda':
        res = subprocess.check_output(f"{cmd_3} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

    if track == 'snowtuxpeak':
        res = subprocess.check_output(f"{cmd_4} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

    if track == 'cornfield_crossing':
        res = subprocess.check_output(f"{cmd_5} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

    if track == 'scotland':
        res = subprocess.check_output(f"{cmd_6} {track}", universal_newlines=True)
        res_steps = int(res.split(' ')[0])
        if res_steps < map_times[track]:
            print(f"[+] {track} passed with {res_steps / 10}s")
        else:
            print(f"[-] {track} failed with {res_steps / 10}s")

if __name__ == '__main__':
    print(f'== Testing Coding Assignment 4 ==')
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    p.map(test_track, map_times.keys())

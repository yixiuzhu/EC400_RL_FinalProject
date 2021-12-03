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

cmd = "python planner.py" # change if error occurs (could have python as python3)

def test_track(track: str):
    res = subprocess.check_output(f"{cmd} {track}", universal_newlines=True)
    res_steps = int(res.split(' ')[0])
    if res_steps < map_times[track]:
        print(f"[+] {track} passed with {res_steps / 10}s")
    else:
        print(f"[-] {track} failed with {res_steps / 10}s")

if __name__ == '__main__':
    print(f'== Testing Coding Assignment 5 ==')
    p = multiprocessing.Pool(16)
    p.map(test_track, map_times.keys())
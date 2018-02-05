import os
import random
import subprocess

def get_files(root):
    files = []

    def scan_dir(dir):
        for f in os.listdir(dir):
            f = os.path.join(dir, f)
            if os.path.isdir(f):
                scan_dir(f)
            elif os.path.splitext(f)[1] == ".mp3":
                files.append(f)

    scan_dir(root)
    return files

# double-buffered playlists so there aren't any repeats
buffers = (get_files("music folder directory"), [])
playing = 0

while True:
    if len(buffers[playing]) > 0:
        f = random.choice(buffers[playing])
        buffers[playing].remove(f)
        buffers[not playing].append(f)
    else:
        playing = not playing
        continue
    p = subprocess.Popen(["mpg123", f])
    p.wait()


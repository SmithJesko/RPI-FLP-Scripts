import time

animation = "|/-\\"
idx = 0
while idx <= 15:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
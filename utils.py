
import csv
from datetime import datetime

def log_access(name, mask, emotion, access):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, time_now, mask, emotion, access])

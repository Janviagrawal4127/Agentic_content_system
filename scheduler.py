import schedule
import time

from agents.manager_agent import run_pipeline

schedule.every(1).minutes.do(run_pipeline)

print("Scheduler Running...")

while True:
    schedule.run_pending()
    time.sleep(60)
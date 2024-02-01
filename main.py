import task_01
import task_02
import task_03
import task_04

tasks = [
    task_01.run,
    task_02.run,
    task_03.run,
    task_04.run
]

for f in tasks:
    f()

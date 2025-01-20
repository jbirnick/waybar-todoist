from todoist_api_python.api import TodoistAPI
import subprocess

def api_token():
    return subprocess.run(['secret-tool','lookup','uuid','todoist_api_token'], capture_output=True, text=True).stdout

def countTasks(items):
    count = {1: 0, 2: 0, 3: 0, 4: 0}
    for item in items:
        count[item.priority] += 1
    return count

api = TodoistAPI(api_token())

try:
    tasks = api.get_tasks(filter="today | overdue | no due date")
    count = countTasks(tasks)
    #print('%{{B#de4c4a}} {0[4]} %{{B-}}%{{B#f49c18}} {0[3]} %{{B-}}%{{B#4073d6}} {0[2]} %{{B-}}%{{B#444444}} {0[1]} %{{B-}}'.format(count))
    print('{{"text": "<span background=\\"#de4c4a\\" line_height=\\"26624\\"> {0[4]} </span><span background=\\"#f49c18\\"> {0[3]} </span><span background=\\"#4073d6\\"> {0[2]} </span><span background=\\"#444444\\"> {0[1]} </span>", "class": "todoist"}}'.format(count), flush=True)
except:
    print(' ERROR ', flush=True)

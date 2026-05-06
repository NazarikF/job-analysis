import json

with open('../data/jobs.json') as f:
    data = json.load(f)
    for i, job in enumerate(data,1):
        print(f'{i}',job['title'],"\n", job['company'],'\n', job['description'])




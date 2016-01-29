import csv
import random
import json
from collections import OrderedDict

questions = list(csv.DictReader(open("questions.csv"), ('question', 'answer')))
nodes = list(csv.DictReader(open("nodes.csv"), ('node', 'x', 'y')))
remaining_questions = csv.DictWriter(open("remaining.csv", 'w'), ('question', 'answer'))

mapinfo = OrderedDict()
mapinfo['6-4B'] = {
        'end_node': 'L',
        'boss_node': 'L',
        'boss_question': 17,
        }
mapinfo['6-4C'] = {
        'end_node': 'S',
        'boss_node': 'P',
        'boss_question': 25,
        }

EMPTY_QUESTION = {'question': '', 'answer': ''}
randomized_questions = questions.copy()
for current_map in mapinfo:
    boss_question = mapinfo[current_map]['boss_question']-1
    randomized_questions[boss_question] = EMPTY_QUESTION
randomized_questions = [question for question in randomized_questions if question != EMPTY_QUESTION]
random.shuffle(randomized_questions)

maps = {}
for map_name, current_map in mapinfo.items():
    map_questions = {}
    for node in nodes:
        current_node = node.copy()
        del current_node['node']
        if node['node'] == current_map['boss_node']:
            current_node.update(questions[current_map['boss_question']-1])
        else:
            current_node.update(randomized_questions.pop())
        map_questions[node['node']] = current_node
        if node['node'] == current_map['end_node']:
            break
    maps[map_name] = map_questions

out_js = open("../js/questions.js", "w")
out_js.write("var map_order=")
json.dump([map_name for map_name in mapinfo], out_js)
out_js.write(";var questions=")
json.dump(maps, out_js)
out_js.write(";")
out_js.close()

for question in randomized_questions:
    remaining_questions.writerow(question)

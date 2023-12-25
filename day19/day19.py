
import copy

class Rule:
    def __init__(self):
        self.default = ""
        self.rules = []

    def parse_string(self, string):
        a = string.split("{")[1][:-1]
        b = a.split(",")
        self.default = b[-1]
        for p in b[:-1]:
            new = []
            new.append(p[0]) # key
            new.append(p[1]) # greater, less
            d = p[2:].split(":")
            new.append(int(d[0]))
            new.append(d[1])
            self.rules.append(new)
    
    def apply_rule(self, item):
        for rule in self.rules:
            key = rule[0]
            number = item[key]
            if rule[1] == "<":
                if number < rule[2]:
                    return rule[3]
            if rule[1] == ">":
                if number > rule[2]:
                    return rule[3]
        
        return self.default

def parse_key(string):
    split = string.split('{')
    return split[0]

def get_rule(rule):
    key = parse_key(rule)
    rule_object = Rule()
    rule_object.parse_string(rule)
    return key, rule_object

def get_item(item):
    item = item.strip('{}')
    pairs = item.split(',')
    result = {}
    for pair in pairs:
        key, value = pair.split('=')
        result[key.strip()] = int(value.strip())
    return result

def get_state(item, rules):
    state = rules["in"].apply_rule(item)
    while state not in ["A", "R"]:
        new_state = rules[state].apply_rule(item)
        state = copy.deepcopy(new_state)
    return state

def part1(rules, items):
    rejected = []
    accepted = []

    for item in items:
        state  = get_state(item, rules)
        if state == "A":
            accepted.append(copy.deepcopy(item))
        elif state == "R":
            rejected.append(copy.deepcopy(item))
        else:
            print("Error", state)

    # print(len(accepted), len(rejected))
    result = 0
    for item in accepted:
        for value in item.values():
            result += value

    return result

"""
1) dict of rules.
2) list of dicts as items.
"""

if __name__ == "__main__":
    with open("day19_input.txt", "r") as f:
        lines = f.readlines()
    rule_lines = []
    item_lines = []

    for line in lines:
        if line[0] == "{":
            item_lines.append(line[:-1])
        else:
            rule_lines.append(line[:-1])

    rule_dict = {}
    list_of_items = []

    for rule in rule_lines:
        key, rule_object = get_rule(rule)
        rule_dict[key] = rule_object

    for item in item_lines:
        item_dict = get_item(item)
        list_of_items.append(item_dict)
    
    solution_part1 = part1(rule_dict, list_of_items)
    print("Solution Part 1: ", solution_part1)
    

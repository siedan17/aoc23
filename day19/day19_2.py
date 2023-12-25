
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
            new.append(int(d[0])) # num
            new.append(d[1]) # next rule-key
            self.rules.append(new)

def split_interval(rule, interval):
    interval = copy.deepcopy(interval)
    result = []
    for r in rule.rules:
        i = interval[r[0]]
        if r[1] == "<":
            if i[0] < r[2] < i[1]:
                append_i = copy.deepcopy(interval)
                append_i[r[0]] = [i[0], r[2] - 1]
                result.append([r[3], append_i])
                interval[r[0]] = [r[2], i[1]]
                continue
            if i[1] < r[2]:
                result.append([r[3], copy.deepcopy(interval)])
                return result

        elif r[1] == ">":
            if i[0] < r[2] < i[1]:
                append_i = copy.deepcopy(interval)
                append_i[r[0]] = [r[2] + 1, i[1]]
                result.append([r[3], append_i])
                interval[r[0]] = [i[0], r[2]]
                continue
            if i[0] > r[2]:
                result.append([r[3], copy.deepcopy(interval)])
                return result
    
    if calc_num(interval) > 0:
        result.append([rule.default, copy.deepcopy(interval)])

    return result

def apply_rules(rules, interval, key):
    result = []
    rule = rules[key]
    new_intervals = split_interval(rule, interval) # these intervals have their rule-key attached to them.
    for new_interval in new_intervals:
        if new_interval[0] == "A":
            result.append(new_interval[1])
        elif new_interval[0] == "R":
            continue
        elif new_interval[0] not in ["A", "R"]: # recursive call.
            for r in apply_rules(rules, new_interval[1], new_interval[0]):
                result.append(r)
    
    return result

def calc_num(interval):
    x = interval["x"][1] - interval["x"][0]
    m = interval["m"][1] - interval["m"][0]
    a = interval["a"][1] - interval["a"][0]
    s = interval["s"][1] - interval["s"][0]
    if interval["x"][0] != 0:
        x += 1
    if interval["m"][0] != 0:
        m += 1
    if interval["a"][0] != 0:
        a += 1
    if interval["s"][0] != 0:
        s += 1
    return x * m * s * a

def part2(rules):
    accepted = apply_rules(rules, {"x": [0, 4000], "m": [0, 4000], "a": [0, 4000], "s": [0, 4000]}, "in")
    result = 0
    for interval in accepted:
        result += calc_num(interval)
    return result

def parse_key(string):
    split = string.split('{')
    return split[0]

def get_rule(rule):
    key = parse_key(rule)
    rule_object = Rule()
    rule_object.parse_string(rule)
    return key, rule_object

if __name__ == "__main__":
    with open("day19_input.txt", "r") as f:
        lines = f.readlines()

    rule_lines = []
    for line in lines:
        if line[0] != "{":
            rule_lines.append(line[:-1])

    rule_dict = {}
    for rule in rule_lines:
        key, rule_object = get_rule(rule)
        rule_dict[key] = rule_object
    
    solution_part2 = part2(rule_dict)
    print("Solution Part 2: ", solution_part2)
    

"""
aoc y2023 day 19
https://adventofcode.com/2023/day/19
"""
from operator import lt, gt
from copy import copy


def d19parse(data):
    """
    parse
    """
    workflows = {
        'A': True,
        'R': False
    }
    parts = []

    is_parts = False
    for line in data:
        if line == '':
            is_parts = True
            continue

        if not is_parts:
            workflow = []
            line_split = line.split('{')
            key = line_split[0]
            flow_split = line_split[1][:-1].split(',')

            default = None
            for flow in flow_split:
                flow_desc = flow.split(':')
                if len(flow_desc) == 1:
                    default = flow_desc[0]
                else:
                    split_flow_desc = []
                    func = None
                    if '<' in flow_desc[0]:
                        split_flow_desc = flow_desc[0].split('<')
                        func = lt
                    else:
                        split_flow_desc = flow_desc[0].split('>')
                        func = gt
                    value = split_flow_desc[0]
                    compare_to = int(split_flow_desc[1])
                    target = flow_desc[1]
                    workflow.append((value, func, compare_to, target))

            workflow.append(default)
            workflows[key] = workflow

        else:
            part = {}
            split_line = line[1:-1].split(',')
            for elem in split_line:
                split_elem = elem.split('=')
                part[split_elem[0]] = int(split_elem[1])
            parts.append(part)

    return parts, workflows


def execute(part, workflow):
    """

    """
    for flow in workflow:
        if type(flow) is tuple:
            key, func, compare_to, target = flow
            value = part[key]
            # print(f'    {key}: {value}{"<" if func == lower else ">"}{compare_to}: {target}')
            if func(value, compare_to):
                return target
        else:
            # print(f'    default: {flow}')
            return flow


def run_workflow(workflows, part):
    """

    """
    rest = ['in']

    while rest:
        flow, rest = rest[0], rest[1:]
        # print(f'  {flow}')
        workflow = workflows[flow]
        if type(workflow) is bool:
            return workflow
        else:
            rest.append(execute(part, workflow))

    raise Exception('End reached')


def d19p1(data):
    """
    part 1
    """
    parts, workflows = data
    result = 0
    for part in parts:
        # print(part)
        res = run_workflow(workflows, part)
        if res:
            for value in part.values():
                result += value

    return result


# d19p2 is still incorrect, need additional debug
def opposite(flow):
    """

    """
    value, func, compare_to, _ = flow
    if func == lt:
        return (value, gt, compare_to-1)
    else:
        return (value, lt, compare_to+1)


def explore_workflow(workflows, constraints, workflow_name, current_workflow):
    """

    """
    workflow = workflows[workflow_name]
    if type(workflow) is bool:
        if workflow:
            current_workflow = current_workflow[:-2]
            return [(current_workflow, constraints)]
        else:
            return [None]

    else:
        results = []
        rest_constraints = []
        for flow in workflow[:-1]:
            flow_constraints = copy(constraints)
            value, func, compare_to, target = flow

            current_workflow_copy = f'{current_workflow}{workflow_name}=>{target}, '

            flow_tuple = (value, func, compare_to)

            flow_constraints.append(flow_tuple)
            rest_constraints.append(opposite(flow))

            results.extend(explore_workflow(workflows, flow_constraints, target, current_workflow_copy))

        target = workflow[-1]
        current_workflow = f'{current_workflow}{workflow_name}=>{target}, '
        flow_constraints = copy(constraints)
        flow_constraints = flow_constraints + rest_constraints

        results.extend(explore_workflow(workflows, flow_constraints, target, current_workflow))

        return results


def d19p2(data):
    """
    part 2
    """
    parts, workflows = data
    constraint_list = explore_workflow(workflows, [], 'in', '')
    constraint_list = [r for r in constraint_list if r is not None]

    treated = {}
    result = 0
    for constraints in constraint_list:
        flow, constraint = constraints

        xmas = {
            'x': (1, 4000),
            'm': (1, 4000),
            'a': (1, 4000),
            's': (1, 4000)
        }
        for c in constraint:
            value, func, compare_to = c
            if func == lt:
                compare_to = compare_to - 1
                xmas[value] = (min(xmas[value][0], compare_to), min(xmas[value][1], compare_to))
            else:
                xmas[value] = (max(xmas[value][0], compare_to), max(xmas[value][1], compare_to))

        if flow not in treated:
            treated[flow] = xmas
        else:
            for key in xmas.keys():
                min_old, max_old = treated[flow][key]
                min_new, max_new = xmas[key]
                treated[flow][key] = (max(min_old, min_new), (min(max_old, max_new)))

    for key, xmas in treated.items():
        possibilities = 1
        for value in xmas.values():
            possibilities = possibilities * (value[1] - value[0] + 1)

        result += possibilities

    return result

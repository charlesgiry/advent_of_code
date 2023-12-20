"""
aoc 2023 day 19
https://adventofcode.com/2023/day/19
"""
from copy import copy
from pprint import pprint

# seems I could have used https://docs.python.org/3/library/operator.html as well for next 2 methods
def lower(value, compared_to):
    """

    """
    return value < compared_to


def bigger(value, compared_to):
    """

    """
    return value > compared_to


workflows = {
    'A': True,
    'R': False
}
parts = []
with open('data/day19_data.txt', 'r') as file:
    lines = file.read().splitlines()

is_parts = False
for line in lines:
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
                    func = lower
                else:
                    split_flow_desc = flow_desc[0].split('>')
                    func = bigger
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


def run_workflow(part):
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


def d19p1():
    """
    The Elves of Gear Island are thankful for your help and send you on your way. They even have a hang glider that someone stole from Desert Island; since you're already going that direction, it would help them a lot if you would use it to get down there and return it to them.
    As you reach the bottom of the relentless avalanche of machine parts, you discover that they're already forming a formidable heap. Don't worry, though - a group of Elves is already here organizing the parts, and they have a system.
    To start, each part is rated in each of four categories:

        x: Extremely cool looking
        m: Musical (it makes a noise when you hit it)
        a: Aerodynamic
        s: Shiny

    Then, each part is sent through a series of workflows that will ultimately accept or reject the part. Each workflow has a name and contains a list of rules; each rule specifies a condition and where to send the part if the condition is true. The first rule that matches the part being considered is applied immediately, and the part moves on to the destination described by the rule. (The last rule in each workflow has no condition and always applies if reached.)
    Consider the workflow ex{x>10:one,m<20:two,a>30:R,A}. This workflow is named ex and contains four rules. If workflow ex were considering a specific part, it would perform the following steps in order:

        Rule "x>10:one": If the part's x is more than 10, send the part to the workflow named one.
        Rule "m<20:two": Otherwise, if the part's m is less than 20, send the part to the workflow named two.
        Rule "a>30:R": Otherwise, if the part's a is more than 30, the part is immediately rejected (R).
        Rule "A": Otherwise, because no other rules matched the part, the part is immediately accepted (A).

    If a part is sent to another workflow, it immediately switches to the start of that workflow instead and never returns. If a part is accepted (sent to A) or rejected (sent to R), the part immediately stops any further processing.
    The system works, but it's not keeping up with the torrent of weird metal shapes. The Elves ask if you can help sort a few parts and give you the list of workflows and some part ratings (your puzzle input). For example:

    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}

    The workflows are listed first, followed by a blank line, then the ratings of the parts the Elves would like you to sort. All parts begin in the workflow named in. In this example, the five listed parts go through the following workflows:

        {x=787,m=2655,a=1222,s=2876}: in -> qqz -> qs -> lnx -> A
        {x=1679,m=44,a=2067,s=496}: in -> px -> rfg -> gd -> R
        {x=2036,m=264,a=79,s=2244}: in -> qqz -> hdj -> pv -> A
        {x=2461,m=1339,a=466,s=291}: in -> px -> qkq -> crn -> R
        {x=2127,m=1623,a=2188,s=1013}: in -> px -> rfg -> A

    Ultimately, three parts are accepted. Adding up the x, m, a, and s rating for each of the accepted parts gives 7540 for the part with x=787, 4623 for the part with x=2036, and 6951 for the part with x=2127. Adding all of the ratings for all of the accepted parts gives the sum total of 19114.
    Sort through all of the parts you've been given; what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?
    """
    result = 0
    for part in parts:
        # print(part)
        res = run_workflow(part)
        if res:
            for value in part.values():
                result += value

    return result


# d19p2 is still incorrect, need additional debug
def opposite(flow):
    """

    """
    value, func, compare_to, _ = flow

    if func == lower:
        return (value, bigger, compare_to-1)
    else:
        return (value, lower, compare_to+1)


def explore_workflow(constraints, workflow_name, current_workflow):
    """

    """
    # current_workflow = f'{current_workflow}{workflow_name}, '

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

            results.extend(explore_workflow(flow_constraints, target, current_workflow_copy))

        target = workflow[-1]
        current_workflow = f'{current_workflow}{workflow_name}=>{target}, '
        flow_constraints = copy(constraints)
        flow_constraints = flow_constraints + rest_constraints

        results.extend(explore_workflow(flow_constraints, target, current_workflow))

        return results

def d19p2():
    """

    """
    constraint_list = explore_workflow([], 'in', '')
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
            if func == lower:
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

import re

def solution(args):
    all_range = sorted(list(range(args[0], args[-1] + 1)))
    args_str = ' '.join(str(rng) for rng in all_range)
    missing = set(args) ^ set(all_range)

    for val in missing:
        args_str = args_str.replace(f' {val} ', ' | ')

    formatted = re.sub(r'\|+', '|', args_str.replace(' | ', '|')).split('|')
    return ','.join(f'{val.split()[0]}-{val.split()[-1]}' if len(val.split()) > 2 else ','.join(val.split()) for val in formatted)
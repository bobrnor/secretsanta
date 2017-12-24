
import sys
import random


def choose_da_victim(i):
    work_set = filter(lambda x: x not in [i - 1, i, i + 1], leftover_set)
    if len(work_set) > 0:
        victim = work_set[random.randint(0, len(work_set) - 1)]
        leftover_set.remove(victim)
        return victim
    else:
        return None

if len(sys.argv) == 2:
    number_of_victims = int(sys.argv[1])

    origin_set = [i for i in range(number_of_victims)]
    result_set = []
    done = False

    while not done:
        leftover_set = list(origin_set)
        result_set = [choose_da_victim(i) for i in range(number_of_victims)]
        done = None not in result_set

    assert len(result_set) == len(set(result_set))
    assert len(filter(lambda x: x == result_set[x], result_set)) == 0

    print "\n".join([str(i + 1) for i in result_set])

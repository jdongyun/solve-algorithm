# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(n, stages):
    stages_count = [0] * (n+2)
    for i in range(len(stages)):
        stages_count[stages[i]] += 1
    stages_list = []
    users_count = len(stages)
    for i in range(n+2):
        divided = 0
        if users_count > 0:
            divided = stages_count[i] / users_count
        stages_list.append((i, divided))
        users_count -= stages_count[i]
    stages_list = sorted(stages_list, key=lambda x: x[1], reverse=True)
    ret = []
    for stage in stages_list:
        if 0 < stage[0] <= n:
            ret.append(stage[0])
    return ret

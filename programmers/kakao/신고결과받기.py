from collections import defaultdict
def solution(id_list, report, k):
    answer = {i:0 for i in id_list}
    report = set(report)
    reported_list = defaultdict(list)
    reported_time = defaultdict(int)

    for item in report:
        reporter, target = item.split()
        reported_list[reporter].append(target)
        reported_time[target]+=1

    mail_to_target = []
    for key,value in reported_time.items():
        if value >=k:
            mail_to_target.append(key)

    for key, value in reported_list.items():
        target = set(value).intersection(mail_to_target)
        if target:
            answer[key] = len(target)

    return list(answer.values())
def func501(num):
    return bin(num)[2:]

def func502(num):
    return bin(int(num, 16))[2:]

def func503(ch):
    if ch.islower():
        return ch.upper()
    elif ch.isupper():
        return ch.lower()
    else:
        return ch

def func504(s):
    count_0 = s.count('0')
    sum_digits = sum(int(c) for c in s)
    return [count_0, sum_digits]

def func505(n):
    count = 0
    # 先扣除每种商品至少买一个的花费：15+3+2=20，剩余金额为n-20
    remaining = n - 20
    if remaining < 0:
        return 0
    # 球拍、球、水的数量分别为 r, b, w（r≥0, b≥0, w≥0），满足 15r + 3b + 2w = remaining
    for r in range(remaining // 15 + 1):
        remaining_r = remaining - 15 * r
        for b in range(remaining_r // 3 + 1):
            remaining_b = remaining_r - 3 * b
            if remaining_b % 2 == 0:
                count += 1
    return count

def func506(list):
    excellent = 0
    passed = 0
    failed = 0
    for score in list:
        if score >= 90:
            excellent += 1
        elif 60 <= score <= 89:
            passed += 1
        else:
            failed += 1
    return [excellent, passed, failed]

def func507(list):
    max_age_person = list[0]
    for person in list:
        if person['age'] > max_age_person['age']:
            max_age_person = person
    return max_age_person

def func508(n):
    remaining = n
    count = 0

    # 阶段1：1~10次，每次2元
    stage1_max = 10
    stage1_cost = 2 * stage1_max
    if remaining >= stage1_cost:
        count += stage1_max
        remaining -= stage1_cost
    else:
        count += remaining // 2
        return count

    # 阶段2：11~20次，每次1.9元
    stage2_max = 10
    stage2_cost = 1.9 * stage2_max
    if remaining >= stage2_cost:
        count += stage2_max
        remaining -= stage2_cost
    else:
        count += remaining // 1.9
        return int(count)

    # 阶段3：21~50次，每次1.6元
    stage3_max = 30
    stage3_cost = 1.6 * stage3_max
    if remaining >= stage3_cost:
        count += stage3_max
        remaining -= stage3_cost
    else:
        count += remaining // 1.6
        return int(count)

    # 阶段4：51次以上，每次1元
    count += remaining // 1
    return int(count)

def func509(n, dis):
    # 计算各站点间的累积距离
    cumulative_dis = [0] * 30
    for i in range(1, 30):
        cumulative_dis[i] = cumulative_dis[i - 1] + dis[i - 1]

    max_stations = 0
    # 遍历所有可能的起始和结束站点组合
    for start in range(30):
        for end in range(start + 1, 30):
            distance = cumulative_dis[end] - cumulative_dis[start]
            # 计算票价
            if distance <= 5:
                cost = 2
            else:
                cost = 2 + ((distance - 5 + 4) // 5)  # 不满5km按1元计算，向上取整
            if cost <= n and (end - start) > max_stations:
                max_stations = end - start
    return max_stations

def func510(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def func511(n, h):
    distance = h
    current_height = h
    for i in range(1, n):
        current_height /= 2
        distance += 2 * current_height
    rebound_height = current_height / 2
    return [distance, rebound_height]

def func512(n):
    digit1 = n // 1000
    digit2 = (n // 100) % 10
    digit3 = (n // 10) % 10
    digit4 = n % 10
    sum_pow = digit1 ** 4 + digit2 ** 4 + digit3 ** 4 + digit4 ** 4
    return sum_pow == n

def func513(n):
    def is_semiprime(num):
        factor_count = 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factor_count += 1
                if i != num // i:#进一步判断非平方根因数
                    factor_count += 1
            if factor_count > 2:
                return False
        return factor_count == 2

    total = 0
    for num in range(10, n + 1):
        if is_semiprime(num):
            total += num
    return total

def func514(lst):
    total = 0
    prev_center_score = 0  # 记录上一次中心跳跃的得分，初始为0表示无连续中心跳跃
    for action in lst:
        if action == 0:
            break
        elif action == 1:
            total += 1
            prev_center_score = 0  # 非中心跳跃，重置连续中心标记
        elif action == 2:
            if prev_center_score == 0:
                # 第一次中心跳跃或上一次是1分
                current_score = 2
            else:
                current_score = prev_center_score + 2
            total += current_score
            prev_center_score = current_score
    return total

def func515(m, step, n):
    current_pos = m
    for i in range(1, n + 1):
        current_pos -= step
        if current_pos < 0:
            return False
        elif current_pos == 0:
            return i
        else:
            current_pos += step*0.5
    return False


if __name__ == "__main__":
    pass
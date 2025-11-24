import math

def func201(a, b):
    integer_result = a // b
    float_result = a / b
    s1 = f"{integer_result:>4d}"
    s2 = f"{float_result:>8.2f}"
    return s1 + s2

def func202(a, b, c, d):
    m=max(a,b,c,d)
    return m


def func203(a, b):
    shang=a//b
    yu=a%b
    s1="{:>4d}".format(shang)
    s2="{:>4d}".format(yu)
    return s1 + s2


def func204(name):
    c=len(name)
    return c


def func205(a, b, c):
    nums = [a,b,c]
    nums.sort()
    return nums


def func206(distance_to_moon_km):
        t="{:>8.2f}".format(2*distance_to_moon_km/299792.458)
        return t


def func207(radius, height):
    if radius <= 0 or height <= 0:
        return []
    base_area = math.pi * radius ** 2
    volume = (1 / 3) * math.pi * radius ** 2 * height
    return [int(base_area), int(volume)]


def func208(num):
    num_str = str(num)
    new_num_str = num_str[-1] + num_str[1] + num_str[0]
    return int(new_num_str)


def func209(x, y, z, a, b):
    volume = x * y * z
    actual_speed = a - b
    time_seconds = volume / actual_speed
    hours = int(time_seconds // 3600)
    minutes = int((time_seconds % 3600) // 60)
    seconds = int(time_seconds % 60)
    return [hours, minutes, seconds]


def func210(h, r):
    volume = math.pi * r ** 2 * h
    # 转换为升
    volume_liter = volume / 1000
    # 向上取整
    buckets = math.ceil(20 / volume_liter)
    return buckets


def func211(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return int(distance)


def func212(x1, y1, x2, y2, x3, y3):
    side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)** 2)
    side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)** 2)
    side3 = math.sqrt((x3 - x1)**2 + (y3 - y1)** 2)
    s = (side1 + side2 + side3) / 2
    # 利用海伦公式计算面积
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return int(area+0.5)

def func213(time1_str, time2_str):
    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    sec1 = time_to_seconds(time1_str)
    sec2 = time_to_seconds(time2_str)
    return abs(sec1 - sec2)


def func214(year, month, day, hour, min, sec):
    def is_leap(year):
        """判断一个年份是否为闰年"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_days_in_month(year, month):
        """获取指定年月的天数"""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if is_leap(year) else 28
        else:
            return 0  # 无效月份

    days = 0
    # 累加1970到给定年份前一年的天数
    for y in range(1970, year):
        days += 366 if is_leap(y) else 365
    # 累加给定年份中，给定月份前的每个月的天数
    for m in range(1, month):
        days += get_days_in_month(year, m)
    # 加上给定的日数（注意日是从1开始，所以要减1）
    days += day - 1
    return [days, hour]

def func215(real_part, imag_part):
    modulus = math.sqrt(real_part ** 2 + imag_part ** 2)
    angle = math.atan2(imag_part, real_part) * (180 / math.pi)
    return [int(modulus), int(angle)]


if __name__ == "__main__":
   pass
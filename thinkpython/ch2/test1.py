# Email: zbl5337@gmail.com
# Create by Frozen
# Date: 2022/6/30 22:38
import math

x = y = 1
print(x, y)

print(5 ** 3)
print(4 / 3 * math.pi * (5 ** 3))

print(60 * (24.95 * 0.6) - 3 - 59 * 0.75)
hour = (6 * 60 * 60 + 52 * 60 + 8 * 60 + 15 + 3 * 7 * 60 + 3 * 12 + 8 * 60 + 15) / 60 // 60
minute = (6 * 60 * 60 + 52 * 60 + 8 * 60 + 15 + 3 * 7 * 60 + 3 * 12 + 8 * 60 + 15) / 60 % 60
print(hour, minute)

print(math)

# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)
print(math.pi)
print(math.sqrt(2) / 2.0)


def print_lyrics():
    print("I'm a lumberjack.")


def repeat_lyrics():
    print_lyrics()
    return "a"


print_lyrics()
repeat_lyrics()
print(print_lyrics)
print(repeat_lyrics)
print(repeat_lyrics())

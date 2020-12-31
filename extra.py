import matplotlib.pyplot as plt
import numpy

data = open("./data", "r")


def freq(data):
    crossings = 0

    prev = data[0]

    for i in range(1, len(data)):
        if prev <= 0 and data[i] > 0:
            crossings += 1
        elif prev >= 0 and data[i] < 0:
            crossings += 1
        prev = data[i]

    return round(crossings / 8)


audio_data = []
eight_digits = []

count = 0
for line in data:
    line = line.split('\n')[0].split(",")
    audio = [int(x) for x in line]
    eight_digits.append(freq(audio) - 1)
    count += 1
    if count > 7:
        audio_data.append(eight_digits)
        eight_digits = []
        count = 0

# print(audio_data)

my_string = ""

for char_data in audio_data:
    char_dec = 0
    for i in range(1, 6):
        char_dec += char_data[i] * (3 ** (5-i))
    my_string += chr(char_dec)

print(my_string)
# plt.plot(audio)
# plt.ylabel('amplitude')
# plt.show()

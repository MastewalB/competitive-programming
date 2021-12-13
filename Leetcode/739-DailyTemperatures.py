from datetime import datetime


def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        if len(stack) > 0:
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
        stack.append(i)

    return answer


def daily_temperature_recursive(temperatures):
    answer = [0] * len(temperatures)


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
with open('sample.txt', 'r') as f:
    temperatures = f.read()

# temperatures = []
# temperatures = [30, 40, 50, 60]
# answer = [1, 1, 1, 0]
before = datetime.now()
ans = daily_temperatures(temperatures)
after = datetime.now()
print(ans)
print(after-before)
# print(ans == answer)

data = [1000, 120, 200, 300, 400, 300, 200, 100]
import matplotlib.pyplot as plt

days = (range(1, len(data) + 1))

plt.plot(days, data)
plt.title('Price for days')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()
print(min(data), max(data), max(data) / 2)
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, c='black', edgecolors='red', s=100)
plt.title('scatter point', fontsize=18)
plt.xlabel('value', fontsize=16)
plt.ylabel('value of x', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40)
# plt.title('scatter point', fontsize=18)
# plt.xlabel('value', fontsize=16)
# plt.ylabel('value of x', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
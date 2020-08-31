import matplotlib.pyplot as plt

plt.scatter(3, 6, s=200)
plt.title('scatter point', fontsize=18)
plt.xlabel('value', fontsize=16)
plt.ylabel('value of x', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
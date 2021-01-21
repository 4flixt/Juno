# 01 - Identify the shape of x and y and print it in a readable form:
# Your code here!
print('x.shape = {}'.format(x.shape))
print('y.shape = {}'.format(y.shape))
# 02 - Create a plot of x over y. Use plt.plot(). Feel free to add axis label, a title etc.
# Your code here!
fig, ax = plt.subplots()
ax.plot(x,y, 'x')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

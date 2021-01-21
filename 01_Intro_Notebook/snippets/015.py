fig, ax = plt.subplots()
for k in range(5):
    ax.plot(x_reg,y_hat[k], label='Order {}'.format(str(k)))
ax.plot(x,y,'x', label='Measured')
ax.legend()

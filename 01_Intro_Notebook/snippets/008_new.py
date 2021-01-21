p = poly_regression(x,y,order=4)
X = X_fun(x_reg, order=4)
y_hat = X@p

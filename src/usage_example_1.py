n = 150
m = 100

data = np.random.random((n, m))

delta_x = 0.35 
delta_y = 0.25

x_derivative = compute_derivative_x(data, delta_x, 'center')
quick_plotContourMap(x_derivative)


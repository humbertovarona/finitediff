n = 20
m = 18

data = np.random.random((n, m))

delta_x = 0.15
delta_y = 0.12

y_derivative = compute_derivative_y(data, delta_y, 'right')
quick_plotContourMap(y_derivative)


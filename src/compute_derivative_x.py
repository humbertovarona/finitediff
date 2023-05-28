def compute_derivative_x(data, delta_x, derivative_type):
    n, m = data.shape
    derivative = np.zeros_like(data)
    if derivative_type == 'left':
        derivative[:, :-1] = (data[:, 1:] - data[:, :-1]) / delta_x
    elif derivative_type == 'right':
        derivative[:, 1:] = (data[:, 1:] - data[:, :-1]) / delta_x
    elif derivative_type == 'center':
        derivative[:, 1:-1] = (data[:, 2:] - data[:, :-2]) / (2 * delta_x)
    else:
        raise ValueError("Invalid derivative_type. Allowed values are 'left', 'right', or 'center'.")
    return derivative

# finitediff

Computes the derivatives in X and Y from a regular grid using finite differences

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-May%2C%2010%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```shell
pip install numpy
pip install matplotlib
```

## Installation

```python
import numpy as np
import matplotlib.pyplot as plt
```

# Functions list

1. **compute_derivative_x** Compute the derivative in the X-direction using finite differences

> Arguments:
>
>> `data`: 2D array of shape (n, m) containing the data.
>>
>> `delta_x`: The known spacing between data points in the x-direction.
>>
>> `derivative_type`: String specifying the type of derivative calculation. Can be 'left', 'right', or 'center'.
>>
> Returns: `derivative` 2D array of shape (n, m) containing the numerical derivative in the x-direction.

2. **compute_derivative_y** Compute the derivative in the Y-direction using finite differences

> Arguments:
>
>> `data`: 2D array of shape (n, m) containing the data.
>>
>> `delta_y`: The known spacing between data points in the y-direction.
>>
>> `derivative_type`: String specifying the type of derivative calculation. Can be 'left', 'right', or 'center'.
>>
> Returns: `derivative` 2D array of shape (n, m) containing the numerical derivative in the y-direction

3. **quick_plotContourMap** Plots a contour map with the result of the derivative by finite difference

# Usage examples

## Sample 1

```python
n = 150
m = 100

data = np.random.random((n, m))

delta_x = 0.35 
delta_y = 0.25

x_derivative = compute_derivative_x(data, delta_x, 'center')
quick_plotContourMap(x_derivative)
```

<p align="center">
<img src="/images/sample1.png" width="500">
</p>


## Sample 2

```python
n = 20
m = 18

data = np.random.random((n, m))

delta_x = 0.15
delta_y = 0.12

y_derivative = compute_derivative_y(data, delta_y, 'right')
quick_plotContourMap(y_derivative)
```

<p align="center">
<img src="/images/sample2.png" width="500">
</p>


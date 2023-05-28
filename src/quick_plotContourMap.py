def quick_plotContourMap(data):
    n, m = data.shape
    x = np.arange(0, n)
    y = np.arange(0, m)
    Y, X = np.meshgrid(y, x)

    plt.contourf(X, Y, data, cmap='viridis')
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Contour Map')
    plt.show()

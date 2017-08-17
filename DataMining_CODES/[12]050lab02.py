# coding=utf-8
"""
My registration number is  = E12050
By compare with given format  e1 = 0, e2 = 5, e3 = 0

Therefore equation is f(x) = e2 ∗ x^(e1 mod 5) − e3 ∗ x^(e2 mod 5) − e1 ∗ x^(e3 mod 5) + e3
By substituting e1, e2, e3

    f(x) = 5

"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class GradientDescent:
    def __init__(self, startingPoint, func, precision, learningRate):
        self.startingPoint = startingPoint
        self.func = func
        self.precision = precision
        self.learningRate = learningRate

    def minimize(self):
        """
        This is the function that find local minimal
        :return: return local minimal
        """

        if self.startingPoint == 0:
            return 0
        current_x = self.startingPoint

        while True:
            previous_x = current_x
            current_x = current_x - self.learningRate * self.getGradX(current_x)
            previous_step_size = np.abs(current_x - previous_x)
            if previous_step_size <= self.precision:
                break
        return current_x

    def getGradX(self, point):
        """
        This is the function that calculate gradient at given point
        :param point: point that need to calculate gradient
        :return: return gradient at given point
        """
        c1 = self.func[0]
        c2 = self.func[2]
        c3 = self.func[4]
        e1 = self.func[1]
        e2 = self.func[3]
        e3 = self.func[5]
        return (c1 * e1 * (point ** (e1 - 1))) - (c2 * e2 * (point ** (e2 - 1))) - (c3 * e3 * (point ** (e3 - 1)))


if __name__ == '__main__':
    matplotlib.rc('xtick', labelsize=30)
    matplotlib.rc('ytick', labelsize=30)
    matplotlib.rc('axes', titlesize=30)
    matplotlib.rc('legend', fontsize=30)

    """
    
    Ex 1:
    
    """
    x = range(-100, 100)
    y = np.full(200, 5)

    plt.plot(x, y)

    plt.ylabel('f(x)')
    plt.xlabel('x values')
    plt.title('f(x) = 5')

    plt.show()

    """
    Ex 2:
    
    Due to selection of initial value local minimal that gradient descent algorithm will optimize can be change. It will
    go to closet minimal that in that near to initial value. If initial value changed it may converge to another minimal 
    value.
    
    """

    """
    Ex 3:
    
    When learning rate is is small value, it will go to minimal value by small steps but if learning rate is high value, 
    it will go to minimal in high rate and there is possibility to missed the minimal value. 
    
    """

    func = [5, 0, 0, 0, 0, 0, 0]
    gda = GradientDescent(5, func, 0.00005, 0.0005)
    print '', gda.minimize()
    """
    
    Ex 4:
    
    f(x) = 5 is constant function. It has not any minimal values. It will return any staring value as local minimal 
    value. 
    
    """

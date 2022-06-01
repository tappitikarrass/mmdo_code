import sys

class GradDescent:
    def __init__(self, coef, size, eps):
        self.coef = [coef,
            [2, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 2, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 2, 0, 1, 1, 0, 0, 1, 0]]
        self.size = size
        self.eps = eps

    def get_point(self, x1, x2, x3):
        point_x1, point_x2, point_x3 = 0, 0, 0
        coef = self.coef

        for i in range(self.size):
            if coef[1][i] != 0:
                point_x1 += (coef[0][i] * coef[1][i]) * x1 ** (coef[1][i] - 1) * x2 ** coef[2][i] * x3 ** coef[3][i]
            if coef[2][i] != 0:
                point_x2 += (coef[0][i] * coef[2][i]) * x1 ** coef[1][i] * x2 ** (coef[2][i] - 1) * x3 ** coef[3][i]
            if coef[3][i] != 0:
                point_x3 += (coef[0][i] * coef[3][i]) * x1 ** coef[1][i] * x2 ** coef[2][i] * x3 ** (coef[3][i] - 1)

        return point_x1, point_x2, point_x3

    def minimum_beta(self, x1, x2, x3, grad_x1, grad_x2, grad_x3):
        coef = self.coef
        size = self.size

        left = -sys.maxsize
        right = sys.maxsize
        while right - left > self.eps:
            m_left = left + (right - left) / 3
            m_right = right - (right - left) / 3
            f_left = sum(coef[0][i] *
            (x1 - grad_x1 * m_left) ** coef[1][i] *
            (x2 - grad_x2 * m_left) ** coef[2][i] *
            (x3 - grad_x3 * m_left) ** coef[3][i] for i in range(size))

            f_right = sum(coef[0][i] *
            (x1 - grad_x1 * m_right) ** coef[1][i] *
            (x2 - grad_x2 * m_right) ** coef[2][i] *
            (x3 - grad_x3 * m_right) ** coef[3][i] for i in range(size))

            if f_left > f_right:
                left = m_left
            else:
                right = m_right
        
        return left

    def gradient_descent(self, x1, x2, x3):
        iter_num = 0
        while True:
            iter_num += 1
            grad_x1, grad_x2, grad_x3 = self.get_point(x1, x2, x3)
            b = self.minimum_beta(x1, x2, x3,
                             grad_x1, grad_x2, grad_x3)

            new_x1 = x1 - b * grad_x1
            new_x2 = x2 - b * grad_x2
            new_x3 = x3 - b * grad_x3
            
            evc = (new_x1 - x1) ** 2 + (new_x2 - x2) ** 2 + (new_x3 - x3) ** 2

            if evc**0.5 < self.eps:
                return new_x1, new_x2, new_x3, iter_num
            else:
                x1 = new_x1
                x2 = new_x2
                x3 = new_x3

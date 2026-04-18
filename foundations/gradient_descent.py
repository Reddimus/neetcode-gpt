class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        minimizer: int = init # current guess value
        for i in range(iterations):
            derivative: int = 2 * minimizer # Gradient: df/dx at current x guess
            minimizer -= learning_rate * derivative # Gradient step: new guess = old guess - (α * derivative)
        return round(minimizer, 5)
# hermitePolynomials

**Instructions:**
1. import hermite.py, example: from hermite import hermitePolynomial
2. To calculate hermite value, you will need x array of points, fx array and derivative of fx array
3. Call the function hermitePolynomial(value,x,fx,fxDerivative)


**Output:**

The value of the interpolation

**Example:**

x = [1.3, 1.6, 1.9]

fx = [0.6200860, 0.4554022, 0.2818186]

fxDer = [-0.5220232, -0.5698959, -0.5811571]

and we aree looking for the approximation of the value 1.5

call the function hermitePolynomial(value,x,fx,fxDerivative):
hermitePolynomial(1.5,x,fx,fxDer)

The approximation of the value 1.5 is: 0.5120916533333334

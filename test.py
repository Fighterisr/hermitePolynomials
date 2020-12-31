from hermite import hermitePolynomial

x = [1.3, 1.6, 1.9]
fx = [0.6200860, 0.4554022, 0.2818186]
fxDer = [-0.5220232, -0.5698959, -0.5811571]

hermitePolynomial(1.5,x,fx,fxDer)
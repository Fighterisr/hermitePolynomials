from hermite import hermitePolynomial

x = [1.3, 1.6, 1.9]
fx = [0.6200860, 0.4554022, 0.2818186]
fxDer = [-0.5220232, -0.5698959, -0.5811571]
print('Testing with:\nx: ' + str(x) +  '\nfx: ' + str(fx) + '\nderivative: ' + str(fxDer))
hermitePolynomial(1.5,x,fx,fxDer)

x= [0.1, 0.2, 0.3]
fx = [-0.6204995835, -0.2839866844, 0.0066009467]
fxDer = [3.585020824, 3.140332712, 2.666680427]
print('\nTesting with:\nx: ' + str(x) +  '\nfx: ' + str(fx) + '\nderivative: ' + str(fxDer))
hermitePolynomial(0.25,x,fx,fxDer)
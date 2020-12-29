n=3
x = [1.3, 1.6, 1.9]
y = [0.6200860, 0.4554022, 0.2818186]
yDer = [-0.5220232, -0.5698959, -0.5811571]
z = [0 for i in range(2*n+1)]
q = [[0 for j in range(2*n)] for i in range(2*n)]

for i in range(n):
    z[2*i] = z[2*i+1] = x[i]
    q[2*i][0] = q[2*i+1][0] = y[i]
    q[2*i+1][1] = yDer[i]

    if i != 0:
        q[2*i][1] = (q[2*i][0]-q[2*i-1][0])/(z[2*i]-z[2*i-1])

for i in range(2,2*n):
    for j in range(2,i+1):
        q[i][j] = (q[i][j-1]-q[i-1][j-1])/(z[i]-z[i-j])




import pulp
from pulp.constants import LpMaximize, LpStatus

x1 = pulp.LpVariable('x1')
x2 = pulp.LpVariable('x2')
x3 = pulp.LpVariable('x3')

prob = pulp.LpProblem("myProblem", LpMaximize)

prob += x1 >= -75
prob += x2 >= -100
prob += x3 >= -35
prob += 15*x1 - 5*x2 - 25*x3 >= 250
prob += -5*x1 + 15*x2 -25*x3 >= -250
prob += -5*x1 - 5*x2 + 75*x3 >= -1750
prob += 20*x1 + 20*x2 + 100*x3 == 0
prob += 18*x1 + 23*x2 + 102*x3 >= 1880
prob += 0*x1 + 3*x2 + 5*x3 + 475

status = prob.solve()

print(LpStatus[status])

print(pulp.value(x1), pulp.value(x2), pulp.value(x3))

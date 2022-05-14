# QTM3620 Assignment 1 Question 1
# Based on instructions in "Linear Programming using Python" by Priyansh Soni
# https://towardsdatascience.com/linear-programming-using-python-priyansh-22b5ee888fe0

# import webbrowser module
import webbrowser

# URL from which I base this linear programming on!
url = "https://towardsdatascience.com/linear-programming-using-python-priyansh-22b5ee888fe0"

# Open the url
user_input = input("Open the LP website? >>> ")

if user_input == 'Yes' or user_input == 'yes':
    webbrowser.open(url)
else:
    pass

"""
Question 1: [30 points] Consider the following LP problem.
𝑀ax:  3𝑋1 + 2𝑋2
𝑠. 𝑡:
3𝑋1  +  3𝑋2 ≤ 300
6𝑋1  +  3𝑋2 ≤ 480
3𝑋1  +  3𝑋2 ≤ 480
𝑋1, 𝑋2 ≥ 0

a. Sketch the feasible region for this problem and show the level curve(s).
b. Determine  the  optimal  solution  and  the  optimal  objective  value  based  on  the  graph  (
No Excel solution should be submitted)
"""
# Test for github

# Objective function: Max: 3x_1 + 2x_2

# Decision variables: x_1, x_2

# Constraints:
# 1. 3x_1 + 3x_2 <= 300
# 2. 6x_1 + 3x_2 <= 480
# 3. 3x_1 + 3x_2 <= 480
# 4. x_1 >= 0
# 5. x_2 >= 0
# 4 and 5 will be incorporated as an argument in LpVariable.matrix()

from pulp import *
import pandas as pd
import numpy as np

# Number of decision variables and constraints

n_dv = 2
n_constraints = 3

# Coefficients for respective decision variables in objective function
coefficients_obj_func = np.array([3, 2])

# Right hand side of Constraints
rhs_constraints = np.array([300, 480, 480])

# Model initialization
model = LpProblem('q1', LpMaximize)

# Define variable names
variable_names = [str(i) for i in range(1, n_dv + 1)]

variable_names.sort

# print('Variable Indices:', variable_names)

# Further define our variables
# LpVariable.matrix(prefix for variables, suffix for variables, category of the LP program, non-negativity constraints)
DV_variables = LpVariable.matrix('x', variable_names, cat = 'Integer', lowBound = 0)

# Allocate the decision variables into a matrix (just for the sake of experimentation)
allocation = np.array(DV_variables).reshape(1, 2)

# print("Decision variables/Allocaton Matrix:")
#
# print(allocation)

# Define objective function
# 'lpsum()' is used instead of 'sum()' becaues it is much faster and summarizes variables well[

obj_func = lpSum(coefficients_obj_func * allocation)

# print(obj_func)

# Add the objective function to the function

model += obj_func

# print(model)

"""
Output of print(obj_func) and print(model):

3*x_1 + 2*x_2
Rudimentary-LP-Problem:
MAXIMIZE
3*x_1 + 2*x_2 + 0
VARIABLES
0 <= x_1 Integer
0 <= x_2 Integer
"""

# Adding constraints

# Supply Constraints
# for i in range(n_warehouses):
#     print(lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i])
#     model += lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i] , "Supply Constraints " + str(i)

# Demand Constraints
# for j in range(n_customers):
#     print(lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j])
#     model += lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j] , "Demand Constraints " + str(j)

c_first_const = np.array([3, 3])
c_second_const = np.array([6, 3])
c_third_const = np.array([3, 3])

# test codes
# print(allocation[0])
# print(c_first_const)
# print(allocation[0][0])

# First constraint

# print(c_first_const[0] * allocation[0][0] + c_first_const[1] * allocation[0][1] <= rhs_constraints[0])
model += c_first_const[0] * allocation[0][0] + c_first_const[1] * allocation[0][1] <= rhs_constraints[0], 'Constraint ' + str(1)

# Second constraint

# print(c_second_const[0] * allocation[0][0] + c_second_const[1] * allocation[0][1] <= rhs_constraints[1])
model += c_second_const[0] * allocation[0][0] + c_second_const[1] * allocation[0][1] <= rhs_constraints[1], 'Constraint ' + str(2)

# Third constaraint

# print(c_third_const[0] * allocation[0][0] + c_third_const[1] * allocation[0][1] <= rhs_constraints[2])
model += c_third_const[0] * allocation[0][0] + c_third_const[1] * allocation[0][1] <= rhs_constraints[2], 'Constraint ' + str(3)

# print(model)

# Export the model description
# model.writeLP('q1.lp')

# Run the model and check status
model.solve(PULP_CBC_CMD())

status = LpStatus[model.status]

print(status)

# Output the objective function value and decision variables value

# Objective function
print('Total Cost:', model.objective.value())

# Decision variables
# alt + ¥ for \

for v in model.variables():
    try:
        print(v.name, '=', v.value())
    except:
        print('Error: Couldn\'t Find Value')

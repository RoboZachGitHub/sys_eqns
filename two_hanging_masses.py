import numpy as np
import scipy.optimize
import math



def func_to_opt(vector_of_x_vars):

	x = vector_of_x_vars
	f = np.ones(len(x))

	f[0] =	3*x[3]	+	4*x[4]	+	4*x[5]	-	8.0
	f[1] =	3*x[0]	+	4*x[1]	-	4*x[2]
	f[2] =	x[6]*x[0]	-	x[7]*x[1]	-	10.0
	f[3] = 	x[6]*x[3]	-	x[7]*x[4]
	f[4] =	x[7]*x[1]	+	x[8]*x[2]	-	20.0
	f[5] =	x[7]*x[4]	-	x[8]*x[5]
	f[6] =	math.pow(x[0], 2)	+	math.pow(x[3], 2)	-	1.0
	f[7] = 	math.pow(x[1], 2)	+	math.pow(x[4], 2)	-	1.0
	f[8] =	math.pow(x[2], 2)	+	math.pow(x[5], 2)	-	1.0

	return f
	
			
# func is the function, x0 is an initial guess
x0 = np.ones(9)

solution = scipy.optimize.fsolve(func_to_opt, x0) 

print solution

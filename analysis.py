import sys
# append the folder of your code
sys.path.append("case/pcms_thomas")

# import the code you want to analysis
import thomas

# import the function provided by our group 
import macauaws

# we import the simulated parameters to evaluate our reward functions
params = macauaws.get_param()

rewards = thomas.reward_function(params)

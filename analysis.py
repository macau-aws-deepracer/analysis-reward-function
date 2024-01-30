import sys
# append the folder of your code
sys.path.append("case/pcms_example")

# import the code you want to analysis
import example

# import the function provided by our group 
import macauaws

# we import the simulated parameters to evaluate our reward functions
params = macauaws.get_param()

rewards = (example.reward_function(params))

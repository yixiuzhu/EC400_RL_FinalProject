# EC400_FinalProject
Different test codes for the EC 400: Reinforcement Learning Final Project. This is working with PyTuxKart and python in order to minimize times. Note, due to issues with my computer, only 50 training runs were run.

# 1st Plan
The motive behind this idea was to double the number of outputs in each layer with the idea being if it doubles all the way to 256, the neural network will be able to collect enough information in order to accurately find each aim point. However this proved less than successful. 
[planner_1.py](planner_1.py)

# 2nd Plan
In order to improve the controller, I thought it might help to use the fact that there are essentially 2 variables that are important for this first baseline of code, the parameter for the aimpoint when the car should drift, and the parameter for how much the car should steer. In order to test different values, I found that the best parameter for drifting should be between .1 and .7, and the best parameter for steering should be between 1 and 5. This wasn't as help as I would have liked because there were not 2 parameters that worked the best universally, it was more track-dependent, so its likely the "2-parameter" model likely was not comprehensive enough to have success. 
[controller](controller.py)

# 3rd Plan
[planner_3.py](planner_3.py)

# 4th Plan
I thought it might help to have a smaller difference between input and output and to add more layers. Then, each layer would improve more and more, and by adding a lot of layers, this would help. This worked relatively well, and better than the 1st plan by a small margin, but didn't totally work. 
[planner_4.py](planner_4.py)

# 5th Plan
Similar to the 4th plan, the thinking was having a large difference between the input and output, but only have a few layers. As a result, the neural network would be able to get all of the necessary information to make the weights, but prevent overfitting. This worked the best, and lead to trying more fine tuning to this idea. 
[planner_5.py](planner_5.py)

# 6th Plan
Almost the exact same as the 4th plan, but changing some of the numbers. This did not work very well at all likely due to some of the same problems. 
[planner_6.py](planner_6.py)

# 7th Plan
I tried to work with the planner that came from on of my teammates, which worked the best. He had several layers, which took way took too long ony my computer, so I cut it down to see how it performed. The results show that [planner_7.py](planner_7.py) worked decently well, especially comparing to the previous attempts. 

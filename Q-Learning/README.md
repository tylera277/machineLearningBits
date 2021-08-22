I implemented q-learning reinforcement learning to solve simple mazes. I did not write this solely on my own, I got it mainly from 
https://www.analyticsvidhya.com/blog/2021/04/q-learning-algorithm-with-step-by-step-implementation-using-python/

The original maze is in this form,
<img width="232" alt="rawMaze" src="https://user-images.githubusercontent.com/37377528/130355837-f7cc8f5b-9a0f-4309-a444-bedfcb9486bd.png">

I then have to convert it to this form in order to be more easily implemented into the program,
<img width="323" alt="mazePutIntoProgram" src="https://user-images.githubusercontent.com/37377528/130355875-a1b08f59-c552-49ca-8f21-fdc4a35c2da5.png">

And after a few runs of the program, I get output that looks like this,
<img width="1157" alt="outputFromProgram" src="https://user-images.githubusercontent.com/37377528/130356027-e59b1bdb-4da9-4c54-b3fa-1a2a17757b61.png">
That gives me the coordinates on my graphing paper of what steps are needed to be taken in order to successfully complete the maze.

Obviously this program has the issue of not scaling very well to complicated mazes because it takes me a bit of time to accurately convert
the raw maze to the one seen on the graph paper, but nonetheless I think this is pretty neat method.

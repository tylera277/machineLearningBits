I implemented q-learning reinforcement learning to solve simple mazes.


The original maze is in this form,
<p align="center">
<img width="232" alt="rawMaze" src="https://user-images.githubusercontent.com/37377528/130355837-f7cc8f5b-9a0f-4309-a444-bedfcb9486bd.png">
</p>

I then have to convert it to this form in order to be more easily implemented into the program,
<p align="center">
<img width="323" alt="mazePutIntoProgram" src="https://user-images.githubusercontent.com/37377528/130355875-a1b08f59-c552-49ca-8f21-fdc4a35c2da5.png">
</p>
  
And after a few runs of the program, I get output that looks like this,
<p align="center">
<img width="1157" alt="outputFromProgram" src="https://user-images.githubusercontent.com/37377528/130356027-e59b1bdb-4da9-4c54-b3fa-1a2a17757b61.png">
</p>
That gives me the coordinates on my graphing paper of what steps are needed to be taken in order to successfully complete the maze.

Obviously this program has the issue of not scaling very well to complicated mazes because it takes me a bit of time to accurately convert
the raw maze to the one seen on the graph paper, but nonetheless I think this is a pretty neat method.

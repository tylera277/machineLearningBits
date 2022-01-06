
Trying to implement the Convolutional Neural Network (CNN) LeNet-5 architecture with the goal of hopefully getting a higher accuracy in identifying digits in the MNIST database than what my simple neural network achieved (94%).
A view of the overall architecture I am going for is included below.

<p align="center">
<img width="665" alt="lenet5Architecture" src="https://user-images.githubusercontent.com/37377528/148327158-da8ee344-e086-4a97-8d31-2468b798b89e.png">
</p>

Steps:
1.) Get an overall view of the specific sizes of the matrices after each of these steps in the layer. The input is a 28x28x1 matrix.
2.) Get a grasp on the matrix math that is occurring in the convolution step.
3.)       "                                   "     in the subsampling step. 
    --> FOr subsampling, I'm going to use max pool.
4.) Get an understanding on how to backpropagate through the convolution layers and applying it to the initially randomnized filters.
5.) ...

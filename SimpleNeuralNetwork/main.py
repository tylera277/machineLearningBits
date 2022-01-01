
import pandas as pd
import numpy as np

from PIL import Image
from sigmoid import sigmoid, sigmoid_prime

# Set the randomness for reproducibility
np.random.seed(897887897)


Raw = pd.read_csv('/Users/starman/Desktop/winter2021-programming/python-MNIST/mnist_train.csv')


#Raw = Raw.drop(labels=(range(0, 3))).drop(labels=(range(4, len(Raw))))
Raw = Raw.to_numpy()


input_pixels = np.zeros((784, 1))

# Rate which is utilized in deciding the gradient descent steps
learningRate = .6

# Weighted connections between neurons
first_layer_weights = np.random.randn(32, 784)
second_layer_weights = np.random.randn(32, 32)
third_layer_weights = np.random.randn(10, 32)

# Biases for each neuron; two levels
first_layer_biases = np.zeros((32, 1))
second_layer_biases = np.zeros((32, 1))
output_biases = np.zeros((10, 1))

activation_1st_layer = np.zeros((32, 1))
activation_2nd_layer = np.zeros((32, 1))
output = np.zeros((10, 1))

# These arrays store the weighted sums before they go into
# sigmoid; crucial for back propagation
zs_layer1 = np.zeros((32, 1))
zs_layer2 = np.zeros((32, 1))
zs_layer3 = np.zeros((32, 1))


for epochs in range(1, 10, 1):

    diff_squared_sum = 0

    for train_image in range(1, 50000):

        actual = np.zeros((10, 1))
        actual_number = Raw[train_image][0]

        for i in range(1, len(Raw[train_image])):
            input_pixels[i-1] = (Raw[train_image][i]/255.0)


        # Forward feeding section
        z = np.dot(first_layer_weights, input_pixels) + first_layer_biases
        zs_layer1 = z
        activation_1st_layer = sigmoid(z)


        # ########### ##########
        z = np.dot(second_layer_weights, activation_1st_layer) + second_layer_biases
        zs_layer2 = z
        activation_2nd_layer = sigmoid(z)

        # ########### ##########

        z = np.dot(third_layer_weights, activation_2nd_layer) + output_biases
        zs_layer3 = z
        output = sigmoid(z)

        # ########### ##########

        # Creating the array with the ground truth value for the 10 elements
        actual = np.zeros((10, 1))
        for k in range(0, 10):
            if k == actual_number:
                actual[k] = 1
            else:
                actual[k] = 0



        # ########### ############
        # Back propagation section

        # ########################
        delta_output_3rd = (output - actual)*sigmoid_prime(zs_layer3)

        # bias gradient
        bias_grad_3rd = delta_output_3rd
        # weight gradient
        weight_grad_3rd = np.dot(delta_output_3rd, activation_2nd_layer.T)
        # input gradient
        # input_grad_3rd = np.dot(third_layer_weights.T, delta_output_3rd)
        input_grad_3rd = delta_output_3rd

        # #########################

        #delta_2nd = input_grad_3rd*activation_2nd_layer*(1.0-activation_2nd_layer)
        delta_2nd = np.dot(third_layer_weights.T, input_grad_3rd)*sigmoid_prime(zs_layer2)

        # bias gradient
        bias_grad_2nd = delta_2nd
        # weight gradient
        weight_grad_2nd = np.dot(delta_2nd, activation_1st_layer.T)
        # input gradient
        input_grad_2nd = delta_2nd

        # #########################
        #delta_1st = input_grad_2nd * activation_1st_layer*(1.0-activation_1st_layer)
        delta_1st = np.dot(second_layer_weights.T, input_grad_2nd) * sigmoid_prime(zs_layer1)

        # bias
        bias_grad_1st = delta_1st
        # weight
        weight_grad_1st = np.dot(delta_1st, input_pixels.T)

        # ########## ##############
        # Updates the weights and biases using gradient descent

        third_layer_weights -= learningRate * weight_grad_3rd
        output_biases -= learningRate * bias_grad_3rd

        second_layer_weights -= learningRate * weight_grad_2nd
        second_layer_biases -= learningRate * bias_grad_2nd

        first_layer_weights -= learningRate * weight_grad_1st
        first_layer_biases -= learningRate * bias_grad_1st

        # These record and measure the loss function, which I am using
        # MSE (mean square error)
        diff_squared = np.square(actual - output)
        diff_squared_sum += np.sum(diff_squared)


    cost = diff_squared_sum/1000.0
    #print(output)
    print(cost)




# Evaluation on test data set

RawTest = pd.read_csv('/Users/starman/Desktop/winter2021-programming/python-MNIST/mnist_test.csv')


RawTest = RawTest.to_numpy()

CounterRight = 0

for test_image in range(0, 9800, 1):

    input_pixels = np.zeros((784, 1))
    actual_number = RawTest[test_image][0]

    for i in range(1, len(RawTest[test_image])):
        input_pixels[i - 1] = (RawTest[test_image][i] / 255.0)

    # Forward feeding section
    z = np.dot(first_layer_weights, input_pixels) + first_layer_biases
    activation_1st_layer = sigmoid(z)

    # ########### ##########
    z = np.dot(second_layer_weights, activation_1st_layer) + second_layer_biases
    activation_2nd_layer = sigmoid(z)

    # ########### ##########

    z = np.dot(third_layer_weights, activation_2nd_layer) + output_biases
    output = sigmoid(z)

    predictedOutput = np.argmax(output)

    if predictedOutput == actual_number:
        CounterRight += 1

print("percentage correct:{}".format(CounterRight/9800.0))

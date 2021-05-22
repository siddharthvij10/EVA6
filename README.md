# EVA6
EVA6 Batch Assignment for Pytorch

# Summary
The CNN build as a part of this assignment takes in a random number from 0 to 9 along with an image from MNIST dataset and outputs the sum of random number inputted and the number in MNIST image.

# Data generation
Data for MNIST is generated from pytorch datasets and a dataset is written. For random numbers - We create a list of random number in every iteration with length same as batch size. This list of random number is converted to a tensor which is then forwarded to the model along with MNIST image. 

# Adding MNIST image and random number
This addition is performed as follows. 
We create a list of random number in every iteration with length same as batch size. This list of random number is converted to a tensor which is then forwarded to the model along with MNIST image. 
The output 2d image from Forward part of model has it's labels taken out via torch.argmax(x, dim=1). The labels extracted from above call are added to the tensor of random numbers. The output sum is then converted to one hot encoded vector with 18 (9 numbers and 2 inputs) classes. 

# Cross entropy loss
We picked cross entropy loss. This is because we have one of the output as an one hot encoded vector. This is the sum of random number and MNIST image number. Cross entropy can work on one hot encoded data. 
The second input is an image. Cross entropy will work here as well since both the inputs are categorical and we need to find the best probabilty of one of the outputs.


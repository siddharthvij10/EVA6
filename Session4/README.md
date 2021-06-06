Team includes:
S R Prathaban
Divyanshu Raj
Siddharth Vij
Santosh Chaganti


# Assignment Part 1

## Summary
Part 1 of this session's assignment is to write the backpropagation excel and explain all the important steps in this file. We also need to attach a screenshot of the excel and the different Error graphs created by changing the learning rate. The excel containing LR graph and backpropagation is uploaded in repo.

## Screenshot of backpropagation excel
![image](https://user-images.githubusercontent.com/17743850/120006925-02383f00-bff7-11eb-974d-e4e8ca10dcee.png)

## Important Steps of backpropagation excel
1. **Network** - 
    1. We draw a simple network. The hidden layer and output layer in network has 2 parts - One is the node itself and other is the activated node. 
    2. [*Activated node is the activation function applied to the node.* The formula given in excel explains that we have used sigmoid function as our activation.]
    3. The total error in output is sum of the 2 errors - E1 and E2 being passed through 2 parts of network.
3. **Forward Propagation** -
    1. Compute the formula for h1, h2, o1, o2. These are pretty straight forward as shown in excel.
    2. Formula of activated neuron - a_h1, a_h2, a_o1, a_02 are sigmoid applied to h1, h2, o1, o2 respectively. Apart from Signoid, we can apply any other function as well.
    3. The total error is summation of E1 and E2. [*We are using Mean Squared Error as the error function here.*] 
4. **Back Propagation** -
    1. The first major task of BP is to calculate the derivative of total error w.r.t the weights.
        1. Derivative of Total error w.r.t weight is sum of derivative of individual errors (E1, E2) w.r.t weight (lets say - w5). **Derivates of Total Error w.r.t w5 till w8 is calculated as follows.**
            1. *Derivate of Total Error w.r.t w5  is equal to derivative of E1 w.r.t w5. The error E2 has no impact on this equation since there is no way E2 is used to reach w5 in the network.* 
            2. Few important derivates that are utilized in this computation are [*derivative of sigmoid which is sigmoid(x)(1-sigmoid(x)) based on the quotient rule of differentiation.*]  Other derivates are pretty easily calculated using sum rule, power rule and other simple rules of differentiation.
        2. Derivative of Total error w.r.t weight is sum of derivate of individual errors (E1, E2) w.r.t weight. **Derivates of Total error w.r.t w1 till w4 is calculated as follows.**
            1. [*Derivate of Total Error w.r.t w1 is equal to derivative of E1 w.r.t w1 plus derivative of E2 w.r.t w1. Error E1 and Error E2 both play role in this calculation.*]
            2. The detailed formulas are given in excel for this computation.
      
5. **Process** - 
    1. Start the network with inputs, targets and randomly assigned weights. 
    2. Forward propagation happens as explained in FW step using default weights. 
    3. [*The weights get updated using backpropagation in second iteration. We update the weights (w1, w2 .... w8) based on the value of learning rate (constant) and derivatives of total error w.r.t corresponding weights calculated in BP step.*]
    4. FW and BP keep on happening till last iteration.

## Screenshot of Charts made by changing LR
![image](https://user-images.githubusercontent.com/17743850/120014031-2d269100-bfff-11eb-893a-dda11fa2d3c6.png)

## Effect of modifying LR on Error Graph
As we increase the learning rate, the error gets reduced faster. This means that we are converging to the global minima faster. We can see that with LR 0.1, error gets reduced slowly and at the end of iteration, error is still pretty high which is bad. We keep on increasing LR. Finally, we can see that with LR 2, we are able to achieve the global minima within the limited iterations.
If LR is pretty low, the convergence to minima will take a lot of time and iterations. If LR is pretty hight, we may never be able to reach minima within the number of iterations. 
We need to find the optimum value of LR using which we can reach the global minima - least error - within the iterations.


## PART II
* **Main file** Assignment.ipynb
* **Contents** 
MNIST classification using CNN. 
* **Requirements** 
1. Use less than 20K parameters
1. Train for less than 20 epochs
1. Accuracy >= 99.4% 

* **Solution**
* **Network architecture**
```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 28, 28]              80
       BatchNorm2d-2            [-1, 8, 28, 28]              16
            Conv2d-3           [-1, 16, 28, 28]           1,168
       BatchNorm2d-4           [-1, 16, 28, 28]              32
            Conv2d-5           [-1, 32, 28, 28]           4,640
       BatchNorm2d-6           [-1, 32, 28, 28]              64
         MaxPool2d-7           [-1, 32, 14, 14]               0
            Conv2d-8            [-1, 8, 14, 14]             264
            Conv2d-9           [-1, 16, 14, 14]           1,168
      BatchNorm2d-10           [-1, 16, 14, 14]              32
           Conv2d-11           [-1, 32, 14, 14]           4,640
      BatchNorm2d-12           [-1, 32, 14, 14]              64
        MaxPool2d-13             [-1, 32, 7, 7]               0
           Conv2d-14              [-1, 8, 7, 7]             264
           Conv2d-15             [-1, 16, 7, 7]           1,168
      BatchNorm2d-16             [-1, 16, 7, 7]              32
           Conv2d-17             [-1, 32, 7, 7]           4,640
      BatchNorm2d-18             [-1, 32, 7, 7]              64
AdaptiveMaxPool2d-19             [-1, 32, 1, 1]               0
           Linear-20                   [-1, 10]             330
================================================================
Total params: 18,666
Trainable params: 18,666
Non-trainable params: 0
----------------------------------------------------------------
```

* **Training**
1. Trained for 19 epochs
1. SGD optimizer with a learning rate of 0.1

* **Results**
1. Train set: Accuracy: 59955/60000 (99.92%)
2. Test set: Accuracy: 9940/10000 (99.40%)


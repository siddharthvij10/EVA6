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
* **Main file** EVA_Session_4.ipynb
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
            Conv2d-1            [-1, 8, 26, 26]              80
       BatchNorm2d-2            [-1, 8, 26, 26]              16
            Conv2d-3           [-1, 16, 24, 24]           1,168
       BatchNorm2d-4           [-1, 16, 24, 24]              32
            Conv2d-5           [-1, 16, 22, 22]           2,320
       BatchNorm2d-6           [-1, 16, 22, 22]              32
         MaxPool2d-7           [-1, 16, 11, 11]               0
           Dropout-8           [-1, 16, 11, 11]               0
            Conv2d-9             [-1, 24, 9, 9]           3,480
      BatchNorm2d-10             [-1, 24, 9, 9]              48
          Dropout-11             [-1, 24, 9, 9]               0
           Conv2d-12             [-1, 24, 7, 7]           5,208
      BatchNorm2d-13             [-1, 24, 7, 7]              48
          Dropout-14             [-1, 24, 7, 7]               0
           Conv2d-15             [-1, 32, 5, 5]           6,944
      BatchNorm2d-16             [-1, 32, 5, 5]              64
        AvgPool2d-17             [-1, 32, 1, 1]               0
           Linear-18                   [-1, 10]             330
================================================================
Total params: 19,770
Trainable params: 19,770
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.45
Params size (MB): 0.08
Estimated Total Size (MB): 0.53
----------------------------------------------------------------
```

* **Training**
1. Trained for 19 epochs
1. SGD optimizer with a learning rate of 0.1

* **Results**
1. Train set: Accuracy: 59796/60000 (99.66%)
2. Test set: Accuracy: 9951/10000 (99.51%)


## Team ##

* S R Prathaban
* Divyanshu Raj
* Siddharth Vij
* Santosh Chaganti

### Session 5 Assignment ###
Achieve 99.4% accuracy consistantly in at-least last 3 iterations of 15 iterations total. The base model can be picked from previous assignments. Params should be less than 10k.


### Base Model
* **File** Base_Model.ipynb
1. #### Result
  * Params - 6,377,760, Best Train Acc - 99.94, Best Test Acc - 99.24
2. #### Analysis
  * Quite heavy model and has potential to achieve desired result.  

### Iteration 1
* **File** Experiment_1.ipynb
1. #### Target
  * Reduce size of model
2. #### Result
  * Params - 9,128, Best Train Acc - 99.22, Best Test Acc - 98.91 
3. #### Analysis
  * Overfitting in model; model has capability to learn more

### Iteration 2
* **File** Experiment_2.ipynb
1. #### Target
  * Overfitting - Reduce overfitting by adding regularization and add training capacity by adding drop out. 
  * Increase Capacity - Replace last layer with GAP to save some parameters. Reduce parameters further by using a 1 * 1 after max pool instead of current 3 * 3.
2. #### Result
  * Params - 7,848, Best Train Acc - 99.48, Best Test Acc - 99.32
3. #### Analysis
  * There is a mistake in model that the final layer does not converge to 10 outputs as it should be in case of mnist.
  * There is a slight overfitting.

### Iteration 3
* **File** Experiment_3.ipynb
1. #### Target
  * Correct mistake in model w.r.t outputs of final layer - use FC layer after gap
  * Increase val of dropout slightly
2. #### Result
  * Params - 8018 , Best Train Acc - 99.43, Best Test Acc - 99.37
3. #### Analysis
  * Model reached target but didnt stay there. 

### Iteration 4
* **File** Experiment_4.ipynb
1. #### Target
  * Add Learning Rate concept using plateau to make sure accuracy stays near to 99.4 
2. #### Result
  * Params - 8018, Best Train Acc - 99.44 , Best Test Acc - 99.45
3. #### Analysis
  * Model slightly underfitting but achieved target

## Architecture of Last iteration
```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 28, 28]              72
              ReLU-2            [-1, 8, 28, 28]               0
       BatchNorm2d-3            [-1, 8, 28, 28]              16
           Dropout-4            [-1, 8, 28, 28]               0
            Conv2d-5            [-1, 8, 28, 28]             576
              ReLU-6            [-1, 8, 28, 28]               0
       BatchNorm2d-7            [-1, 8, 28, 28]              16
           Dropout-8            [-1, 8, 28, 28]               0
         MaxPool2d-9            [-1, 8, 14, 14]               0
           Conv2d-10           [-1, 16, 14, 14]           1,152
             ReLU-11           [-1, 16, 14, 14]               0
      BatchNorm2d-12           [-1, 16, 14, 14]              32
          Dropout-13           [-1, 16, 14, 14]               0
           Conv2d-14           [-1, 16, 14, 14]           2,304
             ReLU-15           [-1, 16, 14, 14]               0
      BatchNorm2d-16           [-1, 16, 14, 14]              32
          Dropout-17           [-1, 16, 14, 14]               0
        MaxPool2d-18             [-1, 16, 7, 7]               0
           Conv2d-19              [-1, 8, 7, 7]             128
           Conv2d-20             [-1, 16, 5, 5]           1,152
             ReLU-21             [-1, 16, 5, 5]               0
      BatchNorm2d-22             [-1, 16, 5, 5]              32
          Dropout-23             [-1, 16, 5, 5]               0
           Conv2d-24             [-1, 16, 3, 3]           2,304
             ReLU-25             [-1, 16, 3, 3]               0
      BatchNorm2d-26             [-1, 16, 3, 3]              32
          Dropout-27             [-1, 16, 3, 3]               0
        AvgPool2d-28             [-1, 16, 1, 1]               0
           Linear-29                   [-1, 10]             170
================================================================
```

## Receptive Field of Last iteration - ReceptiveField.xls
!![ReceptiveField](https://user-images.githubusercontent.com/17743850/120941321-931dc180-c73f-11eb-9ae5-d0a450ed58d8.PNG)

## Logs from Last iteration
epoch number  11
Train set: Average loss: 0.0002, Accuracy: 59633/60000 (99.39%)
Test set: Average loss: 0.0194, Accuracy: 9942/10000 (99.42%)

epoch number  12
Train set: Average loss: 0.0002, Accuracy: 59616/60000 (99.36%)
Epoch    12: reducing learning rate of group 0 to 1.0000e-05.
Test set: Average loss: 0.0193, Accuracy: 9945/10000 (99.45%)

epoch number  13
Train set: Average loss: 0.0002, Accuracy: 59595/60000 (99.33%)
Epoch    13: reducing learning rate of group 0 to 1.0000e-06.
Test set: Average loss: 0.0196, Accuracy: 9941/10000 (99.41%)

epoch number  14
Train set: Average loss: 0.0002, Accuracy: 59664/60000 (99.44%)
Test set: Average loss: 0.0196, Accuracy: 9943/10000 (99.43%)

epoch number  15
Train set: Average loss: 0.0002, Accuracy: 59629/60000 (99.38%)
Epoch    15: reducing learning rate of group 0 to 1.0000e-07.
Test set: Average loss: 0.0195, Accuracy: 9943/10000 (99.43%)

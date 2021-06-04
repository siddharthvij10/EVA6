## Team ##

* S R Prathaban
* Divyanshu Raj
* Siddharth Vij
* Santosh Chaganti

### Session 5 Assignment ###
Achieve 99.4% accuracy consistantly in at-least last 3 iterations of 15 iterations total. The base model can be picked from previous assignments. Params should be less than 10k.

[### Base Model]
* **File** Base_Model
#### Result
* Params - 6,377,760, Best Train Acc - 99.94, Best Test Acc - 99.24
#### Analysis
* Quite heavy model and has potential to achieve desired result.

[### Iteration 1]
* **File** Experiment_1
#### Target
* Reduce size of model
#### Result
* Params - 9,128, Best Train Acc - 99.22, Best Test Acc - 98.91 
#### Analysis
* Overfitting in model; model has capability to learn more

[### Iteration 2]
* **File** Experiment_2
#### Target
* Overfitting - Reduce overfitting by adding regularization and add training capacity by adding drop out. 
* Increase Capacity - Replace last layer with GAP to save some parameters. Reduce parameters further by using a 1 * 1 after max pool instead of current 3 * 3.
#### Result
* Params - 7,848, Best Train Acc - 99.48, Best Test Acc - 99.32
#### Analysis
* There is a mistake in model that the final layer does not converge to 10 outputs as it should be in case of mnist.
* There is a slight overfitting.

[### Iteration 3]
* **File** Experiment_3
#### Target
* Correct mistake in model w.r.t outputs of final layer - use FC layer after gap
* Increase val of dropout slightly
#### Result
* Params - 8018 , Best Train Acc - 99.43, Best Test Acc - 99.37
#### Analysis
* Model reached target but didnt stay there. 

[### Iteration 4]
* **File** Experiment_4
#### Target
* Add Learning Rate concept using plateau to make sure accuracy stays near to 99.4 
#### Result
* Params - 8018, Best Train Acc - , Best Test Acc -  
#### Analysis
* Model slightly underfitting but achieved target

[## Logs from Last iteration]
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

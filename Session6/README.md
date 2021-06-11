## Team ##

* S R Prathaban
* Divyanshu Raj
* Siddharth Vij
* Santosh Chaganti

### Session 5 Assignment ###
1. Objective 1 - Create 3 versions of best model from last assignment. Version 1 should implement Layer Normalisation. Version 2 should implement Group Normalisation. Version 3 should implement Batch + L1 Normalisation.
2. Objective 2 - Create a model file that takes Normalisation Flag as an argument. The normalisation flag can have either one of these values - Batch/Layer/Group/All. The model file 
applies the normalisation technique/techniques to the model based on Normalisation flag passed by user. Once done, execute the model file for all the 3 normalisation techniques 
and record following items:
    1. Test Loss and Test Accuracy graphs
    2. Misclassified images

### Files Created in Response to Objective 1
We created 3 files titled - [BatchNorm_L1.ipynb](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective1/BatchNorm_L1.ipynb), [GroupNorm.ipynb](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective1/GroupNorm.ipynb) and [LayerNorm.ipynb](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective1/LayerNorm.ipynb) placed in folder [Objective1](https://github.com/siddharthvij10/EVA6/tree/dev_unpublished/Session6/Objective1)

### Files Created in Response to Objective 1
We have created 4 files titled - [BN.py](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective2/BN.py), [LN.py](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective2/LN.py), [GN.py](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective2/GN.py) and [model.py](https://github.com/siddharthvij10/EVA6/blob/dev_unpublished/Session6/Objective2/Model.ipynb) that are placed in folder [Objective2](https://github.com/siddharthvij10/EVA6/tree/dev_unpublished/Session6/Objective2).

### How to perform normalization techniques
1. Batch normalization is performed across channels of all images. Let's say, we are in layer number 2, we consider channel number 1 of all the images to find mean and std. Hence, the parameters this technique creates depends highly on number of channels in each layer.
2. Layer normalization is performed on each and every image seperately. We get all the channels of let's say image number 1 in layer number 2  and find mean and std and hence, parameters in Layer norm are dependent on number of images.
3. Group normalisation is somewhere in between BN and LN. Here we divide the channels of each and every image in each and every layer into groups and then normalize them seperately. 

### Findings from the normalization techniques

#### Train and Test Accuracy of 3 models built are:
1. Batch Norm - Params =  :Train Accuracy =  , Test Accuracy = 
2. Layer Norm - Params =  :Train Accuracy = , Test Accuracy = 
3. Group Norm - Params =  :Train Accuracy =  , Test Accuracy =

#### Performance Comparison: - TODO
1. GN
2. LN
3. BN
4. Hence the performance of the regularisation based on this esperiment is - 

### All Graphs

### Collection of Misclassified images
1. Layernorm

![LNimage](https://user-images.githubusercontent.com/17743850/121756775-e7a6af80-cb38-11eb-9a84-fa6fb01db8c0.PNG)

2. Groupnorm

![GNIMage](https://user-images.githubusercontent.com/17743850/121756803-fee59d00-cb38-11eb-9f28-ef448008cb72.PNG)

3. Batchnorm

![BNimage](https://user-images.githubusercontent.com/17743850/121756815-09a03200-cb39-11eb-8974-e4e0dbd88fb3.PNG)






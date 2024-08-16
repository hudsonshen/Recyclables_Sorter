#Recyclables_Sorter
My Recyclables Sorter is able to identify the three most common types of recyclable cans/bottles: Glass, Aluminum, and Plastic. Each year, approximately 30 billion tons of recyclable cans and bottles are thrown into the trash. One main reason for this is because it take time to have to sort different types of recyclable materials. However, with my Recyclables Sorter, this process could be expedited and eventually automated.

##The Algorithm
This re-trained ResNet-18 model was created on Jetson Nano and trained on a dataset of images of plastic (PET) bottles, aluminum cans, and glass bottles. It runs on an imagenet.py program that will classify the type of recyclable.

##Running the Project
1. Install both the Jetson-Inference Library and Python3 to your Jetson Nano.
2. Download all of the files on this Github page.
3. Be sure to have Docker installed, then clone the jetson-inference into your home folder
4. 

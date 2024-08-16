# Recyclables_Sorter
My Recyclables Sorter is able to identify the three most common types of recyclable cans/bottles: Glass, Aluminum, and Plastic. Each year, approximately 30 billion tons of recyclable cans and bottles are thrown into the trash. One main reason for this is because it take time to have to sort different types of recyclable materials. However, with my Recyclables Sorter, this process could be expedited and eventually automated.

## The Algorithm
This re-trained ResNet-18 model was created on Jetson Nano and trained on a dataset of images of plastic (PET) bottles, aluminum cans, and glass bottles. It runs on an imagenet.py program that will classify the type of recyclable.

## Running the Project
1. Install both the Jetson-Inference Library and Python3 to your Jetson Nano.
2. Download all of the files on this Github page.
3. Be sure to have Docker installed, then clone the jetson-inference into your home folder.
4. Set the net and data variables as shown below:
   `NET=models/snake`
   `DATASET=data/snake3`
5. Open the terminal and navigate to the classification directory
   `cd jetson-inference/python/training/classification`
6. Use this command to process a test image, change folder to whichever catagory you want, and choose an image after 'xxx'
   `imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/Recyclables-Data/"Folder Test" Folderxxx.jpg`
7. View the output image to see the results.

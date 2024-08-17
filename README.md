# Recyclables_Sorter
My Recyclables Sorter is able to identify the three most common types of recyclable cans/bottles: Glass, Aluminum, and Plastic. Each year, approximately 30 billion tons of recyclable cans and bottles are thrown into the trash. One main reason for this is because it take time to have to sort different types of recyclable materials. However, with my Recyclables Sorter, this process could be expedited and eventually automated.

## The Algorithm
This re-trained ResNet-18 model was created on Jetson Nano and trained on a dataset of images of plastic (PET) bottles, aluminum cans, and glass bottles. It runs on an imagenet.py program that will classify the type of recyclable.

## Running the Project
1. Install both the Jetson-Inference Library and Python3 to your Jetson Nano.
2. Download all of the files on this Github page.
3. Add any image to the final-project folder, either from the internet or from the test folder.
4. Use this command to process the image where the PET787.jpg is the title of your image:

   `python3 final-project.py PET787.jpg OutputImage.jpg`
5. View the output image to see the results - the percentage and clasification will be in the top left corner.
6. Watch the video for the example!

Video Link: https://drive.google.com/file/d/19SO9N4ShPQ7OZqgIMcQNbcjnPKaZ5_uS/view?usp=sharing 

# Fall 2019 CAIS++ Project working with the Waymo Open Dataset


<img style="float: right;" src="Images/cais_logo.png" >

<img style="float: right;" src="Images/waymo_symbol.png">

In the Fall of 2019, me (Ted Lewitt), Eric Ye and Jack Elliott explored the recently released Waymo Open Dataset, a dataset of real self driving car videos pre-labeled by Waymo for research use.

## Our Work

We decided to spend the semester focusing on object detection and segmentation for the camera labels, leaving the 3D and video data for future semesters.

The work is split into four sequential Jupyter Notebooks for the preprocessing, 

Be sure to check it all out and our **Final Presentation**, which can be found here. [ADD LINK]

## Setup <br>

You will need to set up the simple waymo reader and tensorflow object detection githubs which can be found here: <br>

-https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md <br>
-https://github.com/gdlg/simple-waymo-open-dataset-reader <br>


## File Descriptions

**Part 0: Exploratory Data Analysis**

This script takes a first look at the dataset and walks through visualization and file structure for the dataset.

**Part 1: Generate Weather DataSet**

This script preprocesses the dataset by creating a new image folder with images to be used in part 2 based on the weather in the image.

**Part 2: Weather Classifier Competition**

This script shows three seperate CNN model architectures for a binary classifier, and we pit them against each other to find out the best one!

**Part 3: Generating Object Detection API DataSet**

This script preprocesses the dataset to create the tf.Examples dataset used by the Tensorflow Object Detection API. It also saves an image folder with the preprocessed images.





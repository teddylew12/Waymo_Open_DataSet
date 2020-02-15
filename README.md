# Waymo_Open_DataSet
Fall 2019 CAIS++ Project working with the Waymo Open Dataset

In the Fall of 2019, me (Ted Lewitt), Eric Ye and Jack Elliott explored the recently released Waymo Open Dataset,A dataset of real self driving car videos pre-labelled by Waymo for research use.

## Our Work

We decided to spend the semester focusing on object detection and segmentation for the camera labels, leaving the 3D and video data for future semesters.

We first explored the dataset in the *EDA.ipynb* file.

Next we created our own Convolutional Neural Networks (CNNs) for a weather classifier in the *weather_CNN.py* file

Finally, we used transfer learning and a (former) state of the art algorithm called FasterRCNN to perform the 2D segmentation and classification in the *Faster_RCNN.py* file.

## How To Run It

The dataset is huge (1TB), so we won't host it natively. Simply follow the directions in the *data_generation* folder to create the data.

After that, run either *.py* file to replicate our results.

## Final Presentation

Follow this link to see the presentation we gave on this at the CAIS++ Fall Showcase!
ADD LINK


Not on Linux machines so have to use Colab to run it, sucks but it could be worse

Setup:
Have all TFRECORD files downloaded from  in data_generation/tfrecord_files/


Running generate_weather_dataset.ipynb
What it Does:
Takes tdfrecords (using colab) and makes a directory of labelled png files to be used in the weather classifier.
Also makes sure there are an even number of sunny and rainy images.
Saves all the images in data_generation/weather_images.
After running it, you can run the main script, *Weather Classifier Competition.py*


Running generate_fasterrcnn_dataset.ipynb
What it Does

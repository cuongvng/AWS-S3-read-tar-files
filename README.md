# AWS-S3-read-tar-files
This repo contains some utility scripts used for reading files compressed in `tar.gz` on AWS S3.
One potential case is that, if you are familiar with AWS SageMaker, 
after doing a `training job` or `hyperparameter tuning job`, 
you could save your trained model on the temporary directory named `/opt/ml/model`, 
then SageMaker compressed the directory into a `tar.gz` file and save to 
a bucket on S3, and then you need to load a trained model from S3 to 
do some work on your local machine, that is when this repo comes in handy!

Of course, you can manually download the `tar.gz` file, decompress it, 
then read the model file. But for someone lazy (like me :smiley:), 
it is always cool to automate all things!

In my case, as a very example, 
I have a trained `implicit.als.AlternatingLeastSquare` model save in `joblib` format, 
which was then compressed in `tar.gz` file on S3. I will load that compressed model into a Python instance of the class, 
without decompressing it! 
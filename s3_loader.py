import boto3
import tarfile
import joblib

class S3Loader(object):
    AWS_ACCESS_KEY_ID = "<Your_aws_access_key_id>"
    AWS_SECRET_ACCESS_KEY = "<Your_aws_secret_access_key>"
    AWS_REGION_NAME = "<Your_aws_region_name>"
    AWS_STORAGE_BUCKET_NAME = "<Your_aws_bucket_name_on_s3>"

    def __init__(self):
        self.s3_client = boto3.client("s3",
                                     aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                                     aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY)

    def load_tar_file_s3_into_object(self, s3_filepath):
        """
        :param s3_filepath: path to the tar file on your s3 bucket, e.g.
        s3_filepath = "tune-als/output/model.tar.gz"
        :return: the content of the model file that was compressed, as a python object for later use.
        """
        dest = "/tmp/model.tar.gz" # The temporary directory to temporarily save the compressed file

        # Download the file from s3 and save to the destination above
        self.s3_client.download_file(Bucket=self.AWS_STORAGE_BUCKET_NAME, Key=s3_filepath, Filename=dest)

        # Read the trained model from the compressed file into a python object and return it
        tar = tarfile.open(dest, "r:gz")
        model = joblib.load(tar.extractfile(member=tar.getmember(name="model.joblib")))
        return model

if __name__ == "__main__":
    s3_loader = S3Loader()
    model = s3_loader.load_tar_file_s3_into_object(s3_filepath="your_filepath_here.tar.gz")
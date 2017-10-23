import boto3


class S3(object):
    def __init__(self, aws_access_key, aws_secret_access_key):
        self.__s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)

    def upload_file_to_bucket(self, bucket, file_path, key, is_public=False):
        """ Upload files to S3 Bucket """

        with open(file_path, 'rb') as data:
            self.__s3.upload_fileobj(data, bucket, key)

        if is_public:
            self.__s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)

        bucket_location = self.__s3.get_bucket_location(Bucket=bucket)
        file_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location['LocationConstraint'],
            bucket,
            key)

        return file_url

    def download_file_from_bucket(self, bucket, file_path, key):
        """ Download file from S3 Bucket """
        with open(file_path, 'wb') as data:
            self.__s3.download_fileobj(bucket, key, data)
            return file_path

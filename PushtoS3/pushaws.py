import boto
import boto.s3
import sys
from boto.s3.key import Key

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-big-data-project'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "test.csv"
print ('Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name))

k = Key(bucket)
k.key = 'test.csv'
k.set_contents_from_filename(testfile,cb=percent_cb, num_cb=10)

predictfile = "predict.csv"


print ('Uploading %s to Amazon S3 bucket %s' % \
   (predictfile, bucket_name))
   
k = Key(bucket)
k.key = 'predict.csv'
k.set_contents_from_filename(testfile,cb=percent_cb, num_cb=10)


trainfile = "train.csv"

print ('Uploading %s to Amazon S3 bucket %s' % \
   (trainfile, bucket_name))
   
k = Key(bucket)
k.key = 'train.csv'
k.set_contents_from_filename(testfile,cb=percent_cb, num_cb=10)


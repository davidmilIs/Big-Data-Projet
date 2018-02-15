import sys, paramiko
from contextlib import closing

host_ip = "127.0.0.1"
port = 2222
user = "root"
pw = "71313969"

source_train= 'train.csv'
source_test= 'test.csv'
source_predict= 'predict.csv'

dest_train = 'C:\\Users\\Arthur\\Desktop\\train.csv'
dest_test = 'C:\\Users\\Arthur\\Desktop\\test.csv'
dest_predict = 'C:\\Users\\Arthur\\Desktop\\predict.csv'

try:
##SSH Connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host_ip, port=port, username=user, password=pw)
    stdin, stdout, stderr = client.exec_command('hadoop fs -get /tmp/Big_Data_Project/train.csv')
    stdin, stdout, stderr = client.exec_command('hadoop fs -get /tmp/Big_Data_Project/predict.csv')
    stdin, stdout, stderr = client.exec_command('hadoop fs -get /tmp/Big_Data_Project/test.csv')

##SCP Connection
    
    scp = paramiko.Transport((host_ip, port))
    scp.connect(username=user, password=pw)
    sftp = paramiko.SFTPClient.from_transport(scp)
    sftp.get(source_train, dest_train)
    sftp.get(source_predict, dest_predict)
    sftp.get(source_test, dest_test)   

## Erreur
except:
    print("Error")
    
finally:
    client.close()
    scp.close()

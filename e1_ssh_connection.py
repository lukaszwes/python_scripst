# Task 1: Error logs from server
# Connect via SSH (paramiko) to remote host (ip,pw,login)
# from path '/home/ute/Desktop/training/logs/' gather and segregate all
# - error logs files with `error` in filename
#     and
# - dirs that contains errors ending with `_errors`


# A) function should return following output  dict with two attributes
# B) (optional) Download selected error file/files (not dirs!) into local directory
#    as a result files should appear in current working directory

import paramiko

REMOTE_DIR = '/home/ute/Desktop/training/logs/'
PW = 'ute'
LOGIN = 'ute'
IP = '10.42.194.149'



def main():
    result = {}
    files = []
    dirs = []
    
    #copy list of files and dirs
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username=LOGIN, password=PW)
    stdin, stdout, stderr = ssh.exec_command('ls '+REMOTE_DIR)
    opt= stdout.readlines()
    opt = "".join(opt)
    ssh.close()

    list = opt.split('\n')
    for ERR in list:
        if 'error' in ERR:
            if '.' in ERR:
                files.append(REMOTE_DIR+ERR)
            else:
                dirs.append(REMOTE_DIR+ERR)
        

    result = str({
            'dirs'  : dirs,
            'files' : files
         })

    #Formating leyout
    result = result.replace("'dirs'","\n\t'dirs'")
    result = result.replace("[","[\n\t    ")
    result = result.replace("'files'","\n\t'files'")
    result = result.replace("]","\n\t]")
    result = result.replace("}","\n}")
    return result





if __name__ == '__main__':
    print('Result: ', main())
    # print 'Result: ', main() # <-- python 2.7+




'''
EXAMPLE RESULT OUTPUT FOR FOLLOWING FILES/DIRS STRUCTURE
EXAMPLE RESULT OUTPUT FOR FOLLOWING FILES/DIRS STRUCTURE
EXAMPLE RESULT OUTPUT FOR FOLLOWING FILES/DIRS STRUCTURE
...




ute@PLWR5GSISO45E4:/home/ute/Desktop/training/logs$ ls -la

total 16
drwxr-xr-x 4 ute ute 4096 Nov  4 09:26 .
drwxr-xr-x 4 ute ute 4096 Nov  4 09:25 ..
-rw-r--r-- 1 ute ute    0 Nov  4 09:26 20191104_access.log
-rw-r--r-- 1 ute ute    0 Nov  4 09:25 20191104_error.log
-rw-r--r-- 1 ute ute    0 Nov  4 09:26 20191105_access.log
-rw-r--r-- 1 ute ute    0 Nov  4 09:25 20191105_error.log
drwxr-xr-x 2 ute ute 4096 Nov  4 09:25 nginx_errors
drwxr-xr-x 2 ute ute 4096 Nov  4 09:25 rabbit_errors

------  RUNNING SCRIPT


>> python e1_ssh_connection.py



PRODUCES --->

Result: { 
    'dirs': [
    	'/home/ute/Desktop/training/rabbit_errors', 
    	'/home/ute/Desktop/training/nginx_errors' 
    ],   
    'files': [
    	'/home/ute/Desktop/training/20191104_error.log', 
    	'/home/ute/Desktop/training/20191105_error.log'
    ],
} 

'''

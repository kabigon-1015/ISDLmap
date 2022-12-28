import random
import string
# from LAB_SYSTEM import receive
DEBUG=True
USERNAME='1116180073'
PASSWORD='68zZVp2y'
SECRET_KEY="".join([random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&')
                        for i in range(64)])
# DB=receive.U4DB

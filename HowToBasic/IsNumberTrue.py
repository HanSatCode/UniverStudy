from xmlrpc.client import boolean


a = int(input())
if boolean(a) == True :
    print('참입니다.')
else :
    print('거짓입니다.')
name = ('가', '나', '다', '라', '마')
dic = {}

for item in name :
    phone = input(f'{item}의 전화번호를 입력해주세요: ')
    dic[item] = phone

print(dic)
user_name=['bhavani','bhanu','bindu']
user_passward=[123,1234,12345]
name=input('enter the your name:')
if name in user_name:
    passward=int(input('enter the your passward: '))
if passward in user_passward:
    print ('access granted')




name=['bhanu','bhavni','bindu','advika']
passward=[123,1234,12345,123456]
balance=[1000,2000,3000,4000]
def withdraw(current):
    ammount=int(input('enter the amount:'))
    if amount<=balance[current]:
        balance[current]-=amount
        print('succesfully')
    else:print('insufficient funds')
def c_balance(current):
    print('balance is',balance[current])
def default(current):
    print('enter current option')
u_name=input('enter your name:')
for i in range(len(name)):
    if u_name==name[i]:
        u_passward=int(input('enter your passward:'))
        if u_passward==passward[i]:
            while True:
                print('1.withdraw\n2.balance')
                option=int(input('enter your option:'))
                if option==0:
                    break
                data={1:withdraw,2:c_balance}
Exception()
a=10
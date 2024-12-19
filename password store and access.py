passowrds = {
    'Email':'Kannadasatya',
    'blog':'punithlove',
    'luggage':'kannadasatya1234'
}
account = input("Which Account Password you need: ")
if account == 'Email':
    print(passowrds['Email'])
elif account == 'blog':
    print(passowrds['blog'])
elif account == 'luggage':
    print(passowrds['luggage'])
else:
  print("Account Not Found")

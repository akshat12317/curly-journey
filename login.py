import Stud as s
security={'akshat12317':'12345678'}
s.create_table()
print('''application has started''')
while True:
    person = input('1-admin,2-user,3-end')
    if person == '1':
        print('you are logged in as akshat12317')
        password=input('Enter the pasword')
        if password == security['akshat12317']:
            print('welcome')
            admin = input('1-add user,2-display student,3-delete student,4-update student,5-exit')
            if admin=='1':
                id=input('''enter user's id''')
                name = input('''enter the user's name:-''')
                batchcode = input('enter his/her batchcode:-')
                year = input('enter year of joining:-')
                mobile_no = input('enter his/her mobile number:-')
                s.insert_data(id,name,mobile_no,year,batchcode)
            elif admin == '2':
                for i in s.Show():
                    print(i)
            elif admin=='3':
                for j in s.Show():
                    print(j)
                user=input('what user you want to delete tell his/her id-')
                s.delete(user)
            elif admin=='5':
                print('thank you')
                break
            elif admin=='4':
                for k in s.Show():
                    print(k)
                user2=input('''Enter the user's id whose details you want to update:-''')
                name1 = input('''enter the user's name:-''')
                batchcode1 = input('enter his/her batchcode:-')
                year1 = input('enter year of joining:-')
                mobile_no1 = input('enter his/her mobile number:-')
                s.update_by_id(user2,name1,mobile_no1,year1,batchcode1)
    elif person == '3':
        print('Thank you for using')
        break

    elif person == '2':
        print('you are logged in as user')
        user1=input('''Enter the user's id you want to know about-''')
        print(s.fetch_user(user1))

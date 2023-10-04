n=int(input('enter number of members: '))
for person in range(n):
    name=str(input("enter ur name: "))
    age=int(input("enter ur age: "))
    if (age>=18):
        print("eligible")
    else:
        print("not eligible")
        break
    gender=input("enter ur gender: ")
    if gender=='male':
        print('male')
    elif gender=='female':
        print('female')
    else:
        print("Invalid gender type please restart the program.")
        break
    try:
        phonenum=int(input("enter ur phone number: ")) 
        phonenum=phonenum*1
    except Exception:
        print("Invalid credentials")
        print("Please restart the program")
        break
    otp=int(input("enter otp: "))
    aadharnum=int(input("enter aadhar number: "))
    state=input("enter state: ")
    district=input("enter district: ")
    pincode=int(input("enter pincode: "))
    address=input("enter ur address: ")
    print("your registration is complete.\n")

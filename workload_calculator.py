import math

key = 1

def myinput():
    choice = input('Please choose the calculation type：（1-Working Hours，2-Number of People）')
    if choice == '1':
        size = float(input('Please input project size：（1 is standard size，please input float）'))
        number = int(input('Please input the number of people：（please input integer）'))
        time = None
        return size,number,time
       
    if choice == '2':
        size = float(input('Please input project size：（1 is standard size，please input float）'))
        number = None
        time = float(input('Plese input the time：（please input float）'))
        return size,number,time
      
def estimated(my_input):
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]

    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('Project size is %.1fstandard size，to be completed within %.1fhrs，the number of people needed would be：%d人' %(size,time,number)) 
 
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('Project size is %.1fstandard size，%dpeople are working on it，the needed time would be：%.1fhrs' %(size,number,time))  

def again():
    global key
    a = input('Would you like to continue？input y to continue，otherwise quit。')
    if a != 'y':
        key = 0  

def main():
    print('Welcome to use the Workload Calculator！')
    while key == 1:
        my_input = myinput()
        estimated(my_input)
        again()
    print('Thank you for using the Workload Calculator！')

main()

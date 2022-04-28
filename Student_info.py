import csv

def write_into_csv(info):
    with open('student_information.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email-id"])

        writer.writerow(info)


if __name__ == "__main__":
    condition = True
    student_num = 1

    while condition:
        student_info = input("Enter student information for student #{} in the following format (Name Age Contact_Number Email-ID): ".format(student_num))

        stu_info_list = student_info.split(' ')
        print("\nEntered Information is -\nName: {}\nAge: {}\nContact Number: {}\nEmail-id: {}"
              .format(stu_info_list[0], stu_info_list[1], stu_info_list[2], stu_info_list[3]))
        crt_check = input("Is the information correct? ENTER (yes/no): ")
        if crt_check == 'yes':
            write_into_csv(stu_info_list)
            print("Successfully Entered\n")

            check_condition = input("Do you want to enter another student's information? ENTER (yes/no): ")

            if check_condition == 'yes':
                condition = True
                student_num += 1
            elif check_condition == 'no':
                condition = False

        elif crt_check == 'no':
            print("Please Enter the values again!!!")



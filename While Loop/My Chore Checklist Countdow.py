activities=4
print(f"you have {activities} activities to complete")
completed_count=0
activity_num=1
activity_name ="" 

while activity_num<=activities:
    if activity_num==1:
        activity_name= "Make your bed"
    elif activity_num==2:
        activity_name="feed the pet"
    elif activity_num==3:
        activity_name="take out the trash"
    elif activity_num ==4:
        activity_name= "wash the dishes"

    
    answer = input(f"Have you finished: {activity_name}? (yes/no): ")
    if answer == "yes": 
        completed_count = completed_count + 1

        activity_num = activity_num + 1

        print("Great job! Chore completed.")
    else:
        print("Okay, finish it and check again!")
    print("Chores remaining:", activities - completed_count)

    print()


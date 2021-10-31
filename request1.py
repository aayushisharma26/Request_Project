import requests
import json
saral_api = "http://saral.navgurukul.org/api/courses"
getting_data =requests.get(saral_api)
courses_data = getting_data.json()
with open ("all_courses_data.json","w")as mydata:
    json.dump(courses_data,mydata,indent=4)
saral_no=0
saral_courses = courses_data["availableCourses"]
for i in range (len(saral_courses)):
    print(saral_no+1,saral_courses[i]["name"],"id:-",saral_courses[i]["id"])
    saral_no=saral_no+1
user_input=int(input("choose your coursse which you want: "))
print(courses_data["availableCourses"][user_input-1]["name"])
user_id = saral_courses[user_input-1]["id"]

parent_api ="http://saral.navgurukul.org/api/courses/"+str(courses_data["availableCourses"][user_input-1]["id"])+"/exercises"
parents_m=requests.get(parent_api)
data2=parents_m.json()
print(courses_data["availableCourses"][user_input-1]["name"])
with open("parents_data.json","w") as childExercise:
    json.dump(data2,childExercise,indent=4)   
serial_no=1

parents_data = data2["data"]
for i in parents_data:
    print("   ",serial_no ," -",i["name"])  
    serial_no+=1     
    if len(i["childExercises"])>0:
        n=0
        for j in i["childExercises"]:
            n=n+1
            print("          ",n,j["name"])
    else:
        print("              ",i["slug"])   

topic_no=int(input("enter chose your exercise which you want: "))-1
if parents_data[topic_no]["childExercises"]==[]:
    print(topic_no+1,data2["data"][topic_no]["name"])
    print("   ",parents_data[topic_no]["slug"])
else:
    print(topic_no+1,data2["data"][topic_no]["name"])
    s=0
    my_list = []
    while s<len(data2["data"][topic_no]["childExercises"]):
        print("       ",s+1,data2["data"][topic_no]["childExercises"][s]["name"])

        slug = data2["data"][topic_no]["childExercises"][s]["slug"]
        child_api=("http://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercise/getBySlug?slug="+slug)       
        child_data =requests.get(child_api)
        mydata = child_data.json()
        with open ("child_slug_data.json","w")as data:
            json.dump(mydata,data,indent=4)
        data3 = mydata["content"]
        my_list.append(data3)
        s+=1
    questions_no=int(input("do you want to spasiffic question number"))
    question=questions_no-1
    print(my_list[question])
    while questions_no>=0:
        next_question=input("do you next question or previous question n/p:-")
        # if questions_no==len(my_list):
        #     print("next page")
        if next_question=="p":
            if questions_no>=0:
                questions_no=questions_no-1
                
                print(my_list[questions_no])
            else:
                print("page not found: ")
            break    
                   
        elif next_question=="n":
            if questions_no<len(my_list):
                index=questions_no+1       
                print(my_list[index-1])
                question=question+1
                questions_no=questions_no+1 
            else:
                print("no more question in this exercise: ")
        else:
            print("enter right input: ")

            



                 
    


schedule_time =float(input("Enter the schedule time: "))
time1s = 6.30
time1e = 6.40
time2 = 13.00
time3 = 14.00
time4 = 18.30
if schedule_time >= time1s and schedule_time <= time1e:
    print("Aufstehen")
elif schedule_time < time2:
    print("schule")
elif schedule_time >= time2 and schedule_time <= time3:
    print("essen")
elif schedule_time >= time3 and schedule_time <= time4:
    print("Freizeit")
elif schedule_time >= time4:
    print("Judo")


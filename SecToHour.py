# write a program to take second as input and display the number of hours , minute & seconds

tsec=int(input("enter second to convert: "))

hours=tsec//3600
tsec=tsec%3600
mins=tsec//60
secs=tsec%60

print(f"{hours} hours, {mins} minutes & {secs} seconds")

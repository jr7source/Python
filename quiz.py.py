#quiz 

activity = input("How would you spend your evening?\n reading \n partying \n")
print(f"\nyou chose {activity} ")

if activity == "reading":
    print('sounds fun')
elif activity == "partying":
    print('vodka martini?')
else:
    print('wrong choice')


dream_job = input("\nwhats your dream job?\n curator \n business \n")
print(f"\nyou chose {dream_job.upper()} ")

if dream_job == "curator":
    print('intruiguing ')
elif dream_job == "business":
    print('Sounds fun')
else:
    print('wrong choice')

important = input("\nwhats your dream job?\n money \n Love \n")
print(f"\nyou chose {important} ")
if important == "money":
    print('intruiguing ')
elif important == "Love":
    print('Sounds fun')
else:
    print('wrong choice')



decade = input("\nWhat's your favorite decade?\n 1910s \n 2010s \n")
print(f"\nyou chose {decade} ")

if decade == "1910s":
    print('intruiguing ')
elif decade == "2010s":
    print('Sounds fun')
else:
    print('wrong choice')

travel = input("\nWhat's your favorite way to travel?\n Driving \n Flying \n")
print(f"\nyou chose {travel} ")

if travel == "Driving":
    print('intruiguing ')
elif travel == "Flying":
    print('Sounds fun')
else:
    print('wrong choice')

print( f"You chose {activity}, then {dream_job}, then {important}, then {decade}, then {travel}.")

# create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# update scoring variables based on the activity choice
if activity == "reading":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

# update scoring variables based on the job choice
if dream_job == "curator":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the value choice
if important == "money":
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the decade choice
if decade == "1910s":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# update scoring variables based on the travel choice
if travel == "Flying":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

# print the results depending on the score
if sam_like >= 3:
    print( "You're most like Sharp-Eyed Sam!" )
elif cam_like >= 3:
    print( "You're most like Curious Cam!" )
elif kai_like >= 3:
    print( "You're most like Keen Kai!" )
else:
    print( "You're most like Inquisitive Indy!" )




import sched, time
import json

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    dictionary = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("https://raw.githubusercontent.com/izesw/Mist/main/banner.json", "w") as outfile:
        outfile.write(json_object)
    sc.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
import requests, json, datetime


respond1 = requests.post("https://lbasense-hust.appspot.com/data", data={},
                         headers={'type': 'VisitDurations', 'user': 'student-hust', 'pass': '123456a@', 'region': '1',
                                  'startTime': '2016-09-20T00:00:00', 'endTime': '2016-10-10T00:00:00',
                                  'resolution': 'hours'})
print respond1.content


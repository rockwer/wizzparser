import requests
import json


request_url = "https://be.wizzair.com/7.5.2/Api/search/timetable"

head = {'content-type': 'application/json'}

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
#     'path': '/7.5.2/Api/search/timetable',
#     'authority': 'be.wizzair.com',
#     'content-type': 'application/json',
#     'cookie': 'ASP.NET_SessionId=5fmps2oetzbge5qyubgwpawy; ak_bmsc=DA09A276B17E98B06D2869C6D9355167601194041A5300008CD80F5A17ACD105~plPPoQ420Bv9mGe/+GvLdyDFZMGrOOeYBpSXru5Q/TJTOX9ivOZy+byBzPVdijhjROmrB0t6U4nC/qw9A+uPioDgE99K0iqrFFk2ObqsLoXpv/pwsRgjRX1R34dIVz7Qu03gYl61STETB68OkWnfCSCYO5HMQtu33NZZ/MHvF6z5tKhYXWWQHAPOVHwWpHznmyXOKKARrcKHSp7zfYFjSFx2vM6/ZvHIJopbF6PoHh+kM=; bm_sv=596F572CF20263AF8A2D6B8CB908DA67~qFP3ykFhDLR8EmuGr0t8tF1cHxnkGhvdKPL5iGX0u+8RE9jGbknW2seSbsiCmbWrgSDsEg7t9cARFbUCzBQOiIA5TZ78s3bSzswL14waaFrB8VPn6LNQxhhsssaV1MvXN/H8Da8UgM8jIpt5usv92IZuJAbQfzE5jwF6uZk+Z/w=; _ga=GA1.2.1989400728.1510855716; _gid=GA1.2.594641519.1510855716; _gat=1'
# }

payload = {"flightList":[{"departureStation":"IEV","arrivalStation":"BUD","from":"2017-11-18","to":"2017-12-03"},{"departureStation":"BUD","arrivalStation":"IEV","from":"2017-11-27","to":"2017-12-31"}],"priceType":"regular"}

r = requests.post(request_url, headers=head, data=json.dumps(payload))

print(r.content)
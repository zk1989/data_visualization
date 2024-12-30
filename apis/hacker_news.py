import requests
from operator import itemgetter


url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
submission_ids = response.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    rs = requests.get(url)
    rs_dict = rs.json()

    submission_dict = {
        'title': rs_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': rs_dict['descendants']
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

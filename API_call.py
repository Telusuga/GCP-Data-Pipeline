import requests
import json
from google.cloud import storage

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"X-RapidAPI-Key": "32f0bd65ffmshc8b8f556b5bc1f2p158cdbjsn41e9f6e10186",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
x=response.json()


if x['typeMatches'][0]['matchType']=='International':
  print(x['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches'][0]['matchInfo'])
  t=x['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches'][0]['matchInfo']


d={}

d['matchId']=t['matchId']
d['seriesId']=t['seriesId']
d['seriesName']=t['seriesName']
d['matchDesc']=t['matchDesc']
d['matchFormat']=t['matchFormat']
d['startDate']=t['startDate']
d['endDate']=t['endDate']
d['state']=t['state']
d['status']=t['status']

print(d)


with open('test.json','w') as file:
  json.dump(d,file)
  print('file create successful')

bucket_name = "sdk_push"
source_file_path = "/home/javvajisuryateja0305/test.json"
destination_blob_name = "initial.json"  # Optional, keeps the filename

client = storage.Client()
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_path)

#upload_file(bucket_name, source_file_path, destination_blob_name)
print('file transfer successfull')

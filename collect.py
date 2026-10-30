import os,json,datetime,requests,re
from pathlib import Path
key=os.environ['YOUTUBE_API_KEY']; path=Path('data/videos.json')
old=json.loads(path.read_text()); found={v['id']:v for v in old}
queries=['一人暮らし 時短 レシピ shorts','一人前 簡単 料理 shorts','500円以下 節約 レシピ shorts','自炊 15分 料理 shorts']
after=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(days=14)).isoformat().replace('+00:00','Z')
for q in queries:
 p=dict(part='snippet',q=q,type='video',order='date',publishedAfter=after,videoDuration='short',videoEmbeddable='true',maxResults=30,regionCode='JP',relevanceLanguage='ja',key=key)
 try:
  r=requests.get('https://www.googleapis.com/youtube/v3/search',params=p,timeout=30);r.raise_for_status()
 except requests.RequestException as exc:
  status=exc.response.status_code if exc.response is not None else 'network error'
  raise SystemExit(f'YouTube API request failed ({status}). Check API configuration or quota.') from None
 for v in r.json().get('items',[]):
  id=v.get('id',{}).get('videoId');s=v.get('snippet',{});title=s.get('title','');desc=s.get('description','')
  if not id or id in found or not re.search('料理|レシピ|自炊|ごはん|ご飯|飯|丼|パスタ|節約|時短|おかず',title+' '+desc):continue
  found[id]=dict(id=id,platform='youtube',title=title,description=desc,channel=s.get('channelTitle',''),publishedAt=s.get('publishedAt',''),thumbnail=s.get('thumbnails',{}).get('high',{}).get('url',''),url='https://www.youtube.com/watch?v='+id,servings=None,cookMinutes=None,costYen=None,ingredients=[],seasonings=[],verification='unverified')
path.write_text(json.dumps(sorted(found.values(),key=lambda x:x.get('publishedAt',''),reverse=True)[:400],ensure_ascii=False,indent=2)+'\n')

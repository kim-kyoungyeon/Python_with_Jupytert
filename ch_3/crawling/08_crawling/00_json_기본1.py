# import json
# with open ('C:\\book.json')as f:
#     json_data=json.load(f)
# print(json.dumps(json_data))

##################################
import json
file_path= "./sample.json"
data={}
data['posts']=[]
data['posts'].append({
    'title':'how to get storage size',
    'url':'https://codechacha.com/ko/get-free-and-total-size-of-volumes-in-adrodoid/',
    'draft':'false'
})
data['posts'].append({
    'title': 'Android Q, Scoped Stoarge',
    'url': 'https://codechacha.com/ko/android-q-scoped-storage',
    'draft':'false'
})
print(data) #붙어서 나온다

with open(file_path, 'w')as outfile:
    json.dump(data,outfile, indent=3)#indent 공백






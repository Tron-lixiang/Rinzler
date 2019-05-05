import redis
import json
import csv

r=redis.StrictRedis()
data=r.lrange('job',0,-1)

with open('shuju.csv','a+') as f:
        fieldnames = ['岗位名称', '薪资','公司','融资阶段','联系人','要求']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
for i in data:
    expenses=json.loads(i)
    print(expenses)
    with open('shuju.csv','a+') as f:
        fieldnames = ['岗位名称', '薪资','公司','融资阶段','联系人','要求']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(expenses)
        
  

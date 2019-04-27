from uiautomator import Device
from pymongo import MongoClient
client= MongoClient()
database=client.BOSS
collection=database.job
device = Device()

a = 0
b = input("查看多少页:")
b = int(b)
count = b*1

import time
def scroll():
    device(scrollable=True).scroll.vert.forward()
resource_id_dict = {
    '岗位名称':'com.hpbr.bosszhipin:id/tv_position_name',
    '薪资':'com.hpbr.bosszhipin:id/tv_salary_statue',
    '公司':'com.hpbr.bosszhipin:id/tv_company_name',
    '融资阶段':'com.hpbr.bosszhipin:id/tv_stage',
    '联系人':'com.hpbr.bosszhipin:id/tv_employer',
    }
qita_dict={
    'yaoqiu':'1'
    }
def crawl():
    for job in device(className="android.widget.LinearLayout",clickable=True):
        result_dict={}
        job_name = job.child(resourceId='com.hpbr.bosszhipin:id/tv_position_name')
        if not job_name.exists:
            return
        for key,resource_id in resource_id_dict.items():
            value=job.child(resourceId=resource_id)
            if not value.exists:
                return
            result_dict[key] = value.text
        a = job.child(className="android.widget.TextView",index=1)
        result_dict['要求'] = a.text
        print(result_dict)
        collection.insert_one(result_dict)
if __name__=='__main__':
    while True:
        crawl()
        scroll()
        a +=1
        if a==count:
            break

    
    
        

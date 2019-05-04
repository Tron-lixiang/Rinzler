from uiautomator import Device
import json
import redis
device = Device()
r=redis.StrictRedis(host="127.0.0.1",port=6379,db=0)

a = 0
b = input("查看多少页:")
b = int(b)
count = b*1

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
        r.lpush('job',json.dumps(result_dict))  #将字典json序列化后，直接通过lpush存储到redis的job列表中（把序列化的字典，当作一个元素，写入到列表是 思路，原来总想着写入集合）
        data=r.lrange('job',0,-1)[0]            #通过lrange，读取范围（0为第一个元素，-1为最后一个元素，-2为倒数一个元素）的列表，[0]代表列表的第一个元素
        c=json.loads(data)                      #json。load载入读取数据
        print(c)              #本次最大的问题是，第一个坑字典写入redis，原来用mongodb（它自带uid）,而百度相关问题后使用set，每次会覆盖，仅存储一项数据，json未能准确使用也是-致命错误-
if __name__=='__main__':      #导致陷入set，hset，append等遇到各种错误，特别是append后，被网友指导字典转str，str存储，后取出用eval（会报错，eval同时不安全），
    while True:               #最终是 字典转json，直接通过列表，push添加，再通过列表操作range取出，做到写入redis，同时从redis中读取每次列表最左边第一个（最新），完成数据的存储和读取
        crawl()
        scroll()
        a +=1
        if a==count:
            break

   
    
        

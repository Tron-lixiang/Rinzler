from uiautomator import Device
from pymongo import MongoClient
client= MongoClient()
database=client.ZHILIAN
collection=database.job
device = Device()

def scroll():
    device(scrollable=True).scroll.vert.forward()
resource_id_dict = {
    '岗位名称':'com.zhaopin.social:id/position_name',
    '地区':'com.zhaopin.social:id/work_city',
    '薪资':'com.zhaopin.social:id/job_salary',
    '经验要求':'com.zhaopin.social:id/work_exp_value',
    '学历':'com.zhaopin.social:id/education_background',
    '公司':'com.zhaopin.social:id/company_name',
    '发布日期':'com.zhaopin.social:id/publish_time'
    }
def crawl():
    for job in device(className="android.widget.LinearLayout",clickable=True,focusable=False):
        result_dict={}
        job_name = job.child(resourceId='com.zhaopin.social:id/position_name')
        if not job_name.exists:
            return
        for key,resource_id in resource_id_dict.items():
            value=job.child(resourceId=resource_id)
            if not value.exists:
                return
            result_dict[key] = value.text
        print(result_dict)
        collection.insert_one(result_dict)
if __name__=='__main__':
    while True:
        crawl()
        scroll()

import requests
import lxml.html
import re
import csv
#from pandas import DataFrame as pd
source = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=%E7%8E%B0%E4%BB%A3%E5%BC%93%E7%AE%AD').content
selector = lxml.html.fromstring(source)
post_title_list = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
post_editor_list = selector.xpath('//span[@class="frs-author-name-wrap"]/a/text()')
post_time_list = selector.xpath('//div[@class="threadlist_author pull_right"]/span[@class="threadlist_reply_date pull_right j_reply_data"]/text()')
for a in post_title_list:
   print(a)
for b in post_editor_list:
   print(b)
for c in post_time_list:
   c=c.strip()
   print(c)
time_list=[0,0]
for post_time in post_time_list:
   post_time=post_time.strip()
   time_list.append(post_time)
#save=pd({'title':[post_title_list],'editor':[post_editor_list],'time':[post_time_list]})
#save.to_csv("bb.csv",index=False,sep=',')pd未成功使用
with open("tieba.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([post_title_list,post_editor_list,time_list])


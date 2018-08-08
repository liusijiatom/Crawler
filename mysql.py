import pymysql
import json
list1=list()
list2=list()
class MyscrapydemoItem(object):
    def process_item(self, item, spider):
        jsonInfo=json.dumps(dict(item),ensure_ascii=False)
        # personName=jsonInfo.split("\"")[3]
        # personName1=personName.split("-")[0]#电影名
        # musicName=jsonInfo.split("-")[1]
        # musicName1=musicName.split(":")[0]#评分
        personName=jsonInfo.split("\"")[3]
        musicName=jsonInfo.split("\"")[7]
        conn=pymysql.Connect("localhost","root","root","pymydql")
        cur=conn.cursor()
        sql="insert into movies(name,score) values(%s,%s)"
        list1.append(personName)
        list2.append(musicName)
        print(list1)
        print(list2)
        #list1[(len(list1)-1)],list2[(len(list2)-1)],list3[(len(list3)-1)]
        cur.execute(sql,(list1[(len(list1)-1)],list2[(len(list2)-1)]))
        conn.commit()
        print("成功！")
        return item 
    

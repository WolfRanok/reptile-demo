import json
import jsonpath


'''
jsonpath 是一种专业用于json解析的库
'''

with open('dates/学习通.json','r',encoding='GBK') as f:
    obj = json.loads(f.read())

if __name__ == '__main__':
    res = jsonpath.jsonpath(obj,'$.data.lessonArray[?(@.role>3)].className')
    print(res)
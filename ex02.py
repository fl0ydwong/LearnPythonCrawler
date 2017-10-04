import re


def matchBaidutieba():
    with open('got.txt',encoding='utf-8') as f:

        for line in f:
            # 查了一下，python貌似不支持正则嵌套匹配
            user_info = re.findall('<div class=\"l_post.?j_l_post.?l_post_bright.*?data-field=\''
                                '{.*?&quot;user_name&quot;:&quot;(.*?)&quot;,.*?'
                                '&quot;date&quot;:&quot;(.*?)&quot;,.*?\">'
                                '.*?</div>',line,re.S)
            content_list = re.findall('<div .*?d_post_content j_d_post_content  clearfix">(.*?)</div>',line,re.S)

            if len(user_info) != 0 and len(content_list) != 0:
                # 解决了python3 unicode编码问题
                user_name = (user_info[0][0]).encode('utf-8').decode('unicode-escape')
                publish_date = user_info[0][1]
                content = content_list[0]
                print (user_name + ' ' + publish_date+ ' '+ content)


matchBaidutieba()
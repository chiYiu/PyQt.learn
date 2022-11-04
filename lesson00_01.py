# -*- coding: utf-8 -*-
import webbrowser,sys
if len(sys.argv) >1:
	address = "".join(sys.argv[1:])

webbrowser.open('https://map.baidu.com/search/'+address+'/@11585451,3556256.75,12z?querytype=s&da_src=shareurl&wd='+address+'&c=75&src=0&pn=0&sug=0&l=13&b=(11567000,3545298;11609912,3567122)&from=webmap&biz_forward=%7B%22scaler%22:1,%22styles%22:%22pl%22%7D&device_ratio=1')
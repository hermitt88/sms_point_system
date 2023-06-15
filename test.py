from xml.etree.ElementTree import parse

from datetime import datetime

test_file_3days = "sms-20230613211952.xml"
test_file_1day = "sms-20230613213109.xml"
tree = parse(test_file_3days)
root = tree.getroot()

'''실행인력운영협의회 참석 2만 포인트 소진하겠습니다. (최근에 소진/소멸을 하지 않았었음)
'''
# 샘플이 필요

keywords = ["소진", "소멸"]

smss = {}
cnt = 0

for i in root.iter("sms"):
    ts = i.get("date")  # 밀리초 타임스탬프
    text = i.get("body")
    addr = i.get("address")
    flag = 0
    for j in keywords:
        if j in text:
            flag += 1
    if flag:
        print("[[[" + str(ts) + "]]]", text)
for i in root.iter("mms"):
    ts = i.get("date")
    parts = i.find("parts")
    part_iter = parts.iter("part")
    *_, part_last = part_iter
    text = part_last.get("text")

    addrs = i.find("addrs")
    addr_iter = addrs.iter("addr")
    addr_first, *_ = addr_iter
    addr = addr_first.get("address")
    # print(addr)  # type 137 보낸사람 151 받는사람. 137이 내가 아니면 받은 문자인 것이다.

    # flag = 0
    # for j in keywords:
    #     if j in text:
    #         flag += 1
    # if flag:
    #     print("[[[" + str(ts) + "]]]", text)

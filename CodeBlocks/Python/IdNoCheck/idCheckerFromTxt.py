# 判断一个字符串是否是身份证号
# 省份字典
dict = {
    "11": "北京市",
    "12": "天津市",
    "13": "河北省",
    "14": "山西省",
    "15": "内蒙古自治区",
    "21": "辽宁省",
    "22": "吉林省",
    "23": "黑龙江省",
    "31": "上海市",
    "32": "江苏省",
    "33": "浙江省",
    "34": "安徽省",
    "35": "福建省",
    "36": "江西省",
    "37": "山东省",
    "41": "河南省",
    "42": "湖北省",
    "43": "湖南省",
    "44": "广东省",
    "45": "广西壮族自治区",
    "46": "海南省",
    "51": "四川省",
    "52": "贵州省",
    "53": "云南省",
    "54": "西藏自治区",
    "50": "重庆市",
    "61": "陕西省",
    "62": "甘肃省",
    "63": "青海省",
    "64": "宁夏回族自治区",
    "65": "新疆维吾尔自治区",
    "81": "香港特别行政区",
    "82": "澳门特别行政区",
    "83": "台湾省"
}
# 省份序列枚举
pro_list = {
    "11", "12", "13", "14", "15",  # 华北地区
    "21", "22", "23",  # 东北地区
    "31", "32", "33", "34", "35", "36", "37",  # 华东地区
    "41", "42", "43", "44", "45", "46",  # 华南地区
    "50", "51", "52", "53", "54",  # 西南地区
    "61", "62", "63",  # 西北地区
    "81", "82", "83"  # 特别行政区
}
# 月份枚举
mth_list = {"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"}

# 校验位序列
chkstr = "10X98765432"


def func_chk_id_file(cnt, _instr, filepath):
    # 计算权重枚举
    var_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 计算权重枚举迭代器
    it = iter(var_list)
    # filepath = "d:/out.txt"
    wfile = open(filepath, mode='ab+') #追加式写入二进制文件
    #wfile = open(filepath, mode='wb')
    wfile.write(("获取第" + str(cnt + 1) + "个18位身份证号ID:" + _instr + "\n").encode())
    if _instr.__len__() != 18 and _instr.__len__() != 15:
        wfile.write(("长度不正确，是不第二代身份证 :" + _instr.__len__() + "\n").encode())
        wfile.close()
        return False
    if _instr[0:2] not in pro_list:
        wfile.write(("不国内的省市区域" + _instr[0:2] + "\n").encode())
        wfile.close()
        return False
    if _instr[6:10] < "1900" or _instr[6:10] > "2019":
        wfile.write(("出生年份不正确" + _instr[6:10] + "\n").encode())
        wfile.close()
        return False
    if _instr[10:12] not in mth_list:
        wfile.write(("出生月份不正确" + _instr[10:12] + "\n").encode())
        wfile.close()
        return False
    if _instr[12:14] == "00":
        wfile.write(("出生日期不正确" + _instr[12:14] + "\n").encode())
        wfile.close()
        return False
    for key in dict.keys():
        if key == _instr[0:2]:
            wfile.write(("省份==> " + dict[key] + "\n").encode()) #获取字典的键值
            break

    wfile.write(("生日==> " + _instr[6:10] + "年" + _instr[10:12] + "月" + _instr[12:14] + "日" + "\n").encode())

    if int(_instr[14:17]) % 2 == 1:
        wfile.write(("性别==> 男" + "\n").encode())
    else:
        wfile.write(("性别==> 女" + "\n").encode())

    _chk = 0  # 校验位
    count = 0  # 计数器

    for i in _instr:
        if i >= "0" and i <= "9" and count < _instr.__len__() - 1:
            try:
                var = next(it)
                _chk += int(i) * var  # 计算末尾校验系数
                count += 1
            except StopIteration:
                wfile.write("系数计算出错===>".encode())
                wfile.write((" 获取第 " + str(count) + "位，累计系数和=" + str(_chk) + "，本位值=" + str(i) + \
                             "，本位系数=" + str(var) + "\n").encode())
    # 处理末尾校验位
    _chk = _chk % 11
    if _chk == 2:
        wfile.write(("算得校验位= X" + "\n").encode())
    else:
        wfile.write(("算得校验位= " + chkstr[_chk] + "\n").encode())

    if _instr[17] == chkstr[_chk]:
        wfile.write(("输入校验位= " + _instr[17] + "，一致，校验位序号=" + str(_chk) + "\n").encode())
        wfile.write(("合法的身份证：" + _instr + "\n\n").encode())
        wfile.close()
        return True
    else:
        wfile.write(("ERR==>输入的证件号不存在" + "\n\n").encode())
        wfile.close()
        return False


# main function
if __name__ == '__main__':
    # 证件初始值
    file = "d:/id.txt"
    # 读取文件
    # rfile=open(file, mode='br', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    rfile = open(file, mode='r')

    # with open('/path/to/file', 'r') as rfile:
    ids_list = rfile.readlines()
    rfile.close()
    id_list=list(set(ids_list)) #使用set集合去重
    #print("读取证件"+id_list)

    wrfile = "d:/out.txt"
    # 循环之前先清空文件
    wf = open(wrfile, mode='wb')
    wf.write("".encode())
    wf.close()
    #循环写入文件
    for i in range(0, len(id_list)):
        id_list[i] = id_list[i].strip('\n')  # 处理掉末尾的\n
        idstr = id_list[i]
        print("读取第"+str(i+1).zfill(4)+"个二代身份证号："+idstr) #填充字符长度为4 ，左侧补零
        try:
            func_chk_id_file(i, idstr, wrfile)
        except StopIteration:
            print("call function failed")
    exit(0)

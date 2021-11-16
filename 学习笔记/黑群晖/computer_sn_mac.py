import random

k = random.randint(-20,48)               #引入随机变量

print("当前的变量为：",k)

sn0 = int("1140")                       #将基础的sn,不包含设备号和尾号
sn_new = sn0 + 11 * k
sn_new_4 = str(sn_new).zfill(4)         #将获得的sn变为4位数
sn = "1780PDN" + str(sn_new_4) + "01"   #输出16进制的sn

print("当前生成的SN为：",sn)


mac0 = int("9D", 16)                  #将基础的mac转换为10进制，不包含设备号和尾号
mac_new = mac0 + 2 * k
mac1 = "0011327B0C" + str.upper(format(mac_new,"x"))     #输出16进制的第一个mac
mac2 = "0011327B0C" + str.upper(format(mac_new+1,"x"))

print("当前生成的MAC1为：",mac1)
print("当前生成的MAC2为：",mac2)
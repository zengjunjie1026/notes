(6) 路由器防火墙设置，在【网络】→【防火墙】→【自定义规则】中添加如下规则，【重启防火墙】：
iptables -I FORWARD -i ztyqbub6jp -j ACCEPT
iptables -I FORWARD -o ztyqbub6jp -j ACCEPT
iptables -t nat -I POSTROUTING -o ztyqbub6jp -j MASQUERADE
其中的“ztyqbub6jp”在不同的路由器中不一样，你可以在路由器ssh环境中用zerotier-cli listnetworks查询。
(7)如此设置后在192.168.11.1路由器下的设备可以以192.168.191.206或192.168.12.1访问另外一台路由器，同时可以192.168.12.X访问192.168.12.1路由器下的其它设备；反之亦然。
3、应用场景：
(1) 可以远程登录管理路由器了
(2) 可以将群晖nas与其它设备组成内网，文件同步再也不看quickconnect的龟速眼神了
(3) 两端的linux设备都可以远程ssh登录配置了
(4) 两端的windows设备可以用微软自带的远程桌面功能了（先在【计算机】→【属性】→【系统】→【远程设置】中允许远程桌面连接，再在控制端允许窗口输入MSRSC运行远程桌面连接，输入用户名、密码即可像本地计算机一样操控远程计算机了），其速度杠杠的（除了握手阶段需要zerotier中心服务器牵手之外，其余时间都是UDP直连，取决于两端的上传速度）
(5) ……有待读者发掘并分享
4、关于速度，前面已经说了，UDP直连，仅握手阶段需要中心服务器，同时官方还给出了让用户自行在有固网ip的机器上搭建moon卫星级服务器，供带组建内网的其它设备握手使用以提高握手速度和稳定性，感兴趣和有条件的朋友可以去探索和折腾了。
四、后记
1、注意客户端安装、配置zerotier和官网管理中心添加许可、添加路由表的顺序以及ip对应设置情况，万一哪一步操作错误导致设备不能上网的话，可以用zerotier-cli leave ID先让该不能上网的设备断开与zerotier服务器的连接，再重新join和在官网管理中心添加许可、添加路由表。
2、由于我的openwrt软路由之前安装了entware，导致opkg install zerotier是在entware源而非openwrt源，且安装路径也是这样外接磁盘而非路由器内储存，导致无法正常运行，于是我只好在/etc/rc.local配置文件中将自动加载entware的相关设置注释掉，并将/etc/profile中为entware添加的. /opt/etc/profile注释掉就可以正常安装和运行了。

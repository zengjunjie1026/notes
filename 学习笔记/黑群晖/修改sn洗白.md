四、挂载synoboot1分区
1.在“/tmp”目录下创建一个临时目录，目录名称为"boot"：

mkdir -p /tmp/boot
2.切换到“/dev”目录：

cd /dev
3.把"synoboot1"分区挂载到“/tmp/boot”目录：

mount -t vfat synoboot1 /tmp/boot/

vim /tmp/boot/grub/grub.cfg

```shell
当前生成的SN为： 1780PDN155801
当前生成的MAC1为： 0011327B0CE9
```
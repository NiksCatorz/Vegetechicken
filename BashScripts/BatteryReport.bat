@echo off
@echo 正在准备生成随机电池报告！
set lodir=%date:~0,4%%date:~5,2%%date:~8,2%
@echo 截止日期 %lodir%
mkdir D:\BatteryReport\
D:
cd D:\BatteryReport\
powercfg /batteryreport /output "BatteryReport%lodir%.html"
@echo 生成报告完毕，生产文件为"BatteryReport%lodir%.html"
pause
exit
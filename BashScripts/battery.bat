@echo off
@echo ����׼�����������ر��棡
set lodir=%date:~0,4%%date:~5,2%%date:~8,2%
@echo ��ֹ���� %lodir%
mkdir D:\BatteryReport\
D:
cd D:\BatteryReport\
powercfg /batteryreport /output "BatteryReport%lodir%.html"
@echo ���ɱ�����ϣ������ļ�Ϊ"BatteryReport%lodir%.html"
pause
exit
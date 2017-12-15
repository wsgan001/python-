echo "正在安装Apache24";
::作用：以管理员身份安装Apache 说明：在 windows10 x64下工作正常
d:
cd %~dp0\
python manage.py migrate chatroom
pause
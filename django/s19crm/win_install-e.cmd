echo "运行服务器";
::作用：以管理员身份安装Apache 说明：在 windows10 x64下工作正常
e:
cd %~dp0\
python manage.py runserver 0.0.0.0:8000
pause                                                  
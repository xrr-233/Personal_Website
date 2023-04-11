+ 2023/04/11

采用gitbook博客样式，颜值更加高

修复时钟无法缩放问题

采用多种新式vue路由写法（watch、props等）

+ 2023/02/14

给予网站域名

完成单页面（博客/公告）切换主体功能

增加推荐音乐单

+ 2023/01/17

初步完成单页面（博客/公告）切换

+ 2023/01/16

加入传送门功能

+ 2022/12/29

修复博客图片超出问题

加入统计访客功能

+ 2022/12/25

修复了一些display小bug

日志移植进网站，以后不在github readme中显示

+ 2022/12/23

由于旧服务器过期，将所有配置移到新服务器

（顺便，一直看着不爽的）播放音乐的坑终于填啦！有音乐的个人网站才是正宗的个人网站！

日志改天再移

+ 2022/12/11

实现png图片的作品展示（暂未实现从客户端上传以及jpg）

+ 2022/12/09

新增公告栏功能（初步）

未来工作：公告栏页面的跳转

优先工作：作品展示/日志转移

+ 2022/06/13

实现博客文章删除并修复时钟错位，等待部署

部署操作：

Vue前端：

npm run build

将dist文件夹内所有文件拷贝到'/var/www/html'

按照https://zhuanlan.zhihu.com/p/103244419所示配置nginx

Flask后端：

gunicorn -D -w 1 -b 0.0.0.0:5000 app:app

重要：由于最终没有选择将博客内容推至服务器中，从今以后请确保每次push之前先将服务器中博客文档push妥善

+ 2022/06/04

完成发布博客功能开发。下一阶段欲实现博客文章删除功能，之后网站就应可以正式启用（不考虑其他坑要填的话）

+ 2022/06/03

正在进行发布博客开发，能够后端获取文件，但前端仍残留 "Cannot post /" bug

+ 2022/06/02

1. 修复了personal页面position导致的覆盖无法点击bug（残留左边栏长度跟着变的细节bug）

2. 完成了personal页面修改密码的前后端大部分功能

+ 2022/05/21

感谢尚硅谷的老师 https://www.bilibili.com/video/BV1Zy4y1K7SH?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click

知道了vue-router的整体框架以及使用JWT token保存用户登录数据的方法

https://blog.csdn.net/qq_29272181/article/details/121190778

https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html

https://myapollo.com.tw/zh-tw/python-json-web-token/

（目前残留登录后modal无法收回的bug）

+ 2022/05/20

提供项目参考 https://www.cnblogs.com/donghaoblogs/p/10523983.html

路径中的#代表哈希模式hash，历史模式history虽好看但需要后端工作解决history 404问题

+ 2022/05/18

采用新时钟样式 https://github.com/SlyTy7/clock

已经较为系统化地掌握了Vue模块的开发，以及通过axios实现的vue前端与flask后端（api与数据库）的交互

+ 2022/05/17

经过慎重斟酌，为使项目框架更加规范，欲参考https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ 的描述，进行vue+flask混合的前后端分离开发，废弃jinja模板

+ 2022/04/15

正确的Flask+Vue框架整合：

https://juejin.cn/post/6909732949378203662

+ 2022/04/14

尝试vue模块化部分代码

https://learnku.com/python/t/24985

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

https://zhuanlan.zhihu.com/p/101544546

运行vue-cli:

cd client

npm run serve

+ 2022/04/13

修复了bootstrap图标显示bug（更换为emoji）

追加博客主页显示功能

+ 2022/03/12

补充：gunicorn重启：killall -9 gunicorn

允许以POST方式上传博客markdown文件（但尚未将博客在首页显示）

增加SystemStatus表以追踪博客数以及命名规范

待开发：提交博客表单后的反馈信息及动作

+ 2022/01/22

个人中心网页初步开发，以允许博客上传

通过jquery.on实现标签切换，开发修改密码界面充当占位符（暂无功能）

+ 2022/01/16

测试博客插件marked

+ 2022/01/13

移植数据库，创建账号

通过bootstrap（主要是modal）和ajax与flask结合成功完成登录模块开发

+ 2022/01/10

选择使用gunicorn和nginx将网站挂上

gunicorn -D -w 1 -b 127.0.0.1:5000 app:app

参考文章：

https://zhuanlan.zhihu.com/p/92003835

https://www.cnblogs.com/homeworknotes/p/11219902.html

+ 2022/01/08

舍弃旧有的flask-script，改用flask.cli表示方法来连结flask-migrate
***
>参考书籍:   
 Flask Web开发

##1.一些过时的模块或者类的处理
***
### flask_script
>原来的版本
`
  from flask.ext.script import Manager
`

>现在的版本
`
  from flask_script import Manager
`
***  



### flask_bootstrap
>原来的版本
`
  from flask.ext.bootstrap import Bootstrap
`

>现在的版本
`
  from flask_bootstrap import Bootstrap
`
***

### flask_moment
>原来的版本
`
  from flask.ext.moment import Moment
`

>现在的版本
`
  from flask_moment import Moment
`
***
### flask_WTF
>原来的版本
`
  from flask.ext.wtf import Form
`

>现在的版本
`
  from flask_wtf import Form
`
***  
### Required

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/5513300-f686da5c5d71afa2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
使用DataRequired代替

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/5513300-075358041e5ae151.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##2.数据库迁移操作
***
在Termial中操作
>init子命令创建迁移仓库
`
  python FlaskyWeb.py db init
`

>创建迁移脚本
`
  python FlaskyWeb.py migrate -m "initial migration"
`

>更新数据库
`
  python FlaskyWeb.py db upgrade
`

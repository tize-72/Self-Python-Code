#### 1.首先在自己的电脑上打开git生成密钥

```
git config --global user.name "yangjianliang"
配置用户名
git config --global user.email "526861348@qq.com"
配置邮箱

ssh-keygen -t rsa -C "526861348@qq.com"
注意一下这里的邮箱是自己刚刚设置的邮箱
```

#### 2.然后打开linke申请服务器的网址

http://jump.linkedc.ml/linkelife/

进入之后

<img src="/Users/tize-72/Desktop/picture/截屏2021-10-13 13.30.21.png" style="zoom: 50%;" />

点击这个服务器使用申请

里边会有一个地方需要输入自己的公钥，这个公钥已经在上一步中生成过

#### 3.查看自己的公钥

windows系统中查看自己的公钥就是

C盘—>用户—>账户—> .ssh文件中的 **id_rsa.pub** 文件

打开这个文件，将内容复制下就行

mac系统中查看公钥就是在git下输入以下命令

```
cat ~/.ssh/id_rsa.pub
```

#### 4.提交申请

最后提交申请就可以了
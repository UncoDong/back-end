## back-end(后端部分)

[![前端代码库](https://img.shields.io/badge/前端-王相杰-91d5ff)](https://github.com/Asa-kura/note)[![后端代码仓库](https://img.shields.io/badge/后端-董安宁-1890ff)](https://github.com/UncoDong/back-end)[![算法代码仓库](https://img.shields.io/badge/算法-张淇金-2f54eb)](https://github.com/UncoDong/Music-Attention-pytorch-onlycode)[![测试代码仓库](https://img.shields.io/badge/测试-董安宁-061178)](https://github.com/UncoDong/TAPD-test)

### 逻辑结构

#### MusicBackEnd

主工程，用来链接所有Myapp打头的子工程

##### Myapp_convert2musicscore

核心算法工程，提供**字符串转换乐谱**和**音频文件转换乐谱**的功能函数。生成的**MusicXML**，**MID文件**也都保存在这里。

##### Myapp_dealfile

处理文件相关的工程。用来实现文件的**上传**和**下载**功能。以及调用Myapp_convert2musicscore中的转换函数对文件进行处理。

##### Myapp_login

登录功能相关的工程。用来实现用户的**登录**，**登出**，**保持登陆状态**，**注册**等功能。

##### Myaoo_runweb

页面展示相关的功能，用来将html网页返回给用户。所有的JSP文件和CSS文件都保存在这里。




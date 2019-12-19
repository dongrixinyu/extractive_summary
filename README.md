# extractive_summarization

一个从 **中文自然语言文本**  中抽取 **文本摘要** 的工具  
A tool for **summary extraction automatically** from **Chinese natural language** text.

- 该文本摘要抽取算法基于 LDA 主题模型，结合 tfidf 统计信息，Lead-3 权重，使用 MMR 作为抽取准则。
- 基于北大分词器 pkuseg 工具，它性能较高，准确度也较高。  

## 使用方法 Usage

#### 安装 Installation
- 仅支持 python3  
- 自动安装 pkuseg 依赖包   
- python3 only supported  
- Automatic installation of pkuseg dependency package  


```
$ git clone https://github.com/dongrixinyu/extractive_summary
$ cd ~/extractive_summary
$ pip install .
```


#### 示例代码 Sample code 

- 输入必须为 **utf-8** 编码字符串  
- 具体函数参数见代码  
- Input must be **utf-8** encoding string  
- See code for specific function parameters  


```
import ckpe    

ckpe_obj = ckpe.ckpe()
# 初次导入时会自动下载北大词性标注模型包，自动加载入内存（50M）  
# 若由于网速原因下载失败，请参考 https://github.com/lancopku/pkuseg-python 如何安装下载 pkuseg 默认模型  
# Speech Tagging Model Package of pkyseg will be downloaded automatically upon initial import  
# If downloading fails due to network speed, please refer to how to install and download pkuseg default model in https://github.com/lancopku/pkuseg-python  

text = '法国媒体最新披露，巴黎圣母院火灾当晚，第一次消防警报响起时，负责查验的保安找错了位置，因而可能贻误了救火的最佳时机。据法国BFMTV电视台报道，4月15日晚，巴黎圣>母院起火之初，教堂内的烟雾报警器两次示警。当晚18时20分，值班人员响应警报前往电脑指示地点查看，但没有发现火情。20分钟后，警报再次响起，保安赶到教堂顶部确认起火。然而为时>已晚，火势已迅速蔓延开来。报道援引火因调查知情者的话说，18时20分首次报警时，监控系统侦测到的失火位置准确无误。当时没有发生电脑故障，而是负责现场查验的工作人员走错了地方>，因而属于人为失误。报道称，究竟是人机沟通出错，还是电脑系统指示有误，亦或是工作人员对机器提示理解不当？事发当时的具体情形尚待调查确认，以厘清责任归属。该台还证实了此前>法媒的另一项爆料：调查人员在巴黎圣母院顶部施工工地上找到了7个烟头，但并未得出乱扔烟头引发火灾的结论。截至目前，警方尚未排除其它可能性。大火发生当天（15日）晚上，巴黎检察
summary = cse_obj.extract_summary(text)
print(summary)
summary = '法国媒体最新披露，巴黎圣母院火灾当晚，第一次消防警报响起时，负责查验的保安找错了位置，因而可能贻误了救火的最佳时机。据法国BFMTV电视台报道，4月15日晚，巴黎圣母院起火之初，教堂内的烟雾报警器两次示警。当晚18时20分，值班人员响应警报前往电脑指示地点查看，但没有发现火情。参与圣母院顶部翻修施工的工人、施工方企业负责人以及圣 母院保安等30余人相继接受警方问话。'
print(cse_obj.extract_summary.__doc__)
```

## 原理 Principle of algorithm

- 首先基于 pkuseg 工具做分词和词性标注，再使用 tfidf 计算文本的关键词权重，  
- 关键词提取算法找出碎片化的关键词，然后再根据相邻关键碎片词进行融合，重新计算权重，去除相似词汇。得到的融合的多个关键碎片即为关键短语。  
    - 短语的 token 长度不超过 12  
    - 短语中不可出现超过1个虚词  
    - 短语的两端 token 不可是虚词和停用词  
    - 短语中停用词数量不可以超过规定个数  
    - 短语重复度计算添加其中  
    - 提供仅抽取名词短语功能  
- 使用预训练好的 LDA 模型，计算文本的主题概率分布，以及每一个候选短语的主题概率分布，得到最终权重  
- Firstly do word segmentation and part of speech tagging based on pkuseg tool, then use word level tfidf to calculate the keyword weight of the text.  
- Fuse the adjacent key fragment words, recalculates the weights, and removes the similar words. The fused key fragments are candidate keyphrases. Rules include:  
    - Token length of phrase can not exceed 20  
    - There cannot be more than one function word in a phrase  
    - The token at both ends of the phrase should not be the function word and stop words  
    - The number of stopwords in a phrase cannot exceed the specified number  
    - Phrase repetition calculation is added  
    - Provide only noun phrases extraction parameters  
- Calculating the topic probability distribution of the text and the topic probability distribution of each candidate phrase by using the pre-trained LDA model to obtain the final weight  

## TODO
- pkuseg 分词器造成的错误
- 句子信息压缩、裁剪，句子连贯性较差的问题

## 我的窝 My blog  

如果觉得方便好用，请 follow 我一波：https://github.com/dongrixinyu  
If you feel this tool convenient and easy to use, please follow me: https://github.com/dongrixinyu


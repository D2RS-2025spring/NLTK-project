# NLTK-project
# 文本智能分析系统项目

## 项目名称
文本智能分析系统（Text Intelligence Analysis System）

## 项目成员及分工
| 成员             | 分工                              |
|------------------|-----------------------------------|
| 马跃2024303110021 |架构设计、 前后端实现、NLP算法集成与优化、代码整合|
| 姚洁2024303120069 | 需求分析、前端实现|
| 顾瑞莹2024303110020 | 架构设计、前端实现|
| 岳璐璐2024303120074 | 架构设计、前端实现|

## 项目架构
```
NLTK-project/
├── nltk-analyer.py          # 核心代码模块
├── data/                    # 停用词以及知网HowNet情感词典
└── fonts/                   # 字体
```
### 系统分层设计
```mermaid
graph TD
    A[用户界面层] --> B[应用逻辑层]
    B --> C[服务层]
    C --> D[数据层]
    
    A --> |Flask路由| B
    B --> |文本处理流水线| C
    C --> |词典/缓存| D
```
### 模块结构
```mermaid
graph LR
    WEB[前端模块] --> |API调用| API[后端接口]
    API --> NLP[NLP处理模块]
    NLP --> FETCH[网页抓取模块]
    NLP --> VIZ[可视化模块]
```
## 项目技术路线
### 核心技术栈
```mermaid
pie
    title 技术栈分布
    "Python Flask" : 35
    "Jieba分词" : 20
    "BeautifulSoup" : 15
    "Bootstrap 5" : 20
    "WordCloud" : 10
```
### 处理流水线
```mermaid
flowchart TB
    A[用户输入] --> B{输入类型}
    B -->|URL| C[网页内容抓取]
    B -->|文本| D[原始文本处理]
    C --> E[HTML清洗]
    D --> E
    E --> F[中文分词]
    F --> G[停用词过滤]
    G --> H[情感分析]
    G --> I[摘要生成]
    G --> J[关键词提取]
    H --> K[可视化渲染]
    I --> K
    J --> K
    K --> L[结果展示]
```
## 项目实现
### 核心功能模块
 1. 网页采集模块
 2. 文本处理流水线
 3. 情感分析引擎
### 创新特性
 1. 交互式词云系统
 2. 动态进度反馈
 3. 响应式统计卡片
### 性能优化策略
```mermaid
graph LR
    A[预加载词典] --> B[减少IO操作]
    C[内存流处理] --> D[词云Base64生成]
    E[分词缓存] --> F[提升重复分析速度]
    G[异步任务] --> H[提高并发能力]
```
## 技术亮点
1. ​​自适应内容提取​​

* 支持解析主流新闻网站结构
* 智能降级机制保障内容获取

2. ​​多词典情感分析
```mermaid
flowchart LR
    D1[默认词典] --> M[词典合并模块]
    D2[知网HowNet词典] --> M
    M --> S[情感分析引擎]
```
## 总结
### 项目优势
```mermaid
mindmap
  root((系统优势))
      技术整合
          NLP算法集成
          Web框架融合
      用户体验
         可视化展示
         交互功能
      性能表现
         实时响应
         资源优化
```
## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/Gmyue/NLTK-project.git

# 安装依赖
pip install -r requirements.txt

# 运行文本分析
python main/news_analyzer.py
```

#### 本地部署默认网址: http://127.0.0.1:5000


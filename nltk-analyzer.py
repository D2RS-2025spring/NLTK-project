# -*- coding: utf-8 -*-
# @File  : news_analyzer.py
# @Author: 马跃2024303110021
# @Date  : 2025/01/03/21:15

import os
import requests
from bs4 import BeautifulSoup
import re
import jieba
import jieba.analyse
from collections import Counter
from flask import Flask, request, render_template_string, make_response
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')  # 在导入pyplot之前设置
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from io import BytesIO
import base64


app = Flask(__name__)

STOPWORDS_PATH = "./data/stopword.txt"#停用词位置
EXTERNAL_SENTIMENT_DICT_PATH = './data/emotion.txt'  # 词典路径

# 全局样式定义
CSS_STYLE = '''
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>
    /* 主题色定义 */
    :root {
        --primary-color: #4361ee;
        --secondary-color: #3f37c9;
        --accent-color: #4895ef;
        --success-color: #4cc9f0;
        --text-dark: #2b2d42;
        --text-light: #8d99ae;
        --bg-light: #f8f9fa;
        --card-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    }

    body {
        font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
        line-height: 1.6;
        background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
        color: var(--text-dark);
        min-height: 100vh;
    }

    .app-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    /* 导航栏优化 */
    .navbar {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        box-shadow: 0 4px 20px rgba(67, 97, 238, 0.3);
        padding: 0.8rem 1rem;
    }

    .navbar-brand {
        font-weight: 700;
        font-size: 1.5rem;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
    }

    .navbar-brand i {
        font-size: 1.8rem;
        margin-right: 12px;
        background: rgba(255, 255, 255, 0.2);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* 卡片设计优化 */
    .card {
        border-radius: 16px;
        box-shadow: var(--card-shadow);
        border: none;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 25px;
        background: rgba(255, 255, 255, 0.95);
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }

    .card-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
        color: white;
        font-weight: 600;
        font-size: 1.25rem;
        padding: 1.2rem 1.5rem;
        border-bottom: none;
    }

    .card-body {
        padding: 1.8rem;
    }

    /* 按钮优化 */
    .btn-primary {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        border: none;
        border-radius: 50px;
        padding: 10px 25px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(67, 97, 238, 0.3);
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background: linear-gradient(135deg, #3a56d4 0%, #3830b0 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(67, 97, 238, 0.4);
    }

    .btn-outline-primary {
        border-color: var(--primary-color);
        color: var(--primary-color);
        border-radius: 50px;
        font-weight: 500;
    }

    .btn-outline-primary:hover {
        background: var(--primary-color);
        color: white;
    }

    /* 表单优化 */
    .form-control {
        border-radius: 12px;
        padding: 12px 20px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }

    .form-control:focus {
        border-color: var(--accent-color);
        box-shadow: 0 0 0 3px rgba(72, 149, 239, 0.2);
    }

    .input-group-lg > .form-control {
        border-radius: 50px 0 0 50px;
        padding: 15px 25px;
    }

    .input-group-lg > .btn {
        border-radius: 0 50px 50px 0;
        padding: 15px 30px;
    }

    textarea.form-control {
        min-height: 150px;
        border-radius: 16px;
    }

    /* 标签页优化 */
    .nav-tabs {
        border-bottom: 2px solid #e9ecef;
        margin-bottom: 1.5rem;
    }

    .nav-tabs .nav-link {
        border: none;
        border-radius: 8px 8px 0 0;
        padding: 12px 20px;
        color: var(--text-light);
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .nav-tabs .nav-link.active {
        color: var(--primary-color);
        background: transparent;
        border-bottom: 3px solid var(--primary-color);
        font-weight: 600;
    }

    .nav-tabs .nav-link:hover:not(.active) {
        color: var(--primary-color);
        background: rgba(67, 97, 238, 0.05);
    }

    /* 分析结果区域优化 */
    .result-item {
        margin: 20px 0;
        padding: 20px;
        border-left: 4px solid var(--primary-color);
        background: rgba(67, 97, 238, 0.03);
        border-radius: 0 12px 12px 0;
        transition: all 0.3s ease;
    }

    .result-item:hover {
        background: rgba(67, 97, 238, 0.07);
        transform: translateX(5px);
    }

    .analysis-section {
        margin-top: 30px;
        padding: 25px;
        background: white;
        border-radius: 16px;
        box-shadow: var(--card-shadow);
    }

    .stat-card {
        text-align: center;
        padding: 20px 15px;
        border-radius: 12px;
        background: rgba(76, 201, 240, 0.1);
        transition: all 0.3s ease;
        height: 100%;
    }

    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(76, 201, 240, 0.2);
    }

    .stat-card h6 {
        color: var(--primary-color);
        font-weight: 600;
        margin-bottom: 10px;
    }

    .stat-card .value {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--secondary-color);
        line-height: 1.2;
    }

    .stat-card .unit {
        font-size: 1rem;
        color: var(--text-light);
        font-weight: 500;
    }

    /* 词云优化 */
    .word-cloud {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        padding: 20px;
        background: var(--bg-light);
        border-radius: 16px;
        justify-content: center;
    }

    .word-item {
        padding: 8px 16px;
        border-radius: 50px;
        background: white;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        font-weight: 500;
        cursor: pointer;
    }

    .word-item:hover {
        background: var(--primary-color);
        color: white;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
    }

    /* 情感标签优化 */
    .sentiment-tag {
        display: inline-flex;
        align-items: center;
        padding: 6px 15px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
    }

    .sentiment-positive {
        background: rgba(40, 167, 69, 0.15);
        color: #28a745;
    }

    .sentiment-negative {
        background: rgba(220, 53, 69, 0.15);
        color: #dc3545;
    }

    .sentiment-neutral {
        background: rgba(108, 117, 125, 0.15);
        color: #6c757d;
    }

    /* 加载动画 */
    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    .loading-spinner {
        display: inline-block;
        width: 24px;
        height: 24px;
        border: 3px solid rgba(255, 255, 255, 0.3);
        border-top-color: white;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        vertical-align: middle;
        margin-left: 10px;
    }

    /* 页脚 */
    .footer {
        text-align: center;
        padding: 30px 0;
        color: var(--text-light);
        font-size: 0.9rem;
        margin-top: 40px;
    }

    /* 响应式调整 */
    @media (max-width: 768px) {
        .app-container {
            padding: 15px;
        }
        
        .card-body {
            padding: 1.2rem;
        }
        
        .input-group-lg > .form-control {
            border-radius: 50px;
            margin-bottom: 10px;
        }
        
        .input-group-lg > .btn {
            border-radius: 50px;
            width: 100%;
        }
    }
    /* 在现有的 CSS_STYLE 中添加 */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate__animated {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
}

.animate__slower {
    -webkit-animation-duration: 1.5s;
    animation-duration: 1.5s;
}

.animate__fadeIn {
    -webkit-animation-name: fadeIn;
    animation-name: fadeIn;
}
.app-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 30px 20px;
    background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
    border-radius: 24px;
    box-shadow: 0 15px 50px rgba(67, 97, 238, 0.15);
    margin-top: 20px;
    margin-bottom: 40px;
}



/* 2. 卡片设计增强 */
.card {
    border-radius: 20px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(67, 97, 238, 0.1);
}

.card-header {
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    padding: 1.5rem 2rem;
}

/* 3. 按钮美化增强 */
.btn-primary {
    background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
    box-shadow: 0 6px 20px rgba(67, 97, 238, 0.4);
    position: relative;
    overflow: hidden;
}

.btn-primary::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: rgba(255, 255, 255, 0.2);
    transform: rotate(30deg);
    transition: all 0.6s ease;
}

.btn-primary:hover::after {
    transform: translateX(100%) rotate(30deg);
}

/* 4. 输入框美化 */
.form-control {
    border: 1px solid #e0e7ff;
    background: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.05);
}

.form-control:focus {
    background: white;
    box-shadow: 0 0 0 4px rgba(67, 97, 238, 0.15), inset 0 2px 5px rgba(0, 0, 0, 0.05);
}

/* 5. 选项卡增强 */
.nav-tabs {
    border-bottom: 2px solid #e9ecef;
    margin-bottom: 1.8rem;
}

.nav-tabs .nav-link {
    border-radius: 12px 12px 0 0;
    padding: 14px 24px;
    font-size: 1.05rem;
    position: relative;
    overflow: hidden;
}

.nav-tabs .nav-link::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 4px;
    background: var(--primary-color);
    transition: width 0.4s ease;
}

.nav-tabs .nav-link.active::before {
    width: 100%;
}

/* 6. 词云容器美化 */
.word-cloud-container {
    background: linear-gradient(135deg, #f8f9ff 0%, #edf2ff 100%);
    border-radius: 18px;
    padding: 25px;
    border: 1px solid rgba(67, 97, 238, 0.1);
    box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.03);
    margin: 20px 0;
}

/* 7. 动画效果增强 */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.animate-float {
    animation: float 4s ease-in-out infinite;
}

.animate-pulse {
    animation: pulse 2s ease-in-out infinite;
}

/* 8. 结果卡片悬停效果 */
.result-card {
    transition: all 0.4s ease;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    height: 100%;
}

.result-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(67, 97, 238, 0.2);
}

/* 9. 情感标签美化 */
.sentiment-tag {
    padding: 8px 18px;
    border-radius: 50px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    font-size: 0.95rem;
}

.sentiment-positive {
    background: linear-gradient(135deg, rgba(40, 167, 69, 0.15) 0%, rgba(40, 167, 69, 0.25) 100%);
    color: #28a745;
}

.sentiment-negative {
    background: linear-gradient(135deg, rgba(220, 53, 69, 0.15) 0%, rgba(220, 53, 69, 0.25) 100%);
    color: #dc3545;
}

.sentiment-neutral {
    background: linear-gradient(135deg, rgba(108, 117, 125, 0.15) 0%, rgba(108, 117, 125, 0.25) 100%);
    color: #6c757d;
}

/* 10. 响应式优化 */
@media (max-width: 992px) {
    .stat-card .value {
        font-size: 1.8rem;
    }
}

@media (max-width: 768px) {
    .app-container {
        padding: 15px;
        margin-top: 10px;
    }
    
    .card-header {
        padding: 1.2rem;
    }
    
    .navbar-brand {
        font-size: 1.3rem;
    }
    
    .input-group-lg > .form-control {
        border-radius: 50px;
    }
    
    .btn-lg {
        width: 100%;
        margin-top: 10px;
    }
    .img-fluid {
        transition: transform 0.3s ease;
    }
    
    .img-fluid:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 30px rgba(67, 97, 238, 0.15);
    }
    
    .card-body.text-center {
        padding: 30px;
        background: rgba(67, 97, 238, 0.03);
        border-radius: 16px;
    }    
}
</style>
'''

# 文本预处理模块
def clean_text(text):
    """清洗文本，去除HTML标签和特殊字符"""
    text = re.sub(r'<.*?>', '', text)  # 去除HTML标签
    text = re.sub(r'[^\w\s]', '', text)  # 去除特殊字符
    return text



def segment_text(text):
    """使用jieba进行中文分词"""
    words = jieba.lcut(text)  # 分词
    return words

def load_stopwords(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stopwords = set([line.strip() for line in f])
        return stopwords
    except FileNotFoundError:
        print(f"警告：未找到停用词文件{file_path}，使用默认停用词")
        return set(["的", "是", "在", "和", "等", "了", "有", "就", "不", "人", "都", "一",
                   "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有",
                   "看", "好", "自己", "这"])


jieba_stopwords = load_stopwords(STOPWORDS_PATH)


def remove_stopwords(words, stopwords):
    """去除分词结果中的停用词"""
    return [word for word in words if word not in jieba_stopwords]  # 过滤停用词


# 摘要生成模块
def generate_summary(text, word_count=5):
    """使用jieba的TextRank算法生成摘要"""
    if not text:
        return []
    summary = jieba.analyse.textrank(text, topK=word_count, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    return summary

def load_external_sentiment_dict(dict_path):
    """加载外部情感词典（格式：每行"词语 情感极性(1/0/-1)"）"""
    sentiment_dict = {'积极': {}, '消极': {}, '中性': {}}
    try:
        with open(dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                word, score = line.split()
                score = int(score)
                if score > 0:
                    sentiment_dict['积极'][word] = score
                elif score < 0:
                    sentiment_dict['消极'][word] = score
                else:
                    sentiment_dict['中性'][word] = score
        return sentiment_dict
    except FileNotFoundError:
        print(f"警告：未找到情感词典文件{dict_path}，使用默认词典")
        return sentiment_dict  # 使用默认词典
    except Exception as e:
        print(f"加载情感词典失败：{e}，使用默认词典")
        return sentiment_dict  # 使用默认词典

# 情感分析模块
default_sentiment_dict = {
    "积极": {"好": 1, "优秀": 1, "成功": 1, "进步": 1, "高兴": 1, "幸福": 1},
    "消极": {"坏": -1, "失败": -1, "痛苦": -1, "困难": -1, "糟糕": -1, "悲伤": -1},
    "中性": {"的": 0, "是": 0, "在": 0, "了": 0, "和": 0, "有": 0}
}


# 初始化时加载外部词典（示例路径，可改为你的实际路径）
# 注意：需在全局作用域定义，确保Flask应用启动时加载
custom_sentiment_dict = load_external_sentiment_dict(EXTERNAL_SENTIMENT_DICT_PATH)

def sentiment_analysis(text, sentiment_dict):
    """分析文本的情感倾向（支持外部词典）"""
    if not text:
        return "中性"

    words = segment_text(text)
    score = 0
    for word in words:
        # 先检查外部词典，再检查默认词典
        for category, words_dict in sentiment_dict.items():
            if word in words_dict:
                score += words_dict[word]
                break
        else:
            # 若外部词典和默认词典均无该词，跳过
            continue

    if score > 0:
        return "积极"
    elif score < 0:
        return "消极"
    else:
        return "中性"

# 合并外部词典和默认词典（外部词典优先级更高）
def merge_sentiment_dicts(external_dict, default_dict):
    """合并情感词典（外部词典覆盖默认词典同词）"""
    merged_dict = {
        '积极': {**default_dict['积极'], **external_dict['积极']},
        '消极': {**default_dict['消极'], **external_dict['消极']},
        '中性': {**default_dict['中性'], **external_dict['中性']}
    }
    return merged_dict

# 加载并合并词典（在应用启动时执行）
custom_sentiment_dict = load_external_sentiment_dict(EXTERNAL_SENTIMENT_DICT_PATH)
merged_sentiment_dict = merge_sentiment_dicts(custom_sentiment_dict, default_sentiment_dict)


import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.font_manager as fm

def generate_wordcloud(word_freq):
    # 指定项目内置字体路径（确保将中文字体文件放在项目目录下）
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'SimHei.ttf')
    
    # 检查字体文件是否存在
    if not os.path.exists(font_path):
        print("警告：项目内置字体文件不存在，尝试使用系统字体...")
        # 如果没有内置字体，尝试使用系统字体
        system_fonts = [
            'SimHei',       # Windows/Linux
            'WenQuanYi Micro Hei',  # Linux
            'Heiti TC',     # macOS
        ]
        
        font_path = None
        for font in system_fonts:
            try:
                # 检查系统是否有此字体
                if font in [f.name for f in fm.fontManager.ttflist]:
                    font_path = font
                    print(f"成功加载系统字体: {font_path}")
                    break
            except Exception as e:
                print(f"尝试加载系统字体 {font} 失败: {str(e)}")
                continue
        
        # 如果仍未找到字体，则使用WordCloud默认字体（可能无法显示中文）
        if not font_path:
            print("警告：未找到任何合适的中文字体，使用默认字体（可能无法显示中文）")
    
    # 生成词云
    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400,
        max_words=200,
        min_font_size=10,
        max_font_size=150,
        random_state=42,
        collocations=False  # 关闭重复词语（可选）
    )
    wc.generate_from_frequencies(word_freq)
    
    # 渲染图片
    img_buffer = BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)  # 去除图片边缘空白
    plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    plt.close()
    
    return img_base64
    
def generate_bar_chart(word_freq, top_n=10):
    """生成词频统计柱状图（使用导入字体）"""
    # 设置项目字体目录路径
    font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
    
    # 定义备选字体文件列表（按优先级排序）
    font_files = [
        'SimHei.ttf',      # 黑体
        'microsoftyahei.ttf',  # 微软雅黑
        'simfang.ttf',     # 仿宋
        'simsun.ttc',      # 宋体
    ]
    
    # 尝试加载项目内字体
    font_path = None
    for font_file in font_files:
        full_path = os.path.join(font_dir, font_file)
        if os.path.exists(full_path):
            try:
                # 注册字体
                fm.fontManager.addfont(full_path)
                font_name = fm.FontProperties(fname=full_path).get_name()
                font_path = full_path
                print(f"成功加载字体: {font_name} ({full_path})")
                break
            except Exception as e:
                print(f"字体 {full_path} 加载失败: {str(e)}")
    
    # 如果未找到项目字体，回退到系统字体
    if not font_path:
        print("警告：未找到项目字体，尝试使用系统字体...")
        system_fonts = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC', 'Microsoft YaHei']
        available_fonts = {f.name for f in fm.fontManager.ttflist}
        
        for font in system_fonts:
            if font in available_fonts:
                plt.rcParams['font.family'] = font
                print(f"使用系统字体: {font}")
                break
        else:
            # 如果没有找到任何中文字体，使用默认设置
            print("警告：未找到任何中文字体，使用默认字体（可能无法正确显示中文）")
            plt.rcParams['font.family'] = ['sans-serif']
    else:
        # 使用加载的项目字体
        font_name = fm.FontProperties(fname=font_path).get_name()
        plt.rcParams['font.family'] = font_name
    
    plt.rcParams['axes.unicode_minus'] = False  # 确保负号正确显示
    
    # 提取前n个高频词
    top_words = word_freq.most_common(top_n)
    if not top_words:
        return None  # 处理空数据情况
    
    words, counts = zip(*top_words)
    
    # 创建图表
    plt.figure(figsize=(10, 5))
    bars = plt.barh(words, counts, color='#4361EE', edgecolor='white')
    plt.gca().invert_yaxis()  # 按词频降序排列
    
    # 添加数据标签
    for bar in bars:
        width = bar.get_width()
        plt.text(width * 1.01, bar.get_y() + bar.get_height()/2,
                 f'{width}', va='center', fontsize=10)
    
    # 图表美化
    plt.xlabel('词频', fontsize=12)
    plt.ylabel('关键词', fontsize=12)
    plt.title('词频统计柱状图', fontsize=16, pad=20)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.margins(x=0.1)  # 调整边距
    plt.tight_layout()
    
    # 保存为base64
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    plt.close()
    
    return img_base64
# 增强的文本分析功能
def advanced_text_analysis(text):
    """对文本进行多维度分析"""
    if not text:
        return {}

    # 基本统计
    sentences = re.split(r'[。！？!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    words = segment_text(text)
    filtered_words = remove_stopwords(words,
                                      set(["的", "是", "在", "和", "等", "了", "有", "就", "不", "人", "都", "一",
                                           "一个", "上", "也", "很", "到", "说", "要", "去", "你", "会", "着", "没有",
                                           "看", "好", "自己", "这"]))

    # 关键词提取
    keywords = generate_summary(text, 10)

    # 词频统计
    word_freq = Counter(filtered_words)
    top_words = word_freq.most_common(10)

    # 句子情感分析
    sentence_sentiments = []
    for sentence in sentences:
        if sentence:
            sentiment = sentiment_analysis(sentence, merged_sentiment_dict)
            sentence_sentiments.append({
                'text': sentence,
                'sentiment': sentiment
            })


    # 生成词云图
    wordcloud_img = generate_wordcloud(word_freq)

    # 生成词频表
    bar_chart_img = generate_bar_chart(word_freq)

    return {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'filtered_word_count': len(filtered_words),
        'keywords': keywords,
        'top_words': top_words,
        'sentence_sentiments': sentence_sentiments,
        'wordcloud_img': wordcloud_img,  # 新增词云图片数据
        'bar_chart_img': bar_chart_img
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    # 处理表单提交
    analysis_type = request.form.get('analysis_type', 'url')
    news_url = request.form.get('news_url', '')
    custom_text = request.form.get('custom_text', '')

    analysis_results = None
    title = ""

    if request.method == 'POST':
        try:
            if analysis_type == 'url' and news_url:
                # 网页分析
                title, content = fetch_news(news_url)
                cleaned_content = clean_text(content)
                summary = generate_summary(cleaned_content, 8)
                sentiment = sentiment_analysis(cleaned_content, merged_sentiment_dict)
                text_analysis = advanced_text_analysis(cleaned_content)

                analysis_results = {
                    'type': 'url',
                    'title': title,
                    'original_text': content[:1000] + ('...' if len(content) > 1000 else ''),
                    'summary': summary,
                    'sentiment': sentiment,
                    'text_analysis': text_analysis
                }

            elif analysis_type == 'text' and custom_text:
                # 文本分析
                cleaned_text = clean_text(custom_text)
                summary = generate_summary(cleaned_text, 5)
                sentiment = sentiment_analysis(cleaned_text, merged_sentiment_dict)
                text_analysis = advanced_text_analysis(cleaned_text)

                analysis_results = {
                    'type': 'text',
                    'original_text': custom_text[:1000] + ('...' if len(custom_text) > 1000 else ''),
                    'summary': summary,
                    'sentiment': sentiment,
                    'text_analysis': text_analysis
                }

        except Exception as e:
            error_msg = f"分析过程中出错: {str(e)}"
            analysis_results = {
                'error': error_msg
            }

    # 生成带图标的情感标签
    sentiment_icon = {
        "积极": "<i class='fas fa-thumbs-up text-success'></i>",
        "消极": "<i class='fas fa-thumbs-down text-danger'></i>",
        "中性": "<i class='fas fa-minus text-muted'></i>"
    }

    return render_template_string(f'''
        {CSS_STYLE}
        <nav class="navbar navbar-expand-lg bg-primary shadow">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-text-height me-2"></i> 文本智能分析系统
                </a>
            </div>
        </nav>

        <div class="app-container py-5">
            <!-- 分析表单 -->
            <div class="card mb-5">
                <div class="card-header bg-primary text-white">
                    <h3 class="mb-0">文本分析工具</h3>
                </div>

                <div class="card-body">
                    <!-- 分析类型选择 -->
                    <div class="analysis-tabs">
                        <ul class="nav nav-tabs" id="analysisTabs" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button class="nav-link {'active' if analysis_type == 'url' else ''}" 
                                        id="url-tab" data-bs-toggle="tab" 
                                        data-bs-target="#url-analysis" type="button" 
                                        role="tab">
                                    <i class="fas fa-link me-2"></i>网页分析
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button class="nav-link {'active' if analysis_type == 'text' else ''}" 
                                        id="text-tab" data-bs-toggle="tab" 
                                        data-bs-target="#text-analysis" type="button" 
                                        role="tab">
                                    <i class="fas fa-file-alt me-2"></i>文本分析
                                </button>
                            </li>
                        </ul>
                    </div>

                    <!-- 分析表单内容 -->
                    <div class="tab-content" id="analysisTabsContent">
                        <!-- URL分析表单 -->
                        <div class="tab-pane fade {'show active' if analysis_type == 'url' else ''}" 
                             id="url-analysis" role="tabpanel">
                            <form method="post">
                                <input type="hidden" name="analysis_type" value="url">
                                <div class="input-group input-group-lg mb-3">
                                    <input type="url" name="news_url" 
                                           class="form-control rounded-pill" 
                                           placeholder="请输入新闻链接（支持主流媒体网站）" 
                                           value="{news_url}"
                                           required>
                                    <button type="submit" class="btn btn-primary rounded-pill ms-3">
                                        分析网页 <i class="fas fa-search ms-2"></i>
                                    </button>
                                </div>
                            </form>
                        </div>

                        <!-- 文本分析表单 -->
                        <div class="tab-pane fade {'show active' if analysis_type == 'text' else ''}" 
                             id="text-analysis" role="tabpanel">
                            <form method="post">
                                <input type="hidden" name="analysis_type" value="text">
                                <div class="mb-3">
                                    <textarea name="custom_text" rows="5" 
                                              class="form-control" 
                                              placeholder="请输入要分析的文本内容（支持句子、段落、文章等）"
                                              required>{custom_text}</textarea>
                                </div>
                                <button type="submit" class="btn btn-primary">
                                    分析文本 <i class="fas fa-text-height ms-2"></i>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 在表单下方添加进度条 -->
        <div id="progress-container" class="d-none mb-4">
            <div class="progress" style="height: 30px;">
                <div id="progress-bar" class="progress-bar progress-bar-striped progress-bar-animated bg-primary" 
                     role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                    <span id="progress-text">准备中...</span>
                </div>
            </div>
        </div>

            <!-- 分析结果 -->
            {render_analysis_results(analysis_results, sentiment_icon) if analysis_results else ''}
        </div>
        
        
        <script>
            // 监听表单提交
            document.querySelector('form').addEventListener('submit', function(e) {{
                e.preventDefault();
                const progressContainer = document.getElementById('progress-container');
                const progressBar = document.getElementById('progress-bar');
                const progressText = document.getElementById('progress-text');
                
                // 显示进度条
                progressContainer.classList.remove('d-none');
                
                // 模拟进度更新（实际应用中应从服务器接收进度数据）
                const steps = [
                    {{ text: '正在发送请求', value: 20 }},
                    {{ text: '正在解析网页', value: 40 }},
                    {{ text: '正在提取内容', value: 60 }},
                    {{ text: '正在分析情感', value: 80 }},
                    {{ text: '正在生成结果', value: 95 }}
                ];
                
                let stepIndex = 0;
                const interval = setInterval(() => {{
                    if (stepIndex >= steps.length) {{
                        clearInterval(interval);
                        return;
                    }}

                    const step = steps[stepIndex];
                    progressBar.style.width = `${{step.value}}%`;
                    progressBar.setAttribute('aria-valuenow', step.value);
                    progressText.textContent = step.text;
                    stepIndex++;
                }}, 1000);

                // 发送表单数据
                const formData = new FormData(this);
                fetch(this.action, {{
                    method: this.method,
                    body: formData
                }})
                .then(response => {{
                    if (response.ok) {{
                        return response.text();
                    }}
                    throw new Error('Network response was not ok');
                }})
                .then(data => {{
                    // 完成进度
                    progressBar.style.width = '100%';
                    progressBar.setAttribute('aria-valuenow', '100');
                    progressText.textContent = '分析完成！';

                    // 显示结果
                    setTimeout(() => {{
                        document.open();
                        document.write(data);
                        document.close();
                    }}, 500);
                }})
                .catch(error => {{
                    console.error('Error:', error);
                    progressText.textContent = '分析失败!';
                }});
            }});
        </script>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            // 初始化选项卡（修正语法错误）
            document.addEventListener('DOMContentLoaded', function() {{
                var tabs = new bootstrap.Tab('#analysisTabs a[role="tab"]');
            }});
        </script>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
    // 初始化选项卡
    document.addEventListener('DOMContentLoaded', function() {{
        // 初始化Bootstrap标签页
        var tabTriggers = [].slice.call(document.querySelectorAll('#analysisTabs button[data-bs-toggle="tab"]'));
        tabTriggers.forEach(function (trigger) {{
            new bootstrap.Tab(trigger);
        }});

        // 表单提交时显示加载状态
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {{
            form.addEventListener('submit', function() {{
                const submitBtn = this.querySelector('button[type="submit"]');
                if (submitBtn) {{
                    const originalText = submitBtn.innerHTML;
                    submitBtn.innerHTML = '处理中 <span class="loading-spinner"></span>';
                    submitBtn.disabled = true;
                    
                    // 恢复按钮状态（在实际应用中应由页面刷新或AJAX回调处理）
                    setTimeout(() => {{
                        submitBtn.innerHTML = originalText;
                        submitBtn.disabled = false;
                    }}, 3000);
                }}
            }});
        );

        // 词云项点击事件
        const wordItems = document.querySelectorAll('.word-item');
        wordItems.forEach(item => {{
            item.addEventListener('click', function() {{
                const word = this.textContent.split(' ')[0];
                alert(`已选择关键词: ${{word}}\n您可以根据此关键词进行进一步分析或搜索。`);
            }});
        }});
    }});
</script>
    ''')


def render_analysis_results(results, sentiment_icon):
    """渲染分析结果的HTML模板"""
    if not results:
        return ''

    # 处理错误情况
    if 'error' in results:
        return f'''
            <div class="card">
                <div class="card-body">
                    <div class="alert alert-danger" role="alert">
                        <i class="fas fa-exclamation-triangle me-2"></i>
                        {results['error']}
                    </div>
                </div>
            </div>
        '''

    # 基本分析结果
    if results['type'] == 'url':
        title_section = f'''
            <div class="mb-4">
                <h4 class="text-primary">
                    <i class="fas fa-heading me-2"></i> 网页标题
                </h4>
                <p class="fs-5">{results['title']}</p>
            </div>
        '''
    else:
        title_section = ''

    # 情感分析
    sentiment = results['sentiment']
    sentiment_badge = f'''
        <span class="badge bg-{
    'success' if sentiment == '积极' else
    'danger' if sentiment == '消极' else 'secondary'
    }">
            {sentiment} 情感
        </span>
    '''

    # 详细文本分析
    text_analysis = results['text_analysis']

    # 生成词云
    word_cloud_html = ''.join([
        f'<span class="word-item" data-count="{count}">{word} ({count})</span>'
        for word, count in text_analysis['top_words']
    ])

    # 生成句子情感分析
    sentence_sentiments_html = ''.join([
        f'''
        <div class="mb-3 p-3 bg-{
        'success/10' if s['sentiment'] == '积极' else
        'danger/10' if s['sentiment'] == '消极' else 'light'
        } rounded">
            <div class="d-flex justify-content-between align-items-center">
                <span class="fw-medium">句子情感: {s['sentiment']}</span>
                {sentiment_icon.get(s['sentiment'], '')}
            </div>
            <p class="mt-2">{s['text']}</p>
        </div>
        '''
        for s in text_analysis['sentence_sentiments'][:10]  # 只显示前10个句子
    ])

    # 优化后的词云展示部分
    wordcloud_html = f'''
       <div class="text-center mt-4 mb-5">
           <div class="word-cloud-container animate__animated animate__fadeIn">
               <h5 class="text-primary mb-4">
                   <i class="fas fa-cloud me-2"></i> 词云分析
                   <small class="text-muted d-block mt-1">点击词云可查看关键词详情</small>
               </h5>
               <div class="d-flex justify-content-center align-items-center" style="min-height: 350px;">
                   <img src="data:image/png;base64,{results['text_analysis']['wordcloud_img']}" 
                        class="img-fluid rounded shadow-lg animate-float"
                        style="max-width: 85%; height: auto; cursor: pointer;"
                        alt="文本分析词云图"
                        onclick="showWordCloudModal()">
               </div>
               <div class="mt-4">
                   {word_cloud_html}
               </div>
           </div>
       </div>
       '''

    stat_cards = f'''
        <div class="row g-4">
            <div class="col-md-4">
                <div class="result-card h-100">
                    <div class="card-body text-center p-4">
                        <div class="bg-primary-soft rounded-circle p-3 d-inline-block mb-3">
                            <i class="fas fa-font fa-2x text-primary"></i>
                        </div>
                        <h5 class="text-primary mb-2">总字数</h5>
                        <p class="display-4 fw-bold text-dark mb-0">{text_analysis['word_count']}</p>
                        <p class="text-muted mb-0">字符</p>
                    </div>
                </div>
            </div>

           <div class="col-md-4">
                <div class="result-card h-100">
                    <div class="card-body text-center p-4">
                        <div class="bg-success-soft rounded-circle p-3 d-inline-block mb-3">
                            <i class="fas fa-sentence fa-2x text-success"></i>
                        </div>
                        <h5 class="text-success mb-2">句子数</h5>
                        <p class="display-4 fw-bold text-dark mb-0">{text_analysis['sentence_count']}</p>
                        <p class="text-muted mb-0">句子</p>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="result-card h-100">
                    <div class="card-body text-center p-4">
                        <div class="bg-{'success-soft' if sentiment == '积极' else 'danger-soft' if sentiment == '消极' else 'secondary-soft'} rounded-circle p-3 d-inline-block mb-3">
                            <i class="fas fa-heart fa-2x text-{'success' if sentiment == '积极' else 'danger' if sentiment == '消极' else 'secondary'}"></i>
                        </div>
                        <h5 class="text-{'success' if sentiment == '积极' else 'danger' if sentiment == '消极' else 'secondary'} mb-2">情感倾向</h5>
                        <p class="display-4 fw-bold text-dark mb-0">{sentiment}</p>
                        <p class="text-muted mb-0">{sentiment_icon.get(sentiment, '')}</p>
                    </div>
                </div>
            </div>
        </div>
        '''

    return f'''
     <div class="card border-0">
         <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center py-3">
             <h3 class="mb-0">
                 <i class="fas fa-chart-pie me-2"></i> 分析结果
             </h3>
             <span class="badge bg-white text-primary fs-6 px-3 py-2 animate-pulse">
                 <i class="fas fa-star me-1"></i> 智能分析
             </span>
         </div>

         <div class="card-body">
             <!-- 基本信息 -->
             <div class="mb-5">
                 {title_section}

                 <!-- 统计卡片 -->
                 {stat_cards}
             </div>

             <!-- 分析详情选项卡 -->
             <div class="mb-5">
                 <ul class="nav nav-tabs nav-fill mb-4" id="detailTabs" role="tablist">
                     <li class="nav-item" role="presentation">
                         <button class="nav-link active" id="summary-tab" data-bs-toggle="tab" 
                                 data-bs-target="#summary-content" type="button" role="tab">
                             <i class="fas fa-highlighter me-2"></i>智能摘要
                         </button>
                     </li>
                     <li class="nav-item" role="presentation">
                         <button class="nav-link" id="keywords-tab" data-bs-toggle="tab" 
                                 data-bs-target="#keywords-content" type="button" role="tab">
                             <i class="fas fa-tags me-2"></i>关键词提取
                         </button>
                     </li>
                     <li class="nav-item" role="presentation">
                         <button class="nav-link" id="wordcloud-tab" data-bs-toggle="tab" 
                                 data-bs-target="#wordcloud-content" type="button" role="tab">
                             <i class="fas fa-cloud me-2"></i>词云分析
                         </button>
                     </li>
                     <li class="nav-item" role="presentation">
                         <button class="nav-link" id="sentiment-tab" data-bs-toggle="tab" 
                                 data-bs-target="#sentiment-content" type="button" role="tab">
                             <i class="fas fa-smile me-2"></i>情感分析
                         </button>
                     </li>
                     <li class="nav-item" role="presentation">
                        <button class="nav-link" id="bar-chart-tab" data-bs-toggle="tab" 
                                data-bs-target="#bar-chart-content" type="button" role="tab">
                            <i class="fas fa-chart-bar me-2"></i>词频柱状图
                        </button>
                    </li>
                 </ul>

                 <div class="tab-content mt-4" id="detailTabsContent">
                     <!-- 摘要内容 -->
                     <div class="tab-pane fade show active" id="summary-content" role="tabpanel">
                         <div class="card border-0 shadow-sm">
                             <div class="card-body">
                                 <div class="d-flex align-items-center mb-3">
                                     <div class="bg-primary-soft rounded p-2 me-3">
                                         <i class="fas fa-clipboard-list fa-2x text-primary"></i>
                                     </div>
                                     <h5 class="mb-0">文本摘要</h5>
                                 </div>
                                 <div class="p-4 bg-light rounded border">
                                     <p class="lead mb-0">{' • '.join(results['summary'])}</p>
                                 </div>
                             </div>
                         </div>
                     </div>
                    
                   <!-- 关键词内容 -->
                     <div class="tab-pane fade" id="keywords-content" role="tabpanel">
                         <div class="card border-0 shadow-sm">
                             <div class="card-body">
                                 <div class="d-flex align-items-center mb-3">
                                     <div class="bg-success-soft rounded p-2 me-3">
                                         <i class="fas fa-key fa-2x text-success"></i>
                                     </div>
                                     <h5 class="mb-0">关键词提取</h5>
                                 </div>
                                 <div class="word-cloud bg-white p-4 rounded border">
                                     {''.join([f'<span class="word-item animate__animated animate__fadeIn" style="animation-delay: {0.1 * i}s">{word}</span>' for i, word in enumerate(text_analysis['keywords'])])}
                                 </div>
                             </div>
                         </div>
                     </div>

                     <!-- 词云内容 -->
                     <div class="tab-pane fade" id="wordcloud-content" role="tabpanel">
                         {wordcloud_html}
                     </div>

                     <!-- 句子情感内容 -->
                     <div class="tab-pane fade" id="sentiment-content" role="tabpanel">
                         <div class="card border-0 shadow-sm">
                             <div class="card-body">
                                 <div class="d-flex align-items-center mb-3">
                                     <div class="bg-info-soft rounded p-2 me-3">
                                         <i class="fas fa-comments fa-2x text-info"></i>
                                     </div>
                                     <h5 class="mb-0">情感分析</h5>
                                 </div>
                                 <div class="mt-3">
                                     {sentence_sentiments_html}
                                 </div>
                             </div>
                         </div>
                     </div>
                     <div class="tab-pane fade" id="bar-chart-content" role="tabpanel">
                        <div class="card border-0 shadow-sm mt-4">
                            <div class="card-body text-center">
                                <img src="data:image/png;base64,{ results['text_analysis']['bar_chart_img'] }" 
                                     class="img-fluid rounded shadow-lg"
                                     style="max-width: 100%; height: 400px;"
                                     alt="词频统计柱状图">
                            </div>
                        </div>
                     </div>
                 </div>
             </div>

             <!-- 原始文本预览 -->
             <div class="card border-0 shadow-sm">
                 <div class="card-body">
                     <div class="d-flex align-items-center mb-3">
                         <div class="bg-warning-soft rounded p-2 me-3">
                             <i class="fas fa-file-alt fa-2x text-warning"></i>
                         </div>
                         <h5 class="mb-0">原始文本预览</h5>
                     </div>
                     <div class="bg-light p-4 rounded border" style="max-height: 300px; overflow-y: auto;">
                         <p class="mb-0">{results['original_text']}</p>
                     </div>
                 </div>
             </div>
         </div>
     </div>

     <!-- 词云模态框 -->
     <div class="modal fade" id="wordCloudModal" tabindex="-1" aria-hidden="true">
         <div class="modal-dialog modal-lg modal-dialog-centered">
             <div class="modal-content">
                 <div class="modal-header bg-primary text-white">
                     <h5 class="modal-title">
                         <i class="fas fa-cloud me-2"></i> 词云详情
                     </h5>
                     <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                 </div>
                 <div class="modal-body text-center p-0">
                     <img src="data:image/png;base64,{results['text_analysis']['wordcloud_img']}" 
                          class="img-fluid"
                          alt="全屏词云图">
                    
                 </div>
                 <div class="modal-footer justify-content-center">
                     <button type="button" class="btn btn-outline-primary" data-bs-dismiss="modal">
                         <i class="fas fa-times me-1"></i> 关闭预览
                     </button>
                 </div>
             </div>
         </div>
     </div>

     <script>
         // 显示词云模态框
         function showWordCloudModal() {{
             new bootstrap.Modal(document.getElementById('wordCloudModal')).show();
         }}

         // 动画控制
         document.querySelectorAll('.btn-animate').forEach(btn => {{
             btn.addEventListener('click', function() {{
                 const animationType = this.dataset.animation;
                 const wordcloudImg = document.querySelector('#wordcloud-content img');

                 // 移除所有动画类
                 wordcloudImg.classList.remove('animate-float', 'animate-pulse', 'animate__animated', 
                                             'animate__pulse', 'animate__shakeX', 'animate__rubberBand');

                 // 添加新动画
                 if (animationType === 'pulse') {{
                     wordcloudImg.classList.add('animate-pulse');
                 }} else if (animationType === 'shake') {{
                     wordcloudImg.classList.add('animate__animated', 'animate__shakeX');
                 }} else if (animationType === 'rubberBand') {{
                     wordcloudImg.classList.add('animate__animated', 'animate__rubberBand');
                 }}
             }});
         }});
     </script>
     '''

# 1. 新闻文本采集模块
def fetch_news(url):
    """从给定的URL获取新闻标题和内容（优化版，提取更完整文字）"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        soup = BeautifulSoup(response.text, 'html.parser')

        # ---------------------- 标题提取优化 ----------------------
        title = "标题未找到"
        title_tags = ['h1', 'h2', 'h3', 'title']  # 按优先级尝试提取标题
        for tag in title_tags:
            elem = soup.find(tag)
            if elem and elem.text.strip():
                title = elem.text.strip()
                break  # 找到第一个有效标题即停止

        # ---------------------- 内容提取优化 ----------------------
        # 定义有效内容标签（按常见新闻结构优先级排序）
        content_tags = ['article', 'body', 'main', 'div', 'p', 'span']
        content = []

        for tag in content_tags:
            # 提取标签内非空文本，并过滤长度过短的内容（≥10字）
            elements = soup.find_all(tag)
            for elem in elements:
                text = elem.get_text(strip=True)
                if len(text) >= 10:  # 过滤极短文本（如导航、版权信息）
                    content.append(text)

        # 合并所有有效文本，按标签出现顺序拼接
        cleaned_content = ' '.join(content).strip()

        # 处理特殊情况：若内容仍为空，尝试提取所有可见文本
        if not cleaned_content:
            visible_text = soup.get_text(strip=True, separator=' ')
            cleaned_content = re.sub(r'\s{2,}', ' ', visible_text)  # 压缩连续空白

        # 最终内容校验
        if len(cleaned_content) < 50:  # 若总长度过短，视为提取失败
            cleaned_content = "内容未找到"

        return title, cleaned_content

    except requests.exceptions.RequestException as e:
        print(f"请求URL出错: {e}")
        return "获取失败", f"无法访问URL: {url}"
    except Exception as e:
        print(f"内容提取异常: {e}")
        return "标题未找到", "内容提取失败"

if __name__ == '__main__':
    app.run(debug=True)

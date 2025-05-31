
//姚洁
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
//岳璐璐
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


//顾瑞莹
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
}
</style>
'''


 //顾瑞莹
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
//姚洁
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
                    //岳璐璐
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

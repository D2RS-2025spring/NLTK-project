代码请粘贴到名字下方
/**
*第一部分代码请在这里粘贴
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

//顾瑞莹

**/
/**
*第二部分代码请在这里粘贴
 //顾瑞莹

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

**/

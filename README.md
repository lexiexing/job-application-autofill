# Job Application Autofill

一个同时提供 **Codex Skill** 和 **Chrome 扩展** 的网申辅助工具。

用户可以直接和 Codex 对话，让 Skill 整理材料并协助填写网申；也可以下载 Chrome 扩展，在浏览器中独立使用。

## 选择使用方式

| 方式 | 适合人群 | 如何使用 |
| --- | --- | --- |
| Codex Skill | 已使用 Codex，希望通过对话整理材料和填写网申 | 安装本仓库后，直接调用 `$job-application-autofill` |
| Chrome 扩展 | 希望在 Chrome 中点击按钮填写，不依赖 Codex 对话 | 下载扩展 ZIP，解压后加载到 Chrome |

两种方式可以单独使用，也可以同时使用。

### 仅使用 Codex Skill

安装 Skill 后直接在 Codex 中对话即可。首次使用时，Codex 会引导上传简历、成绩单、证书和作品集，自动生成私有档案，不需要修改代码。

### 使用 Chrome 扩展

[下载 Chrome 扩展 ZIP](./assets/chrome-extension/job-autofill-extension-public.zip)，然后：

1. 解压 ZIP。
2. 在 Chrome 地址栏打开 `chrome://extensions`。
3. 打开右上角「开发者模式」。
4. 点击「加载已解压的扩展程序」。
5. 选择解压后的 `job-autofill-extension-public` 文件夹。
6. 在自动打开的设置页填写个人资料并保存。

Chrome 扩展不包含任何真实候选人的资料。简历、成绩单和证书由用户在招聘网站中手动选择上传。

## 主要功能

- 自动创建简历、成绩单、证书、作品集等材料目录
- 根据上传材料生成和维护私有候选人档案
- 支持中英文求职、实习、校招和候选人资料表单
- 处理多段教育、实习、工作、项目、奖项和证书经历
- 匹配文本框、日期、下拉框、单选、多选和文件上传字段
- 保留网站已有的正确内容，避免覆盖简历解析结果
- 缺少事实依据时留空并集中询问，不编造个人信息
- 默认不点击提交、暂存、保存或“预览并提交”按钮

## 方式一：安装 Codex Skill

将仓库克隆到 Codex 的 Skills 目录：

```bash
git clone https://github.com/lexiexing/job-application-autofill.git ~/.codex/skills/job-application-autofill
```

然后重启 Codex，使 Skill 被重新加载。

也可以下载 ZIP，将解压后的文件夹复制到：

```text
~/.codex/skills/job-application-autofill
```

请确认 `SKILL.md` 位于上述目录的第一层，而不是嵌套在另一个同名文件夹中。

## 首次使用

在 Codex 中输入：

```text
使用 $job-application-autofill 初始化我的网申资料，请提示我上传材料并自动整理，不需要我修改代码。
```

Skill 会运行初始化脚本并创建：

```text
private/
├── profile.md
└── materials/
    ├── resume/       # 简历
    ├── transcripts/  # 成绩单
    ├── certificates/ # 语言、技能和获奖证书
    ├── portfolio/    # 作品集
    └── other/        # 其他申请材料
```

用户只需把材料拖入当前对话。Codex 会根据文件内容进行分类，并更新 `private/profile.md`，无需修改代码或配置文件。

## 填写网申

完成资料初始化后，可以提供招聘链接并调用 Skill：

```text
使用 $job-application-autofill 根据我的资料填写这个网申，但不要提交：https://example.com/application
```

填写结束后，Skill 会汇报：

- 已填写或纠正的字段
- 因资料不足而留空的字段
- 日期拆分、格式规范等确定性转换
- 已选择或上传的文件
- 是否执行过保存或提交操作

## 隐私与安全

- 所有个人材料存放在 `private/` 中，该目录已被 `.gitignore` 排除。
- 不要把简历、成绩单、证书、身份证明或生成后的 `profile.md` 提交到 GitHub。
- Skill 不会根据简历推断民族、政治面貌、婚姻、宗教、健康和家庭情况等敏感属性。
- 不会编造薪资、调剂意愿、到岗时间、内推码、排名、GPA、导师、日期或语言成绩。
- 日期只有年月时，不会擅自补充具体日期。
- 未获得针对当前申请的明确授权时，不会执行最终提交或其他不可逆操作。
- 不会绕过验证码、身份验证、反自动化检查或网站访问控制。

建议在提交申请前逐项检查表单内容和上传文件。

## 项目结构

```text
job-application-autofill/
├── SKILL.md                         # Skill 核心工作流与安全规则
├── agents/
│   └── openai.yaml                  # Codex 界面名称和默认提示词
├── references/
│   └── profile-template.md          # 私有候选人档案模板
├── scripts/
│   └── init_private_workspace.py    # 私有材料目录初始化脚本
├── assets/
│   └── chrome-extension/
│       └── job-autofill-extension-public.zip
│                                      # 可选的 Chrome 扩展安装包
└── .gitignore                       # 排除私人档案和材料
```

首次初始化后会在本地生成 `private/`，但该目录不会进入版本控制。

## 运行要求

- 使用 Skill：Codex、Python 3.9 或更高版本
- 使用 Chrome 扩展：支持 Manifest V3 的 Chrome 浏览器
- 需要让 Codex 操作登录后的招聘网站时，应允许 Codex 使用相应浏览器会话

## 更新

进入 Skill 目录后执行：

```bash
git pull
```

更新不会覆盖被 Git 忽略的 `private/` 目录。

## 适用边界

不同招聘网站的页面结构和控件实现差异较大，部分复杂日期选择器、级联地区控件、验证码或特殊上传组件可能需要用户手动处理。Skill 应把无法可靠完成的字段报告给用户，而不是猜测或绕过网站限制。

## 免责声明

本项目用于辅助整理求职材料和填写表单。候选人应对最终提交的信息、材料真实性和申请结果负责。使用前请遵守目标网站的服务条款和适用法律。

# Skill Specification v1.0 — AI 编程技能标准格式

## 目的

定义 AI 编程技能的标准格式，使技能可以被 AI 编程助手（如 Trae IDE）正确加载和使用。

## 核心文件

每个技能仓库必须包含：

```
skill-repo/
├── README.md              # 项目说明
├── LICENSE                # 开源许可证
├── CHANGELOG.md           # 版本记录
├── spec/v1.0/skill-spec.md # 本文件
├── platforms/
│   ├── trae/SKILL.md      # Trae IDE 技能（含 YAML frontmatter）
│   └── universal/         # 通用 Markdown 参考版
└── docs/                  # 论文、案例研究、原理解释
```

## 技能文件要求

### YAML frontmatter（必需）

```yaml
---
name: skill-name           # kebab-case
description: 技能描述       # 含触发关键词列表
---
```

### 内容要求

1. **零项目特定引用**：适用于任何语言、框架、领域
2. **可执行操作**：非抽象理论，有具体步骤和检查清单
3. **标准输出格式**：审查/设计完成后的统一模板
4. **清晰触发条件**：用户知道什么场景下该使用

## 梁文锋式技能作为参考实现

本规范的首个参考实现，展示如何将一种思维方式系统化为 AI 编程技能。

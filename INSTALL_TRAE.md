# 梁文锋式思维技能 — Trae IDE 安装指南

## ⚡ 快速安装

### 方法 1: 直接导入（推荐）

1. **打开 Trae IDE**
2. **进入技能管理**
   - Settings → Skills → Manage Skills
3. **导入技能文件**
   - 点击 "Import Skill"
   - 选择文件：`/workspace/platforms/trae/SKILL.md`
4. **确认导入**
   - 技能名称：`liangwenfeng-thinking`
   - 版本：1.1.0
5. **完成！**现在可以使用了

---

### 方法 2: 复制到技能目录

如果你知道 Trae 的技能存储目录，可以直接复制：

```bash
# 假设 Trae 技能目录是 ~/.trae/skills
cp /workspace/platforms/trae/SKILL.md ~/.trae/skills/liangwenfeng-thinking.md
```

然后重启 Trae IDE。

---

## 🎯 如何使用

安装完成后，在对话中直接说以下关键词即可触发：

| 你想说... | 触发的功能 |
|----------|-----------|
| "用梁文锋思维审查这个文件" | 完整系统审查 |
| "找找这里有没有隐藏的漏洞" | 不变量分析 |
| "优化一下成本/性能" | 稀疏化优化 |
| "六层递进诊断一下" | 深度诊断 |
| "用梁文锋思维" | 通用模式 |

---

## 📝 技能文件信息

- **文件位置**: `/workspace/platforms/trae/SKILL.md`
- **技能名称**: `liangwenfeng-thinking`
- **版本**: 1.1.0
- **最后更新**: 2026-05-11

---

## ✅ 验证安装

安装完成后，你可以这样验证：

1. 创建一个测试文件 `test_buggy.py`（内容在 [examples/buggy.py](examples/buggy.py)）
2. 在 Trae 中说："用梁文锋思维审查 test_buggy.py"
3. 你应该会看到一份结构化的审查报告！

---

## 📚 更多资源

- [快速入门指南](QUICKSTART.md)
- [示例代码](examples/)
- [完整文档](docs/)

---

## 🆘 遇到问题？

如果技能没有正确加载：
1. 检查 YAML frontmatter 是否正确（文件开头的 `---` 部分）
2. 确认文件格式是 UTF-8 编码
3. 重启 Trae IDE 后重试

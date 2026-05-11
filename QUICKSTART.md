# 快速入门 — 5 分钟上手

> "不要先读完整本书，先看结果。"

## 3 步快速体验

### 第 1 步：找一个"有问题"的代码片段

复制这个有典型问题的代码（我们叫它 `buggy.py`）：

```python
# buggy.py - 梁文锋式审查示例

class FaceAuthSystem:
    def __init__(self):
        # 问题1: 每次都加载模型，没有单例
        self.model = load_arcface_model()
    
    def verify_face(self, image):
        try:
            similarity = self.model.predict(image)
            # 问题2: 硬编码返回 0.80，阈值是 0.85
            return similarity
        except Exception as e:
            logger.warning(f"验证失败: {e}")
            return 0.80  # ← 假装通过
    
    def check_permission(self, user, resource):
        # 问题3: TODO 占位，永远返回 True
        return True  # TODO: 实现权限检查
    
    def collect_feedback(self, result):
        # 问题4: 反馈收集了但没人用
        self.feedback_history.append(result)

# 调用方
auth = FaceAuthSystem()
similarity = auth.verify_face(user_image)
if similarity >= 0.85:
    grant_access()  # 永远不会执行！
```

### 第 2 步：调用技能

在对话中输入：

```
用梁文锋思维审查这个文件
```

### 第 3 步：看结果

你会得到类似这样的输出（这就是这个技能的价值）：

```
## 梁文锋式审查报告

### 1. 隐藏结构分析
- **不变量断裂 1**: "验证失败时应该拒绝访问" → 实际 `return 0.80` 绕过了
- **不变量断裂 2**: "权限检查应该真实执行" → 实际永远 `return True`

### 2. 稀疏化分析
- **浪费 1**: `load_arcface_model()` 每次实例化都加载 → 改单例可省 ~600MB GPU
- **浪费 2**: `collect_feedback()` 收集但没人读 → 闭环断裂

### 优先级清单
🔴 立即修复: `return 0.80`、`return True // TODO`
🟡 近期优化: 模型单例化、反馈闭环
```

就这么简单！你现在体验了这个技能的核心价值。

---

## 一句话触发场景速查

| 你想做什么 | 你说什么 |
|-----------|---------|
| 审查代码找隐藏漏洞 | "用梁文锋思维审查这个目录" |
| 优化成本/性能 | "用稀疏化思维优化这个系统" |
| 设计新模块 | "用梁文锋思维设计这个功能" |
| 觉得之前审查不够深 | "六层递进诊断这个系统" |

---

## 下一步

- 想了解原理？读 [WHY_LIANGWENFENG.md](docs/WHY_LIANGWENFENG.md)
- 想深入学习？读 [SKILL.md](platforms/trae/SKILL.md)
- 想看真实案例？看 [examples/](examples/) 目录

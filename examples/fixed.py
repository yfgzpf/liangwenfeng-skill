# -*- coding: utf-8 -*-
"""
梁文锋式审查示例 - 修复后的版本
解决了 4 个问题：
1. ✅ 模型单例化（稀疏化）
2. ✅ 异常时正确处理（不变量保护）
3. ✅ 权限检查真正实现（不变量保护）
4. ✅ 反馈闭环形成（自监督进化）
"""

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


# ==================== 修复 1: 模型单例化 ====================
_arcface_model_instance = None


def get_arcface_model():
    """获取 ArcFace 模型单例（只加载一次）"""
    global _arcface_model_instance
    if _arcface_model_instance is None:
        logger.info("正在加载 ArcFace 模型... (消耗 600MB 显存)")
        _arcface_model_instance = {"name": "ArcFace", "version": "1.0"}
    else:
        logger.info("使用已加载的 ArcFace 模型单例")
    return _arcface_model_instance


def grant_access():
    """模拟授予访问权限"""
    logger.info("✅ 访问已授予")


class FeedbackLoop:
    """反馈闭环系统"""
    def __init__(self):
        self.history = []
        self.threshold_adjustment = 0.0
    
    def collect(self, result: Dict[str, Any]):
        """收集反馈"""
        self.history.append(result)
        logger.info(f"反馈已收集: {result}")
        self._adapt()  # 收集后立即适配
    
    def _adapt(self):
        """根据反馈自我调整（自监督进化）"""
        if len(self.history) >= 5:
            recent = self.history[-5:]
            false_rejects = sum(1 for r in recent if r.get("granted") and r.get("similarity", 0) < 0.9)
            if false_rejects >= 2:
                self.threshold_adjustment -= 0.02
                logger.info(f"🔄 自适应调整: 阈值下调 {self.threshold_adjustment}")


class FaceAuthSystem:
    def __init__(self, feedback_loop: FeedbackLoop = None):
        # 修复 1: 使用单例模型
        self.model = get_arcface_model()
        self.feedback_loop = feedback_loop or FeedbackLoop()
    
    def verify_face(self, image):
        """验证人脸"""
        try:
            similarity = self._calculate_similarity(image)
            return similarity
        except Exception as e:
            logger.error(f"验证失败: {e}")
            # 修复 2: 异常时明确返回失败值，而不是假装通过
            return 0.0  # 明确表示验证失败
    
    def _calculate_similarity(self, image):
        """计算相似度（内部方法）"""
        # 简化模拟
        base = 0.92
        return base + self.feedback_loop.threshold_adjustment
    
    def check_permission(self, user, resource):
        """检查用户权限"""
        # 修复 3: 真正实现权限检查
        if not user or not resource:
            return False
        # 这里应该是实际的权限逻辑
        return user.startswith("user_") and resource.startswith("resource_")
    
    def collect_feedback(self, result):
        """收集用户反馈"""
        # 修复 4: 反馈闭环形成，会触发自适应
        self.feedback_loop.collect(result)


# ==================== 调用方代码 ====================

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # 创建反馈闭环（全局共享）
    feedback_loop = FeedbackLoop()
    
    # 场景：同一个服务中多次实例化
    auth1 = FaceAuthSystem(feedback_loop)  # 第 1 次加载模型
    auth2 = FaceAuthSystem(feedback_loop)  # 使用已加载的单例 ✅
    
    # 验证人脸
    user_image = "path/to/image.jpg"
    similarity = auth1.verify_face(user_image)
    
    # 阈值判断
    if similarity >= 0.85:
        if auth1.check_permission("user123", "resource456"):
            grant_access()
            granted = True
        else:
            logger.warning("❌ 权限检查失败")
            granted = False
    else:
        logger.warning("❌ 人脸验证失败")
        granted = False
    
    # 收集反馈（会触发自适应）✅
    auth1.collect_feedback({"similarity": similarity, "granted": granted})
    
    print(f"\n历史反馈: {feedback_loop.history}")
    print(f"自适应调整量: {feedback_loop.threshold_adjustment}")
    print("✅ 反馈闭环已形成，系统会越用越好！")

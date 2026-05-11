# -*- coding: utf-8 -*-
"""
梁文锋式审查示例 - 有问题的版本
包含 4 个典型问题：
1. 模型重复加载（稀疏化问题）
2. 硬编码假通过（不变量问题）
3. TODO 权限占位（不变量问题）
4. 反馈闭环断裂（自监督问题）
"""

import logging

logger = logging.getLogger(__name__)


def load_arcface_model():
    """模拟加载 ArcFace 模型（消耗约 600MB GPU 显存）"""
    logger.info("正在加载 ArcFace 模型... (消耗 600MB 显存)")
    # 实际项目中这里是真正的模型加载
    return {"name": "ArcFace", "version": "1.0"}


def grant_access():
    """模拟授予访问权限"""
    logger.info("✅ 访问已授予")


class FaceAuthSystem:
    def __init__(self):
        # 问题 1: 每次实例化都加载模型，没有单例
        self.model = load_arcface_model()
        self.feedback_history = []
    
    def verify_face(self, image):
        """验证人脸"""
        try:
            similarity = self._calculate_similarity(image)
            return similarity
        except Exception as e:
            logger.warning(f"验证失败: {e}")
            # 问题 2: 硬编码返回 0.80，假装通过（调用方阈值是 0.85）
            return 0.80
    
    def _calculate_similarity(self, image):
        """计算相似度（内部方法）"""
        # 简化模拟
        return 0.92
    
    def check_permission(self, user, resource):
        """检查用户权限"""
        # 问题 3: TODO 占位，永远返回 True
        return True  # TODO: 实现实际的所有权检查逻辑
    
    def collect_feedback(self, result):
        """收集用户反馈"""
        # 问题 4: 反馈收集了但没人读（闭环断裂）
        self.feedback_history.append(result)
        logger.info(f"反馈已收集: {result}")


# ==================== 调用方代码 ====================

if __name__ == "__main__":
    # 场景：同一个服务中多次实例化
    auth1 = FaceAuthSystem()  # 第 1 次加载模型
    auth2 = FaceAuthSystem()  # 第 2 次加载模型（浪费！）
    
    # 验证人脸
    user_image = "path/to/image.jpg"
    similarity = auth1.verify_face(user_image)
    
    # 阈值判断
    if similarity >= 0.85:
        auth1.check_permission("user123", "resource456")
        grant_access()
    else:
        logger.warning("❌ 人脸验证失败")
    
    # 收集反馈（但没人用）
    auth1.collect_feedback({"similarity": similarity, "granted": True})
    
    print(f"\n历史反馈: {auth1.feedback_history}")
    print("但是... 这些反馈被用来改进系统了吗？")

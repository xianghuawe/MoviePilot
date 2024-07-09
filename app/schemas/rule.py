from typing import Optional

from pydantic import BaseModel


class CustomRule(BaseModel):
    """
    自定义规则项
    """
    # 规则ID
    id: Optional[str] = None
    # 名称
    name: Optional[str] = None
    # 包含
    include: Optional[list] = []
    # 排除
    exclude: Optional[list] = []
    # 大小范围
    size_range: Optional[str] = None
    # 最少做种人数
    seeders: Optional[str] = None


class FilterRuleGroup(BaseModel):
    """
    过滤规则组
    """
    # 名称
    name: Optional[str] = None
    # 规则串
    rule_string: Optional[str] = None
    # 适用类媒体类别 None-全部 电影/电视剧
    media_type: Optional[str] = None
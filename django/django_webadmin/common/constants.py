# coding=utf-8

SEX = (
    (0, u'男'),
    (1, u'女'),
)

TRUE_FALSE = (
    (True, u'是'),
    (False, u'否')
)

DICT_NULL_BLANK_TRUE = {
    'null': True,
    'blank': True
}

EXCLUDE_BASE_FIELD = ('creator', 'created_at', 'updated_at', 'deleted_at')

PAYWAY = (
    (0, u"记应付帐款"),
    (1, u"现金付款"),
    (2, u"预付款"),
)

GOODS_ORDER_STATUS = (
    (0, u"待审核"),
    (1, u"审核通过"),
)

GOODS_STORAGE_STATUS = (
    (0, u"待入库"),
    (1, u"已入库"),
)


class UsableStatus(object):
    UNUSABLE = False
    USABLE = True
    STATUS = (
        (UNUSABLE, u'禁用'),
        (USABLE, u'启用'),
    )


class TaskStatus(object):
    NORMAL = 0
    EXCEPT = 1
    FINISHED = 2
    DELETED = 3
    TASK_STATUS = (
        (NORMAL, u'正常(进行中)'),
        (EXCEPT, u'异常'),
        (FINISHED, u'完成'),
        (DELETED, u'删除')
    )

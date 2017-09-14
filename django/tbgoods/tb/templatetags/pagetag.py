# _*_ coding:utf-8 _*_


from django import template
register = template.Library() #为了成为一个可用的标签库，这个模块必须包含一个名为  register  的变量，它是 template.  Library 的一个实例，所有的标签和过滤器都是在其中注册的

@register.filter     #自定义过滤器
def kong_upper(val):
    print ('val from template:',val)
    return val.upper()


from django.utils.html import format_html
@register.simple_tag        #自定义标签
def circle_page(curr_page,loop_page):  #当前页码与所有页码相减
    offset = abs(curr_page - loop_page)
    if offset < 3:      #显示当前页码为中心，向前后位移的页码数，其它的隐藏，即return ''
        if curr_page == loop_page:
            page_ele = '<td class="active"><a href="?page=%s">-%s-</a></td>'%(loop_page,loop_page)
        else:
            page_ele = '<td><a href="?page=%s">-%s-</a></td>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''

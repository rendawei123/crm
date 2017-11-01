
from django.template import Library
from types import FunctionType

register = Library()


def result_head_list(data_list):
    if not data_list.list_display:
        yield data_list.model_config.model_name

    else:
        for name in data_list.list_display:
            if isinstance(name, FunctionType):
                yield name(data_list.model_config, is_header=True)
            else:
                yield data_list.model_config.model_class._meta.get_field(name).verbose_name


def result_body_list(data_list):
    for row in data_list.data_list:
        if not data_list.list_display:
            print([row, ])
            yield [row, ]
        else:
            l = []
            for name in data_list.list_display:
                if isinstance(name, FunctionType):
                    l.append(name(data_list.model_config, obj=row))
                else:
                    l.append(getattr(row, name))
            print(l)
            yield l


@register.inclusion_tag('curd/aaa.html')
def show_result_list(data_list):

    return {
        'headers': result_head_list(data_list),
        'result': result_body_list(data_list)
    }

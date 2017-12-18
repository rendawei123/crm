from django.shortcuts import render, HttpResponse


class ShowList(object):
    def __init__(self, data_list, model_config):
        self.data_list = data_list
        self.model_config = model_config
        self.list_display = model_config.get_show_list_display()


class CurdConfig(object):
    """
    基础配置类
    """
    list_display = []

    def __init__(self, model_class):
        self.model_class = model_class
        self.request = None
        self.model_name = model_class._meta.model_name

    def get_show_list_display(self):
        list_display = []
        if self.list_display:
            list_display.extend(self.list_display)

        return list_display

    # 生成添加，删除等url
    @property
    def urls(self):
        return self.get_url(), None, None

    def show_list(self, request):

        data_list = self.model_class.objects.all()
        cl = ShowList(data_list, self)
        context = {
            'cl': cl
        }

        return render(request, 'curd/show_list.html', context)
        # return HttpResponse('show list')

    def add_list(self, request):
        return HttpResponse('add list')

    def del_list(self, request):
        return HttpResponse('del list')

    def mod_list(self, request):
        return HttpResponse('mod list')

    def get_url(self):
        from django.conf.urls import url

        # curd/curd/userinfo/add/
        patterns = [
            url(r'^$', self.show_list),
            url(r'^add/', self.add_list),
            url(r'^del/', self.del_list),
            url(r'^mod/', self.mod_list),
        ]

        return patterns


class CurdSite(object):
    """
    构造URL
    """
    def __init__(self, name='curd'):
        self.name = name
        self.namespace = name
        self._registry = {}

    def register(self, model, model_config=None):
        if not model_config:
            model_config = CurdConfig
        self._registry[model] = model_config(model)

    def get_urls(self):
        patterns = []

        from django.conf.urls import url
        patterns += [
            url(r'^login/', self.login),
            url(r'^logout/', self.logout),
        ]
        for model_class, model_nb_obj in self._registry.items():

            patterns += [
                url(r'^%s/%s/' % (model_class._meta.app_label, model_class._meta.model_name,), model_nb_obj.urls)
            ]
            # curd/app01/user/

        return patterns

    def login(self, request):
        """
        登录
        :return:
        """
        return HttpResponse('用户登录')

    def logout(self, request):
        """
        退出
        :return:
        """
        return HttpResponse('退出登录')

    @property
    def urls(self):
        return self.get_urls(), self.name, self.namespace

site = CurdSite()


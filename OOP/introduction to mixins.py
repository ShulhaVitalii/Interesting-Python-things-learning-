"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yXPFcDe6jco

Подвиг 8 (введение в паттерн миксинов - mixins). Часто множественное наследование используют для наполнения дочернего
класса определенным функционалом. То есть, с указанием каждого нового базового класса, дочерний класс приобретает все
больше и больше возможностей. И, наоборот, убирая часть базовых классов, дочерний класс теряет соответствующую часть
функционала.

Например, паттерн миксинов активно используют в популярном фреймворке Django.  В частности, когда нужно указать
дочернему классу, какие запросы от клиента он должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.).
В качестве примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна миксинов.
"""

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        else:
            method_request = request.get('method').lower()
        return self.__getattribute__(method_request)(request)


class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


assert issubclass(DetailView, GeneralView), "класс DetailView должен наследоваться от класса GeneralView"


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()

try:
    html = view.render_request({'url': '123', 'method': 'POST'})
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при вызове команды render_request({'url': '123', 'method': 'POST'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

try:
    html = view.render_request({'url': '123', 'method': 'PUT'})
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове команды render_request({'url': '123', 'method': 'PUT'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

html = view.render_request({'url': '123', 'method': 'GET'})
assert html == "GET: 123", "метод render_request вернул неверные данные"


class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()
html = view.render_request({'url': '123', 'method': 'POST'})
assert html == "POST: 123", "метод render_request вернул неверные данные"

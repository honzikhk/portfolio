from django.views.generic import TemplateView


class HomepageView(TemplateView):   # this view maybe should be moved somewhere away, same the main_homepage.html
    template_name = "main/main_homepage.html"
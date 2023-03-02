from django.template import Library

register = Library()

# a função recebe: request, paginator e página atual, nesta ordem
@register.inclusion_tag('core/pagination.html')
def pagination(request, paginator, page_obj):
   
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['page_obj'] = page_obj
   
    # page_obj1 = paginator.page(1)
    # print(page_obj1.object_list)
    # copiar variáveis de GET
    getvars = request.GET.copy()
   
    if 'page' in getvars:
        del getvars['page']
    if len(getvars) > 0:
        context['getvars'] = '&{0}'.format(getvars.urlencode())
    else:
        context['getvars'] = ''
    return context
 
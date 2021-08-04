from  .models import Category

# context_processors são funções chamadas toda fez que a app for renderizada
def categories(request):
    return {
        'categories': Category.objects.all()
    }
    
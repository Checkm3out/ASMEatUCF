from wagtail.core.models import Page


def dynamic_url(request):
    pages = Page.objects.all()
    print("printing pages: ")
    print(pages)
    sorted_pages = []
    for item in pages:
        print(item)
        print(item.show_in_menus)
        print(item.pk)

    return {
        'nav_urls': Page.objects.all()
    }
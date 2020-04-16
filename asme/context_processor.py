from wagtail.core.models import Page


def dynamic_url(request):
    pages = Page.objects.in_menu()
    # print("printing pages: ")
    # print(pages)
    # sorted_pages = []
    # for item in pages:
    #     print(item)
    #     print(item.show_in_menus)
    #     print(item.pk)

    return {
        'nav_urls': pages
    }
from rest_framework.pagination import PageNumberPagination


class PaginationNumber(PageNumberPagination):
    page_size = 45
    page_query_param = 'sayfa'
    page_size_query_param = 'adet'
    # page_query_description = 'bu sayfada belirtilen sayıda örnek vardır'
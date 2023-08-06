from rest_framework.pagination import PageNumberPagination
class CustomPageNumberPagination(PageNumberPagination):
    def get_page_size(self, request):
        page_size = request.query_params.get('page_size')
        if page_size is not None:
            return int(page_size)
        return super().get_page_size(request)


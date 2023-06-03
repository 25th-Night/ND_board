from django.core.paginator import Paginator


class Pagination(Paginator):

    def __init__(self, request, target, data_per_page=5):
        self.request = request
        self.target = target
        self.data_per_page = data_per_page

    @property
    def paginate(self):
        paginator = Paginator(object_list=self.target, per_page=self.data_per_page)
        page = self.request.GET.get("page", 1)
        page_obj = paginator.get_page(page)
        page_num_list = [num for num in range(1, page_obj.paginator.num_pages + 1)]
        empty_row_count = self.data_per_page - len(page_obj)

        return [page, page_obj, page_num_list, empty_row_count]
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trains.models import Train

__all__ = ('home', 'TrainListView'
    # 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView',
)


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)

class TrainListView(ListView):
    paginate_by = 3
    model = Train
    template_name = 'trains/home.html'


    
    
#class TrainsDetailView(DetailView):
#    queryset = Trains.objects.all()
#    template_name = 'trains/detail.html'


#class TrainsCreateView(SuccessMessageMixin, CreateView):
#    model = Trains
#    form_class = TrainsForm
#    template_name = 'trains/create.html'
#    success_url = reverse_lazy('trains:home')
#    success_message = "Город успешно создан"


#class TrainsUpdateView(SuccessMessageMixin, UpdateView):
#    model = Trains
#    form_class = TrainsForm
#    template_name = 'trains/update.html'
#    success_url = reverse_lazy('trains:home')
#    success_message = "Город успешно отредактирован"


# class TrainsDeleteView(DeleteView):
#   model = Trains
#   template_name = 'trains/delete.html'
#   success_url = reverse_lazy('trains:home')

#    def get(self, request, *args, **kwargs):
#        messages.success(request, 'Город успешно удален')
#        return self.post(request, *args, **kwargs)







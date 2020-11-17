from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.views import View
from django.http import HttpResponse
from discussion.models import Thread, Comment
from discussion.forms import ThreadForm, CommentForm

# Create your views here.
class ThreadListView(ListView):
    model = Thread
    template_name = 'discussion/thread_list.html'
    def get(self, request):
        thread = Thread.objects.all()
        context = {'thread_list':thread}

        return render(request, self.template_name, context)

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'discussion/thread_detail.html'

    def get(self, request, pk):
        t = get_object_or_404(Thread, id = pk)
        comment = Comment.objects.filter(thread = t).order_by('updated_at')
        comment_form = CommentForm
        context = {'thread': t, 'comments' : comment, 'comment_form' : CommentForm }

        return render(request, self.template_name, context)

class ThreadCreateView(View):
    template_name = 'discussion/create_thread.html'
    success_url = reverse_lazy('discussion:all')

    def get(self, request, pk = None):
        form = ThreadForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk = None):
        form = ThreadForm(request.POST, request.FILES or None)

        if not form.is_valid():
            context = {'form' : form}
            return render(request, self.template_name, context)
        form.save()
        return redirect(self.success_url)

def stream_file(self, pk):
    t = get_object_or_404(Thread, id=pk)
    response = HttpResponse()
    response['Content-Type'] = t.content_type
    response['Content-Length'] = len(t.picture)
    response.write(t.picture)
    return response

class CommentCreateView(View):

    def post(self, request, pk):
        t = get_object_or_404(Thread, id = pk)
        comment = Comment(text = request.POST['text'], thread = t)
        #
        comment.save()
        return redirect(reverse_lazy('discussion:detail', args=[pk]))

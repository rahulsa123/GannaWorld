from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
# Create your views here.er
from django.views.decorators.http import require_POST
from .models import Song, PlayList
from django.contrib.auth.decorators import login_required
from .forms import SongCreateForm, PlayListCreateForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def song_create(request):
    if request.method == "POST":
        s_form = SongCreateForm(request.POST, request.FILES)
        if s_form.is_valid():
            new_song = s_form.save(commit=False)
            new_song.owner = request.user
            new_song.slug = slugify(new_song.title)
            new_song.save()
            s_form.save_m2m()
            messages.success(request,  f"new song {new_song.title} added")
            return redirect(new_song.get_absolute_url())
        else:
            print("sform invlaid")
    else:
        s_form = SongCreateForm()
    return render(request, "song/song_create.html", {"form": s_form})


@login_required
@require_POST
def user_likes(request):
    if request.method == "POST" and request.is_ajax():
        # try:
        song = Song.objects.get(pk=request.POST.get("id"))
        user = song.user_likes.filter(pk=request.user.pk).first()
        print("user", user)
        if user:
            # user dislike song
            song.user_likes.remove(request.user)
            # send inverse input like
            return JsonResponse({"status": "Like"})
        else:
            # user like song
            song.user_likes.add(request.user)
            # send inverse input Dislike
            return JsonResponse({"status": "Dislike"})

        return JsonResponse({"status": "error"})


class SongDetailView(DetailView):
    model = Song
    context_object_name = "song"
    template_name = "song/song_detail.html"


class PlayListDetailView(DetailView):
    model = PlayList
    context_object_name = "playlist"
    template_name = 'song/playlist_detail.html'


class Home(ListView):
    model = Song
    queryset = Song.objects.all()
    context_object_name = "songs"
    template_name = "song/home.html"
    paginate_by = 6


class MyPlayList(LoginRequiredMixin, ListView):
    model = Song
    context_object_name = "playlists"
    template_name = "song/playlist_home.html"
    paginate_by = 6

    def get_queryset(self):
        return PlayList.objects.filter(owner=self.request.user)


class SearchView(ListView):
    model = Song
    context_object_name = "songs"
    template_name = "song/home.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['search_text'] = self.request.GET.get("search")
        return context

    def get_queryset(self):
        return Song.objects.filter(title__contains=self.request.GET.get("search"))


@login_required
def playlist_create_view(request):
    if request.method == "POST":
        p_form = PlayListCreateForm(request.POST, request.FILES)
        if p_form.is_valid():
            new_playlist = p_form.save(commit=False)
            new_playlist.owner = request.user
            new_playlist.slug = slugify(new_playlist.title)
            new_playlist.save()
            p_form.save_m2m()
            messages.success(
                request,  f"new playlist {new_playlist.title} added")
            return redirect(new_playlist.get_absolute_url())
        else:
            print("p form invlaid")
    else:
        p_form = PlayListCreateForm
    return render(request, "song/playlist_create.html", {"form": p_form})

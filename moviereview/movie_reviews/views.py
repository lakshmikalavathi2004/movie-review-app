from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieReview
from .forms import MovieReviewForm


def review_list(request):
    query = request.GET.get('q')

    if query:
        reviews = MovieReview.objects.filter(movie_name__icontains=query)
    else:
        reviews = MovieReview.objects.all()

    return render(request, 'movie_reviews/review_list.html', {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = MovieReviewForm()

    return render(request, 'movie_reviews/add_review.html', {'form': form})


def edit_review(request, id):
    review = get_object_or_404(MovieReview, id=id)

    if request.method == 'POST':
        form = MovieReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = MovieReviewForm(instance=review)

    return render(request, 'movie_reviews/add_review.html', {'form': form})


def delete_review(request, id):
    review = get_object_or_404(MovieReview, id=id)
    review.delete()
    return redirect('review_list')
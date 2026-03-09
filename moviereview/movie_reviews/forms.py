from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['movie_name', 'reviewer_name', 'rating', 'review_text']
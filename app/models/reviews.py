class Review:
    
    """
    class that creates review objects
    """

    all_reviews = []


    def __init__(self, movie_id, title, image_url, review):

        self.movie_id = movie_id
        self.title = title
        self.image_url =image_url
        self.review = review

    def save_review(self):

        Review.all_reviews.append(self)
    
    @classmethod
    def clear_reviews(cls):

        Review.all_reviews.clear()
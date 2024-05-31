from .models import Product, Review


def calculate_rating_and_count(product):
    """
    Calculate and return various metrics for
    the given product's reviews and star rating
    """
    reviews = product.review_set.all()
    average_rating = product.calculate_average_rating()
    review_count = reviews.count()

    # Count reviews for each star rating
    one_star_count = reviews.filter(rating=1).count()
    two_star_count = reviews.filter(rating=2).count()
    three_star_count = reviews.filter(rating=3).count()
    four_star_count = reviews.filter(rating=4).count()
    five_star_count = reviews.filter(rating=5).count()

    total_reviews = (
        five_star_count
        + four_star_count
        + three_star_count
        + two_star_count
        + one_star_count
    )

    if total_reviews > 0:
        five_star_percentage = (five_star_count / total_reviews) * 100
        four_star_percentage = (four_star_count / total_reviews) * 100
        three_star_percentage = (three_star_count / total_reviews) * 100
        two_star_percentage = (two_star_count / total_reviews) * 100
        one_star_percentage = (one_star_count / total_reviews) * 100
    else:
        # Handle the case when there are no reviews to avoid division by zero
        five_star_percentage = 0
        four_star_percentage = 0
        three_star_percentage = 0
        two_star_percentage = 0
        one_star_percentage = 0

    # Calculate star percentages
    star_percentages = {
        rating: (average_rating / 5) * 100 for rating in range(1, 6)
    }

    return {
        "average_rating": average_rating,
        "review_count": review_count,
        "one_star_count": one_star_count,
        "two_star_count": two_star_count,
        "three_star_count": three_star_count,
        "four_star_count": four_star_count,
        "five_star_count": five_star_count,
        "five_star_percentage": five_star_percentage,
        "four_star_percentage": four_star_percentage,
        "three_star_percentage": three_star_percentage,
        "two_star_percentage": two_star_percentage,
        "one_star_percentage": one_star_percentage,
        "star_percentages": star_percentages,
    }

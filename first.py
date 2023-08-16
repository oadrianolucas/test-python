def solution(n, ratings):
    dish_ratings = {}

    for dish_id, *dish_ratings_list in ratings:
        avg_rating = sum(dish_ratings_list) / len(dish_ratings_list)

        if dish_id not in dish_ratings:
            dish_ratings[dish_id] = (avg_rating, sum(dish_ratings_list))
        else:
            existing_avg, _ = dish_ratings[dish_id]
            if avg_rating > existing_avg:
                dish_ratings[dish_id] = (avg_rating, sum(dish_ratings_list))
            elif avg_rating == existing_avg and sum(dish_ratings_list) > dish_ratings[dish_id][1]:
                dish_ratings[dish_id] = (avg_rating, sum(dish_ratings_list))

    max_avg_rating = 0
    best_dish = -1

    for dish_id, (avg_rating, _) in dish_ratings.items():
        if avg_rating > max_avg_rating:
            max_avg_rating = avg_rating
            best_dish = dish_id
        elif avg_rating == max_avg_rating and dish_id < best_dish:
            best_dish = dish_id

    return best_dish


n = int(input())

ratings = [list(map(int, input().split())) for i in range(n)]

out_ = solution(n, ratings)

print(out_)

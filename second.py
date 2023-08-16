def solution(seconds):
    if seconds == 0:
        return "now"

    time_units = []
    years, seconds = divmod(seconds, 365 * 24 * 60 * 60)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    if years:
        time_units.append(f"{years} {'years' if years > 1 else 'year'}")
    if days:
        time_units.append(f"{days} {'days' if days > 1 else 'day'}")
    if hours:
        time_units.append(f"{hours} {'hours' if hours > 1 else 'hour'}")
    if minutes:
        time_units.append(
            f"{minutes} {'minutes' if minutes > 1 else 'minute'}")
    if seconds:
        time_units.append(
            f"{seconds} {'seconds' if seconds > 1 else 'second'}")

    if len(time_units) == 1:
        return time_units[0]
    elif len(time_units) == 2:
        return f"{time_units[0]} and {time_units[1]}"
    else:
        and_string = " and "
        return ", ".join(time_units[:-1]) + and_string + time_units[-1]


seconds = int(input())

out_ = solution(seconds)
print(out_)

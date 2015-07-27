from __future__ import division

SPREADS = {
    6: [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 4.0],
    5: [1.0, 1.0, 2.0, 2.0, 3.0, 4.0],
    4: [1.0, 1.0, 2.0, 3.0, 3.0],
    3: [1.0, 1.0, 2.0, 4.0],
    2: [1.0, 2.0, 3.0],
    1: [1.0, 1.0],
}


def round_to_nearest(x, base):
    # nudge towards rounding up (eg 4.5 towards 5) because in python3: "if two
    # multiples are equally close, rounding is done toward the even choice"
    # ... which makes no sense to me
    divided = float(x) / base
    rounded = round(divided + 0.01)
    return base * int(rounded)


def find_links_in_gap(link_count, start, finish, is_left=False):
    size_of_gap = (finish - start) + 1
    spread = SPREADS[link_count]
    increment = (size_of_gap / sum(spread))

    # calculate the intervals to be used, based upon the spread (which
    # favours putting the extra links nearer to the current page)
    running_total = 0
    last_step = 0
    steps = []
    for i in range(0, link_count):
        link = spread[i]
        running_total += (increment * link)
        step = int(round(running_total))
        if step <= last_step or step < 1:
            step = last_step + 1
        steps.append(step)
        last_step = step

    links = []
    for step in steps:
        if is_left:
            step = finish + 1 - step
        else:
            step = step + start - 1

        if size_of_gap > (49 * link_count):
            step = round_to_nearest(step, 50)
        elif size_of_gap > (9 * link_count):
            step = round_to_nearest(step, 10)
        elif size_of_gap > (4 * link_count):
            step = round_to_nearest(step, 5)

        # rounding can make useless numbers
        if step >= start and step <= finish:
            links.append(step)

    return links


def concertina(page, total_pages):
    # this will cause ValueError if not numbers, correctly aborting
    page = int(page)
    total_pages = int(total_pages)

    # we won't paginate out of the range of pages
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    # we can always show 1-10 no matter what, so don't bother calculating it
    if total_pages < 11:
        return list(range(1, total_pages+1))

    # current, first, and last pages are always present
    pages = {page: 1, 1: 1, total_pages: 1}

    # two to either side of the current page are always present
    for x in range(page-2, page+3):
        if x > 1 and x < total_pages:
            pages[x] = 1

    # how many pages are missing from the navigation
    pages_to_the_left = page - 4                 # remove 1, itself, two beside
    if pages_to_the_left < 0:
        pages_to_the_left = 0
    pages_to_the_right = total_pages - page - 3  # remove last, two beside
    if pages_to_the_right < 0:
        pages_to_the_right = 0
    total_missing = pages_to_the_left + pages_to_the_right

    # how many can we put back in on either side, favouring more
    # links on the side where there is the bigger gap...
    left_ratio = pages_to_the_left/total_missing
    right_ratio = pages_to_the_right/total_missing
    links_to_the_left = int(round(6 * left_ratio))
    links_to_the_right = int(round(6 * right_ratio))

    # ...but always with at least one link
    if links_to_the_left == 0 and pages_to_the_left:
        links_to_the_left = 1
        links_to_the_right = 5
    if links_to_the_right == 0 and pages_to_the_right:
        links_to_the_right = 1
        links_to_the_left = 5

    # add links only where they are not already present
    if page > 4:
        pages.update(
            dict(
                (k, 1) for k in find_links_in_gap(
                    link_count=links_to_the_left,
                    start=2,
                    finish=page - 3,
                    is_left=True,
                )
            )
        )
    if page < (total_pages - 4):
        pages.update(
            dict(
                (k, 1) for k in find_links_in_gap(
                    link_count=links_to_the_right,
                    start=page + 3,
                    finish=total_pages - 1,
                )
            )
        )

    return sorted(pages.keys())

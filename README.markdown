django-concertina
=================

Implements concertina-style pagination for use in django templates and code.

Concertina pagination (also known as bell-curve pagination) provides for
faster user navigation and better search engine discovery on paginated pages
where there may be tens or hundreds of results pages.

Using this will give you up to 13 links, always anchored to the first and
last page, two pages to either side of the current page, and a distribution
of other pages. For example, on page 12 of 27, the links will be:

1 .. 6 .. 9 10 11 **12** 13 14 15 16 .. 19 .. 22 .. 27

On page 427 of 2,783:

1 .. 200 .. 425 426 **427** 428 429 .. 600 .. 800 .. 1150 .. 1500 .. 2050 .. 2783


Blog posts about the idea:

* [Bell Curve Pagination - For The Google Juice!](http://www.gareth53.co.uk/blog/2010/09/bellcurve-concertina-pagination-google-indexing.html)
* [Concertina pagination – getting large scale websites indexed](http://www.locallytype.com/2008/11/28/concertina-pagination-getting-large-scale-websites-indexed/)


## Usage

Install into your virtualenv:

    pip install django-concertina

Then in python directly:

    >>> from concertina import concertina
    >>> concertina(12, 27)
    [1, 6, 9, 10, 11, 12, 13, 14, 15, 16, 19, 22, 27]
    >>> concertina(427, 2783)
    [1, 200, 425, 426, 427, 428, 429, 600, 800, 1150, 1500, 2050, 2783]

Or in your templates, first add `concertina` to your `INSTALLED_APPS`
then:

    {% load concertina_pagination %}

    <ul>
        {% for page in page_obj|concertina_pagination %}
          <li><a href='?page={{page}}'>{{page}}</a></li>
        {% endfor %}
    </ul>

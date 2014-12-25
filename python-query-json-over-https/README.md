# Task

Write a basic command-line script to extract parts of the ReviewBoards REST-API.

    $ ./solution.py https://www.reviewboard.org/api/store/categories/ >links.self.method
	'GET'
    $ ./solution.py https://www.reviewboard.org/api/store/categories/ store_categories[0].name
	'Extensions'

A **GET request** to the URL returns a complex object in JSON — **parse out the part** that the user is interested in and **prettyprint** it.

## Challenges

1. Use [argparse](https://docs.python.org/dev/library/argparse.html) to read url and query from the command line. `argparse` is the standard library for parsing args; it's good to know it. *Alternative:* Use [docopt](docargs).
1. Use [requests](www.python-requests.org/) to make a [GET request](http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request).
  1. Learn how to [send custom headers](http://docs.python-requests.org/en/latest/user/quickstart/#custom-headers). By default, ReviewBoards API represents its resources in XML. You need to supply the [accept](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1) header with the [correct value](https://en.wikipedia.org/wiki/Internet_media_type#List_of_common_media_types) to signal the server to send you the [JSON representation](http://json.org/) of the resource.
1. Learn about [regular expressions in Python](https://docs.python.org/dev/library/re.html) to parse the queries. Support queries built of the following components, with the standard meaning (examples in the description and test case):
  1. `word`, where `word` is a dictionary key and consists of a non-zero number of alphanumerical characters. Result of this query is the dictionary value.
  1. `word[number]` where `number` is an index to a list, hence a non-negative integer. Result of this query is the `number`th value of the list accessible by the
  1. `value1.value2` where `value1` and `value2` are either one of the above constructs. The result of this query has the usual meaning of resolving `value1` first and then resolving `value2` in the context of the result.
1. Learn about [pprint](https://docs.python.org/3.5/library/pprint.html), a library to prettyprint structured data, such as simple nested python objects.

# How to do it

## Prepare the virtualenv (once)

Create a [virtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html), activate it and install the requirements (use requirements.txt for the default challenges above).

    mkvirtualenv kata-query-json-over-https
	pip install -r requirements.txt

Make sure the REST API actually works by running the tests against the reference solution.

    ./testit.py --solution reference.py

## Prepare the session (each day)

1. Make sure to understand what the script is supposed to do. (Read the above)
1. Activate the virtualenv.

	`workon kata-query-json-over-https`

1. Create an empty `solution.py`.
1. Prepare a console to run the tests against your solution — once you are finished, hit RETURN and if the test succeeds, you're done. If it does not, fix the bugs until they do.

    `./testit.py`

1. Start the timer and start coding.

Have fun!

# A broken SSL certificate?

You may see this:

    SSLError: hostname 'www.reviewboard.org' doesn't match either of 'beanbaginc.com', 'www.beanbaginc.com'


Turns out, Beanbag INC is the company behind ReviewBoard, and hosting the API on its server. That message is `requests` (2.5.1 in my case) on Python 2 telling you that the SSL module does [not support Server-Name-Indication](http://docs.python-requests.org/en/latest/community/faq/#what-are-hostname-doesn-t-match-errors). In Python 3 it is fixed.

To make it work, you can install the following additional dependencies, as pointed out on the website.

    pip install pyOpenSSL ndg-httpsclient pyasn1

Alternatively, you may add an additional challenge :)

*Bonus:* Learn how to ignore [locally signed and invalid SSL certificates](http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification). `requests` expects, sensibly enough, SSL certificates to be properly signed.

When you add the config option `verify=False` you ignore that warning — and all others. Whenever you need to trust the source being authentic to deliver correct data, that is a bad idea. That's why you then may see this warning:

    /home/murat/.envs/kata-query-json-over-https/local/lib/python2.7/site-packages/requests/packages/urllib3/connectionpool.py:734: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.org/en/latest/security.html
      InsecureRequestWarning)

That's expected. :)

# The UNIX way.

For the fun of it: Query the API in your UNIX-shell, using curl and [jq](http://stedolan.github.io/jq/), while allowing for `jq`'s slightly different query syntax.

    .links.self.method
    .store_categories[0].name

Actually, *if you needed this functionality*, this is a much better way to go than writing your own script — so go play with `jq`. :)

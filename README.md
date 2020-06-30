# Challenge Pandas

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Installation

Challenge Pandas requires [Python](https://www.python.org/) v3.6+ and [Pip](https://pypi.org/project/pip/) to run

Clone repository

```sh
$ git clone ...
```

Go directory

```sh
$ cd challenge-pandas
```

Install the dependencies

```sh
$ pip3 install -r requirements/base.txt
```

To run tests

```sh
$ pytest
```

Run service with logging
```sh
$ python3 main.py --logging=info
```

This is a example result

```sh
INFO:root:==============================================================
INFO:root:Init process
INFO:root:==============================================================
INFO:root:Create a table Location
INFO:root:==============================================================
INFO:root:Call service to get region list
INFO:root:==============================================================
INFO:root:Call service to get country list from region random item
INFO:root:==============================================================
INFO:root:Generate Dataframe
INFO:root:==============================================================
INFO:root:  region   city_name                                  language      time
0  Polar  Antarctica  f604247ee45bf2d62720dbc7f2bb99a5790b5894  0.016177
INFO:root:==============================================================
INFO:root:Sum of time: 0.016176999999999886
INFO:root:Average time: 0.016176999999999886
INFO:root:Max time: 0.016176999999999886
INFO:root:==============================================================
INFO:root:Save SQLite dataframe
INFO:root:==============================================================
INFO:root:Save Json dataframe
INFO:root:==============================================================
```

License
----

MIT


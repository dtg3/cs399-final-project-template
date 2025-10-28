# Tests

This contains all the code to run pytest. Ideally, you will only need to modify the
`test_routes.py` file to add tests, or create new `test_*.py` files to test specific
aspects of your application. Whie I advise separating tests for the various routes your
api will have, since we are doing a small scale project, I'm fine if you elect to put all
the tests in `test_routes.py`, but use descriptive naming conventions for your test functions
and make sure to group related tests.

I cannot stress enough that if you don't make tests, you'll perpetually be trying to figure out
if your Flask API is broken or the React frontend. Take the time, make tests. It will save you
frustration later...
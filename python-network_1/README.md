# Python - Network #1

This directory contains Python scripts that practice making HTTP
requests, working with response headers and status codes, submitting
form data, parsing JSON, and using the GitHub REST API.

## Requirements

-   Python 3
-   The `requests` package for scripts that use it
-   Internet access for the external API exercises
-   For local sandbox exercises, the provided test web server must be
    running on port `5000`

Install `requests` if needed:

``` bash
python3 -m pip install requests
```

Make a script executable before running it:

``` bash
chmod +x filename.py
```

## Files and descriptions

  ---------------------------------------------------------------------------
  File                                Description
  ----------------------------------- ---------------------------------------
  `0-hbtn_status.py`                  Fetches
                                      `https://intranet.hbtn.io/status` using
                                      `urllib` and displays information about
                                      the response body.

  `1-hbtn_header.py`                  Takes a URL and displays the
                                      `X-Request-Id` response header using
                                      `urllib`.

  `2-post_email.py`                   Takes a URL and email address, sends
                                      the email as a POST parameter, and
                                      displays the response body using
                                      `urllib`.

  `3-error_code.py`                   Fetches a URL using `urllib`; prints
                                      the response body or
                                      `Error code: <status>` for an HTTP
                                      error.

  `4-hbtn_status.py`                  Uses `requests` to fetch
                                      `https://alx-intranet.hbtn.io/status`
                                      and displays the response body type and
                                      content.

  `5-hbtn_header.py`                  Takes a URL and prints its
                                      `X-Request-Id` response header using
                                      `requests`.

  `6-post_email.py`                   Takes a URL and email address, sends a
                                      POST request with the parameter
                                      `email`, and prints the response body.

  `7-error_code.py`                   Takes a URL and prints the response
                                      body, or `Error code: <status>` for
                                      HTTP status codes of 400 or higher.

  `8-json_api.py`                     Sends a POST request to the local
                                      `/search_user` endpoint with a `q`
                                      parameter, then handles and displays
                                      the JSON response.

  `10-my_github.py`                   Uses Basic Authentication with a GitHub
                                      username and personal access token to
                                      print the authenticated user's numeric
                                      ID.

  `100-github_commits.py`             Takes a repository name and owner name,
                                      calls the GitHub commits API, and
                                      prints up to 10 commits as
                                      `<sha>: <author name>`.
  ---------------------------------------------------------------------------

## Usage

Run commands from this directory.

### Fetch status with `requests`

``` bash
./4-hbtn_status.py
```

### Display a request ID

``` bash
./5-hbtn_header.py https://alx-intranet.hbtn.io
```

### Submit an email address

``` bash
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### Handle HTTP status codes

Start the provided local test server on port `5000` in a separate
terminal, then run:

``` bash
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500
```

The script prints the response body for status codes below 400, and
`Error code: <status>` for status codes of 400 or higher.

### Search the local JSON API

``` bash
./8-json_api.py
./8-json_api.py a
```

The script sends `q` as a POST parameter to
`http://0.0.0.0:5000/search_user`. The test server may return random
data, so IDs and names can differ between runs.

### Retrieve your GitHub user ID

``` bash
./10-my_github.py YOUR_GITHUB_USERNAME YOUR_PERSONAL_ACCESS_TOKEN
```

Create a GitHub personal access token with the minimum required
`read:user` permission. Do not share your token, hard-code it in the
script, or commit it to the repository. If authentication fails, the
script should print `None`.

### List recent repository commits

``` bash
./100-github_commits.py rails rails
```

The script requests up to 10 commits from the GitHub REST API and prints
each commit SHA with the author name recorded in the commit metadata.
GitHub's unauthenticated API rate limit applies.

## Output formats

Examples of expected output formats:

``` text
Body response:
    - type: <class 'str'>
    - content: OK
```

``` text
Error code: 404
```

``` text
[8446] example_name
```

``` text
<commit_sha>: <author_name>
```

Exact request IDs, commit details, and JSON search results may vary.

## Notes

-   Scripts `0` through `3` use Python's `urllib`; scripts `4` onward
    use `requests`.
-   The local sandbox examples require the assignment's test server to
    be running and reachable on port `5000`. A `Connection refused`
    error usually means the server is not running or is not accessible.
-   These are educational exercises and do not include comprehensive
    network-error handling or argument validation unless required by the
    exercise.

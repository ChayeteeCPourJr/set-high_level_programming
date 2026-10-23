# python-network_0

Bash scripts that use `curl` to interact with a web server, plus one algorithm exercise (finding a peak in a list).

## Requirements

- Ubuntu (Bash)
- `curl`
- Python 3 (only for `6-peak.py`)
- Scripts are executable (`chmod +x <file>`)
- The web server on port `5000` is only available in the SET sandbox, so the `curl` scripts must be tested there

## Files

### Mandatory

| File | Description |
| --- | --- |
| `0-body_size.sh` | Takes a URL, sends a request, and displays the size of the response body in bytes |
| `1-body.sh` | Sends a `GET` request to a URL and displays the body only if the status code is `200` |
| `2-delete.sh` | Sends a `DELETE` request to a URL and displays the body of the response |
| `3-methods.sh` | Takes a URL and displays all HTTP methods the server accepts |
| `4-header.sh` | Sends a `GET` request with the header `X-School-User-Id: 98` and displays the body |
| `5-post_params.sh` | Sends a `POST` request with the variables `email` and `subject` and displays the body |
| `6-peak.py` | Function `find_peak(list_of_integers)` that returns a peak of an unsorted list in `O(log(n))` |
| `6-peak.txt` | Time complexity of the `find_peak` algorithm |

### Advanced

| File | Description |
| --- | --- |
| `100-status_code.sh` | Sends a request to a URL and displays only the status code (no pipes, redirections, `;` or `&&`) |
| `101-post_json.sh` | Sends a JSON `POST` request with the contents of a file (second argument) and displays the body |
| `102-catch_me.sh` | Makes a request to `0.0.0.0:5000/catch_me` so the server responds with `You got me!` |

## Usage

```bash
./0-body_size.sh 0.0.0.0:5000
# 10

./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
# Route 2

./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
# I'm a DELETE request

./3-methods.sh 0.0.0.0:5000/route_4
# OPTIONS, HEAD, PUT

./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
# Hello School!

./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
# POST params:
#	email: test@gmail.com
#	subject: I will always be here for PLD

./100-status_code.sh 0.0.0.0:5000 ; echo ""
# 200

./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
# Valid JSON

./102-catch_me.sh ; echo ""
# You got me!
```

`find_peak` can be tested from Python:

```python
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))  # 6
print(find_peak([]))               # None
```

## Notes

- Each `curl` script uses `-s` (silent mode) so only the requested output is printed.
- `6-peak.py` uses a binary search: it compares the middle element with its right neighbor and keeps the half that must contain a peak.

## Author

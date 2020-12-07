Built on the [Goodreads API](https://www.goodreads.com/api).

### Setup
###### Checking out
```bash
git clone <repo>
cd goodreads-bookmark/
```

###### Developer Key
To access the Goodreads API, you [need a developer key](https://www.goodreads.com/api/documentation).
1. Register for a key [here](https://www.goodreads.com/api/keys) and save the generated `key` and `secret`.
2. In `/key.json`, save your `key` and `secret` as strings.
3. Run `git update-index --assume-unchanged key.json` from your command line.

# movie

### install
```bash
# main
$ pip install git+https://github.com/HaramSs/movie.git

# branch
$ pip install git+https://github.com/HaramSs/movie.git@0.2/api
```

### start dev
```
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install
$ pytest

$ #option
$ pdm venv create
```

### setting env
```
cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"
```

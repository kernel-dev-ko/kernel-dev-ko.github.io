This project use GitHub Pages service.
So, if you want to preview modified pages before upload modified documents,
you may test those pages on local jekyll server.
This documents will guide for it.

# install pre-requesites package

$ sudo apt install reby-full build-essential zlib1g-dev
$ gem install bundler
$ bundle install

# execute Jekyll server

$ bundle update
$ bundle exec jekyll serve [--port < port-number >]

It's default port is 4000. you may access with "http://localhost:4000"

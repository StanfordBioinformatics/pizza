FROM ubuntu:14.04
MAINTAINER Kate Smith <nathankw@stanford.edu>
RUN apt-get update && apt-get install -y ruby ruby-dev
RUN gem install sinatra

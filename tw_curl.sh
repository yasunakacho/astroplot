#!/bin/bash

curl --request GET \
 --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' \
 --header 'authorization: OAuth oauth_consumer_key="158328362-NDXr90tA6ZiwWF5EtwQhh1vcAOFLrNxpl8pO99et", \

 oauth_nonce="generated-nonce", oauth_signature="generated-signature", \

 oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", \

 oauth_token="zxwcHlI5FAKRtBlU3GGxDzW5Z", oauth_version="1.0"'

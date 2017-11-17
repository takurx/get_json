require 'net/http'
require 'uri'
require 'json'

    uri = URI.parse('http://111.111.111.111/hogehoge.json')

    json = Net::HTTP.get(uri)

    puts json

    result = JSON.parse(json)

    puts result


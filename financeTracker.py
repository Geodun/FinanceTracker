#!/bin/env python
import config

from finnhub import client as Finnhub
client = Finnhub.Client(config.api_key)

print(client.company_profile(symbol="NFLX"))

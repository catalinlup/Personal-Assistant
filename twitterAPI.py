try:
    from twitter import*
except:
    print("Error! Please install twitter API!")

access_token = 	'618087450-26csbKlyvHTAzGm96jnwMHexWx8eq4zVUv9tIbdM'
access_token_secret ='y3zf9gY6s5GTUzjm2onQqed4fwDP5BdePTgGwF6uqLUz1'
consumer_key = 'W3Cu6S01CjedmXbW7UOgW0tuC'
consume_secret = '3aNuhY1Ko4AdV0oL4VRSNRaNmhN6nqnadbEyMh0Aobl857okuw'


t = Twitter(auth=OAuth(access_token,access_token_secret,consumer_key,consume_secret))

def SendOnTwitter(text):
    t.statuses.update(status=text)

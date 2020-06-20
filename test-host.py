import urllib.request
import asyncio
import re

def get(url):
    response = urllib.request.urlopen(serverip + urllib.parse.quote(url)).read()
    response = re.search("'.*'", str(response)).group()
    response = response.strip("\'[]")
    return str(response)

serverip = "http://127.0.0.1:5000/"
session = "testsession:#:?%"
result = get("/session/" + session + "/create")

async def main():
    partHp = [[3680], [9348, 5168, 504], [7123, 31074]]
    partHpModifier = [30, 70, 110]
    ailmentBuildup = [[190, 692], [21], [61, 28, 0]]
    ailmentBuildupModifier = [10, 15, 5]

    for i in range(len(partHp)):
        for j in range(len(partHp[i])):
            assert(get("/session/" + session + "/monster/" + str(i) + "/part/" + str(j) + "/create") == "true")
            assert(get("/session/" + session + "/monster/" + str(i) + "/part/" + str(j) + "/hp/" + str(partHp[i][j])) == "true")

    print("parts created")

    for i in range(len(ailmentBuildup)):
        for j in range(len(ailmentBuildup[i])):
            assert(get("/session/" + session + "/monster/" + str(i) + "/ailment/" + str(j) + "/create") == "true")

    print("ailments created")

    while True:
        print("changing values")
        
        for i in range(len(partHp)):
            for j in range(len(partHp[i])):
                if partHp[i][j] <= partHpModifier[i]:
                    partHp[i][j] = 9999
                partHp[i][j] -= partHpModifier[i]
                assert(get("/session/" + session + "/monster/" + str(i) + "/part/" + str(j) + "/hp/" + str(partHp[i][j])) == "true")

        for i in range(len(ailmentBuildup)):
            for j in range(len(ailmentBuildup[i])):
                ailmentBuildup[i][j] += ailmentBuildupModifier[i]
                assert(get("/session/" + session + "/monster/" + str(i) + "/ailment/" + str(j) + "/buildup/" + str(ailmentBuildup[i][j])) == "true")

        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt as e:
    pass

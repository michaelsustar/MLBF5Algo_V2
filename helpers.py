import statsapi


def getAllPitchersFromGames(games):
    return [[game['game_id'], game['home_probable_pitcher'], game['away_probable_pitcher']] for game in games]


def findPlayerId(playerName):
    try:
        playerId = statsapi.lookup_player(playerName)[0]['id']
        return playerId
    except:
        return 0


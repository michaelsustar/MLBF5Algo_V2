import statsapi
import datetime
from helpers import getAllPitchersFromGames, findPlayerId


todayDate = datetime.datetime.now().strftime('%m/%d/%Y')
todayGames = statsapi.schedule(start_date=todayDate, end_date=todayDate)

todaysPitchers = getAllPitchersFromGames(todayGames)

boxscore = statsapi.boxscore_data(778735, timecode=None)

del boxscore['playerInfo']

print(boxscore)




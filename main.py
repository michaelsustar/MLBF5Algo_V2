import statsapi
import datetime
from helpers import getAllPitchersFromGames, findPlayerId


todayDate = datetime.datetime.now().strftime('%m/%d/%Y')
todayGames = statsapi.schedule(start_date=todayDate, end_date=todayDate)

todaysPitchers = getAllPitchersFromGames(todayGames)

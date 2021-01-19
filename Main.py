import TicTacToeJudge
import MinimaxBot, DummyBot

BotNumOneObj = MinimaxBot.BotNumOne()
BotNumTwoObj = DummyBot.BotNumTwo()
Judge = TicTacToeJudge.TicTacToeJudge(BotNumOneObj, BotNumTwoObj)
Judge.SetBotOneName("Bot One")
Judge.SetBotTwoName("Bot Two")
Winner, GameBaord = Judge.TakeTurns()
print(Winner)
for line in (GameBaord[iterator:iterator + 3] for iterator in range(0, len(GameBaord), 3)):
    print(str(line))

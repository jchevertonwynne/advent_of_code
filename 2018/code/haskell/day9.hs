import Data.List.PointedList

type ScoreBoard = [(Int, Int)]

createScoreBoard :: Int -> ScoreBoard
createScoreBoard n = map (\n -> (n, 0)) [1..n]

incScore :: ScoreBoard -> ScoreBoard

game :: Int -> Int -> Int
game plr mrb = plr * mrb

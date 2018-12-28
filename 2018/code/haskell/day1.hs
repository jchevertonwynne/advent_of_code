import Data.HashSet (HashSet, fromList, member, insert)

parseLine :: String -> Int
parseLine line@(h:t)
    | h == '+'  = read t
    | otherwise = read line

findLoop :: [Int] -> Int
findLoop nums = findLoopA 0 nums nums (fromList [0])

findLoopA :: Int -> [Int] -> [Int] -> (HashSet Int) -> Int
findLoopA tot (h:t) n2 set
    | con       = nxt
    | null t    = findLoopA nxt n2 n2 nset
    | otherwise = findLoopA nxt t n2 nset
    where
        nxt     = tot + h
        con     = nxt `member` set
        nset    = nxt `insert` set

main :: IO()
main = do
    file <- readFile "../../input/input_day1.txt"
    let input = map parseLine $ lines file
        part1 = sum input
        part2 = findLoop input
    print part1
    print part2

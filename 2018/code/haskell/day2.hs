import Prelude hiding (filter)
import Data.HashMap.Lazy (HashMap, filter, empty, elems, lookupDefault, insert, member)
import Debug.Trace (traceShow)

type LetterCount = HashMap Char Int

getCount :: String -> LetterCount
getCount str = getCountA str (empty :: LetterCount)

getCountA :: String -> LetterCount -> LetterCount
getCountA (h:t) hm
    | null t    = mhm
    | otherwise =  getCountA t mhm
    where
        inc     = (lookupDefault 0 h hm) + 1
        mhm     = insert h inc hm

checkCount :: LetterCount -> (Int, Int)
checkCount hm =
    let c2    = fromEnum ((length (filter (== 2) hm)) >= 1)
        c3    = fromEnum ((length (filter (== 3) hm)) >= 1)
    in  (c2, c3)

findSimilar :: String -> [String] -> [String] -> String
findSimilar s l@(h:t) f@(hf:tf)
    | similar   = combine s h
    | null tf   = "this failed"
    | null t    = findSimilar hf tf tf
    | otherwise = findSimilar s t f
    where
        similar = compareCodes s h

combine :: String -> String -> String
combine [] []   = ""
combine fa@(a:ta) (b:tb)
    | same      = a:(combine ta tb)
    | otherwise = combine ta tb
    where
        same     = a == b

compareCodes :: String -> String -> Bool
compareCodes a b = compareCodesA (zip a b) 0

compareCodesA :: [(Char, Char)] -> Int -> Bool
compareCodesA [] i = i <= 1
compareCodesA l@((a, b):t) i
    | a == b       = compareCodesA t i
    | i == 1       = False
    | otherwise    = compareCodesA t 1
    where
        same       = a == b

part1 :: [String] -> Int
part1 str        = 
    let cnt      = map getCount str
        chk      = map checkCount cnt
        (n2, n3) = foldr (\(a, b) (c, d) -> (a + c, b + d)) (0, 0) chk
    in  n2 * n3

part2 :: [String] -> String
part2 (h:t) = findSimilar h t t

main :: IO()
main = do
    file <- readFile "../../input/input_day2.txt"
    let input = lines file
        p1    = part1 input
        p2    = part2 input
    print p1
    print p2
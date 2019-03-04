import Prelude hiding (filter)
import Data.Maybe (fromJust, isJust)
import Text.Regex (mkRegex, matchRegex)
import Data.HashMap.Lazy (HashMap, filter, empty, elems, lookupDefault, insert, member)

type Coord = (Int, Int)
type NumFreq = (Int, Int)
type FreqCount = HashMap Coord Int
type Row = (Int, Int, Int, Int, Int)
type BoxSize = Int -> Int -> Int -> Int

splitLine :: String -> Row
splitLine str              =
    let regex              = mkRegex "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
        extract            = matchRegex regex str
        [id, x, y, xl, yl] = map read (fromJust extract) :: [Int]
    in  (id, x, y, xl, yl)

countFreq :: [NumFreq] -> FreqCount -> FreqCount
countFreq [] hmap    = hmap
countFreq (h:t) hmap =
    let v            = (lookupDefault 0 h hmap) + 1
        nmap         = insert h v hmap
    in  countFreq t nmap

part1 :: FreqCount -> Int
part1 hmap = length (filter (>= 2) hmap)

part2 :: FreqCount -> [Row] -> Int
part2 hmap [] = 0
part2 hmap ((id, x, y, xl, yl):t)
    | satifies   = id
    | otherwise  = part2 hmap t
    where
        options  = [(i, j) 
                   | i <- [x .. (x + xl - 1)]
                   , j <- [y .. (y + yl - 1)]
                   ]
        satifies = all (== 1) $ map (\c -> lookupDefault 0 c hmap) options

main :: IO()
main = do
    file <- readFile "../../input/input_day3.txt"
    let input = map splitLine (lines file)
        options = [ (i, j) 
                  | (id, x, y, xl, yl) <- input
                  , i <- [x .. (x + xl - 1)]
                  , j <- [y .. (y + yl - 1)]
                  ]
        hmap  = countFreq options (empty :: FreqCount)
        p1    = part1 hmap
        p2    = part2 hmap input
    print p1
    print p2
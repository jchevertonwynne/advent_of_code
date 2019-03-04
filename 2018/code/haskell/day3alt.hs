import Prelude hiding (filter)
import Data.Maybe (fromJust, isJust)
import Text.Regex (mkRegex, matchRegex)
import Data.HashSet (HashSet, fromList, member, insert, empty, union)

type ID = Int
type Coord = (Int, Int)
type Common = HashSet Coord
data Row = Row { 
                 id :: ID,
                 xs :: Int,
                 ys :: Int,
                 xe :: Int,
                 ye :: Int 
               }

splitLine :: String -> Row
splitLine str =
    let regex = mkRegex "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
        extract = matchRegex regex str
        [id, x, y, xl, yl] = map read (fromJust extract) :: [Int]
    in  Row id x y (x + xl - 1) (y + yl - 1)

findCommon :: [Row] -> Common
findCommon (h:t) = findCommonA h t t (empty :: Common)

findCommonA :: Row -> [Row] -> [Row] -> Common -> Common
findCommonA r (h:t) f@(hf:tf) com
    | null tf   = com 
    | endnolap  = findCommonA r  t  f  com
    | null t    = findCommonA hf tf tf mod
    | otherwise = findCommonA r  t  f  mod
    where
        xb = max (xs r) (xs h)
        yb = max (ys r) (ys h)
        xl = min (xe r) (xe h)
        yl = min (ye r) (ye h)
        nooverlap = (xl < xb) && (yl < yb)
        endnolap = nooverlap && null t
        shared = [ (i, j)
                 | i <- [xb .. xl]
                 , j <- [yb .. yl]
                 ]
        mod = com `union` (fromList shared)

part1 :: Common -> Int
part1 com = length com

part2 :: [Row] -> Common -> Maybe ID
part2 [] com    = Nothing
part2 (h:t) com
    | satisfies = Just id
    | otherwise = part2 t com
    where
        Row id x1 y1 x2 y2 = h
        coords = [ (i, j)
                 | i <- [x1 .. x2]
                 , j <- [y1 .. y2]
                 ]
        satisfies = all (\n -> not (n `member` com)) coords

main :: IO()
main = do
    file <- readFile "../../input/input_day3.txt"
    let input  = map splitLine (lines file)
        common = findCommon input
        p1     = part1 common
        p2     = part2 input common
    print p1
    print p2

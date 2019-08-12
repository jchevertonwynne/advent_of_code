type Frame = [Segment]

type Segment = [Section]

data Section = F Frame | C Char deriving Show

processInput :: String -> Frame
processInput s = 
    let frame = [[]]
    in processFrame s frame [frame]

processFrame :: String -> Frame -> [Frame] -> Frame
processFrame (h:t) f fl
    | null t = nf
    | otherwise = processFrame' t 
    where
        (nf, nfl) = processFrame' h f fl

processFrame' :: Char -> Frame -> [Frame] -> (Frame, [Frame])
processFrame' c f@(hf, tf) fl@(hfl, tfl)
    | c == '|' = (f, tfl)
    | c == '(' = 
    | c == ')' =
    | any (\l => l == c) "NESW" = 
    | otherwise = 
    where


main :: IO()
main = do
    file <- readFile "../../input/input_day20.txt"
    let frames = processInput file
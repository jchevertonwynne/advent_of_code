import strutils

const d = readFile("../../input/input_day20.txt")

type
    FrameTile = char
    FrameValues = Frame
    Frame = seq[FrameSequence]
    FrameSequence = seq[FrameTile|FrameValues]
    
var frame: Frame
echo $frame

# proc generate(regex: string): Frame =
#     var frames = @[result]
#     for c in regex:
#         if "^$".contains(c):
#             continue
#         elif "NESW".contains(c):
#             let n = FrameObject(kind: FrameTile, tile: c)
#             frames[^1][^1].add(n)
#         elif c == '(':
#             let n = FrameObject(kind: FrameValues)
#             frames[^1][^1].add(n)
#             frames.add(n)
#         elif c == '|':
#             let n = FrameObject(kind: FrameValues)
#             frames[^1].add(n)
#         elif c == ')':
#             discard frames.pop()

# echo generate("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$")
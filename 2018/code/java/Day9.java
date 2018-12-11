import java.util.HashMap;

public class Day9{
    public class Board{
        private class Node{
            public int value;
            public Node left;
            public Node right;
            public Node(int val) {
                value = val;
                left = null;
                right = null;
            }
        }

        private Node base;

        public Board() {
            Node start = new Node(0);
            start.right = start;
            start.left = start;
            base = start;
        }

        public void addNode(int val) {
            Node adding = new Node(val);
            adding.left = base.left;
            adding.right = base;
            base.left.right = adding;
            base.left = adding;
            base = adding;
        }

        public int deleteNode() {
            int value = base.value;
            base.left.right = base.right;
            base.right.left = base.left;
            base = base.right;
            return value;
        }

        public void clockwise(int nums) {
            for (int i = 0; i < nums; i++) {
                base = base.right;
            }
        }

        public void anticlockwise(int nums) {
            for (int i = 0; i < nums; i++) {
                base = base.left;
            }
        }
    }

    public Day9(int maxPlayers, int maxMarble) {
        long start = System.currentTimeMillis();
        Board game = new Board();
        HashMap<Integer, Double> scores = new HashMap<>();

        for (int marble = 1; marble < maxMarble; marble++) {
            if (marble % 23 == 0) {
                game.anticlockwise(7);
                int value = game.deleteNode();
                int scoring = marble % maxPlayers;
                double curr = scores.getOrDefault(scoring, (double)0);
                scores.put(scoring, curr + marble + value);
            }
            else {
                game.clockwise(2);
                game.addNode(marble);
            }
        }

        double highest = 0;
        double temp;

        for (int player: scores.keySet()) {
            temp = scores.get(player);
            if (temp > highest) {
                highest = temp;
            }
        }

        long end = System.currentTimeMillis();
        System.out.println(String.format("highest score: %.0f" ,highest));
        System.out.println(String.format("game was played in %1$d milliseconds", end - start));
    }
    public static void main(String[] args) {
        Day9 test = new Day9(9, 32);
        Day9 part1 = new Day9(411, 71058);
        Day9 part2 = new Day9(411, 71058 * 100);

    }
}

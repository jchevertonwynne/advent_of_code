import java.util.HashMap;
import java.util.Map;
import java.util.Collections;
import java.util.LinkedList;
 
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
            Node newNode = new Node(val);
            newNode.left = base.left;
            newNode.right = base;
            base.left.right = newNode;
            base.left = newNode;
            base = newNode;
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
        
        double highest = Collections.max(
                scores.entrySet(),
                Map.Entry.comparingByValue()
        ).getValue();
        
        long end = System.currentTimeMillis();
        System.out.println(String.format("highest score: %.0f" ,highest));
        System.out.println(String.format("game was played in %1$d milliseconds", end - start));
    }

    public static void main(String[] args) {
        new Day9(9, 32);
        new Day9(411, 71058);
        new Day9(411, 71058 * 100);
    }
}

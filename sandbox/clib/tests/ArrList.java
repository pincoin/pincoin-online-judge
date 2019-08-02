package tests;

import java.util.ArrayList;

public class ArrList {
    public static final int MAX  = 2000000;

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();

        for (int i = 0; i < MAX; i++) {
            a.add(i);
        }

        System.out.println(a.get(MAX-1));
    }
}

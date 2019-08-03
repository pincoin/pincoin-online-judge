package tests;

public class Arr {
    public static final int MAX = 20000000;

    public static void main(String[] args) {
        int[] a = new int[MAX];

        for (int i = 0; i < MAX; i++) {
            a[i] = i;
        }

        System.out.println(a[MAX-1]);
    }
}

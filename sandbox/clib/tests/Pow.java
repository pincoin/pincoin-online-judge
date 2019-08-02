package tests;

import java.util.Scanner;
import java.lang.Math;

public class Pow {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();
        System.out.println(Math.pow(a, b));
    }
}

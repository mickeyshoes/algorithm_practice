package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1436 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		int start = 666;
		while(true) {
			if (Integer.toString(start).contains("666")) {
				cnt+=1;
				if (cnt == N) break;
			}
			start+=1;
		}
		System.out.println(start);
	}

}

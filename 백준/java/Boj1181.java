package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Boj1181 {
	
	static int N;
	static Set<String> ary;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		ary = new HashSet<String>();
		for(int i=0; i<N; i++) {
			ary.add(br.readLine());
		}
		String[] arys = ary.toArray(new String[0]);
		Arrays.sort(arys);
		Arrays.sort(arys, (String i, String j) -> i.length() - j.length());
		
		for(String i : arys) {
			System.out.println(i);
		}
	}

}

package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Boj1874 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Set<Integer> ary = new HashSet<Integer>();
		String[] temp = br.readLine().split(" ");
		for(int i=0; i<N; i++) {
			ary.add(Integer.parseInt(temp[i]));
		}
		
		int M = Integer.parseInt(br.readLine());
		for(String a : br.readLine().split(" ")) {
			if(ary.add(Integer.parseInt(a))) 
				System.out.println(0);
			
			else
				System.out.println(1);
		}
	}

}

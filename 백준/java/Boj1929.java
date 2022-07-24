package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1929 {
		
	public static boolean isPrime(int target) {
		int limit = (int)Math.sqrt(target);
		if(target ==1) return false;
		for(int i=2; i<limit+1; i++) {
			if (target%i == 0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		String[] targets = br.readLine().split(" ");
		int start = Integer.parseInt(targets[0]);
		int end = Integer.parseInt(targets[1]);
		
		for(int i=start; i<end+1; i++) {
			if(isPrime(i))
				System.out.println(i);
		}
	}

}

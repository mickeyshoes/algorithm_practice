package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1018 {
	
	public static int M;
	public static int N;
	public static String[]map;
	
	public static int makePattern(int flag) {
		int binNumber = 0;
		for(int i=0; i<8; i++) {
			if((i+flag)%2 == 0)
				binNumber += (int)Math.pow(2,i);
		}
		return binNumber;
	}
	
	public static int convert2Binary(String sentence) {
		int result = 0;
		for(int i=0; i<sentence.length(); i++) {
			char c = sentence.charAt(i);
			if(c=='W')
				result+= (int)Math.pow(2, i);
		}
		return result;
	}
	
	public static int slidingWindow(int startRow, int startCol) {
		int[] answer = new int[2];
		//get array 8x8
		for(int r=startRow; r<startRow+8;r++) {
			String temp = "";
			for(int c=startCol; c<startCol+8; c++) {
				temp += map[r].charAt(c);
			}
			int binNumber = convert2Binary(temp);
			answer[0] += cntDiff(binNumber, makePattern(r%2));
			answer[1] += cntDiff(binNumber, makePattern((r+1)%2));
		}
		
		return Math.min(answer[0], answer[1]);
	}
	
	public static int cntDiff(int original, int pattern) {
		String temp = Integer.toBinaryString(original^pattern);
		return Integer.bitCount(Integer.parseInt(temp,2));
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		M = Integer.parseInt(input[0]);
		N = Integer.parseInt(input[1]);
		map = new String[M];
		
		for(int i=0; i<M; i++) {
			map[i] = br.readLine();
		}
		
		int answer = 64;
		for(int i=0; i<M-7; i++) {
			for(int j=0; j<N-7; j++) {
				answer = Math.min(answer, slidingWindow(i,j));
				
			}
		}
		
		System.out.println(answer);
						
	}

}

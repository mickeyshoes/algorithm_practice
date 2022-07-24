package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Boj1874 {
	
	static int N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		int[] targetAry = new int[N];
		for(int i=0; i<N; i++) {
			targetAry[i] = Integer.parseInt(br.readLine());
			
		}
		Stack<Integer> inputStack = new Stack<Integer>();

		int targetIdx = 0;
		StringBuilder sb = new StringBuilder();
		boolean flag = false;
		for(int i=1; i<N+1; i++) {
			// 값 추가
			inputStack.add(i);
			sb.append("+").append("\n");

			// 목표물이 있는경우 ->while로 돌아야 계속
			while(inputStack.size()>0 && targetAry[targetIdx] == inputStack.peek()) {
				inputStack.pop();
				sb.append("-").append("\n");
				targetIdx+=1;
			}
			
			// 스택으로 만들 수 없는 값인경우
			if(i==N && inputStack.size()>0)
				flag = true;
			
		}
		
		if (flag)
			System.out.println("NO");
		else {
			System.out.println(sb);
		}
		

	}

}

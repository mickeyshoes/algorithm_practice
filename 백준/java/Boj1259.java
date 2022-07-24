package com.ssafy.class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1259 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String check = br.readLine();
			if (check.equals("0")) break;
			StringBuffer sb = new StringBuffer(check);
			String check2 = sb.reverse().toString();
			
			if(check.equals(check2))
				System.out.println("yes");
			
			else
				System.out.println("no");
			
			
		}
	}

}

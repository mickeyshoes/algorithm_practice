import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj2615 {
	
	static String[][] map = new String[19][];
	static int[][] delta = {{1,0},{0,1},{1,1},{-1,1}};
	
	static boolean isRange(int x, int y) {
		return 0<=x && x<19 && 0<=y && y<19;
	}
	
	static int getCount(int x, int y, String type, int d) {
		int count = 1;
		int nx = x;
		int ny = y;
		
		for(int i=0; i<4; i++) {
			nx += delta[d][0]; ny += delta[d][1];
			if(isRange(nx,ny) && map[nx][ny].equals(type))
				count+=1;
		}
		
		if(isRange(x-delta[d][0], y-delta[d][1]) && 
				map[x-delta[d][0]][y-delta[d][1]].equals(type))
			count = 0;
		if(isRange(nx+delta[d][0], ny+delta[d][1]) &&
				map[nx+delta[d][0]][ny+delta[d][1]].equals(type))
			count = 0;
		return count;
	}

	static boolean isAvail(int x, int y, String type) {
		for(int i=0; i<4; i++) {
			if(getCount(x,y,type,i)==5) {
				return true;
			}
		}
		return false;
	}
	
	static int[] getAnswer() {
		int[] answer = new int[3];
		for(int r=0; r<19; r++) {
			for(int c=0; c<19; c++) {
				if(!map[r][c].equals("0")) {
					if(isAvail(r,c, map[r][c])) {
						answer[0] = Integer.parseInt(map[r][c]);
						answer[1] = r;
						answer[2] = c;
						return answer;
					}
				}
			}
		}
		return answer;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int i=0; i<19; i++) {
			map[i] = br.readLine().split(" ");
		}
		int answer[] = getAnswer();
		
		if(answer[0] !=0) {
			System.out.println(answer[0]);
			System.out.printf("%d %d", answer[1]+1, answer[2]+1);
		}
		else
			System.out.println(0);

	}

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1244 {

	public static int N;
	public static String[] switchValue;
	
	public static boolean isRange(int x) {
		return 0<=x && x<N;
	}
	
	public static boolean isPalendrome(int start, int idx) {
//		System.out.println(start-idx+":"+switchValue[start-idx]+" "+start+idx+": "+switchValue[start+idx]);
		if(isRange(start-idx) && isRange(start+idx) 
				&& switchValue[start-idx].equals(switchValue[start+idx]))
			return true;
		
		return false;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		switchValue = br.readLine().split(" ");
		
		int M = Integer.parseInt(br.readLine());
		for(int i=0; i<M; i++) {
			String[] temp = br.readLine().split(" ");
			int sex = Integer.parseInt(temp[0]);
			int idx = Integer.parseInt(temp[1]);
			
			if(sex == 1) {
				for(int j=idx-1; j<N; j= j+idx) {
					switchValue[j] = switchValue[j].equals("0")? "1": "0";
				}
			}
			else if(sex == 2) {
				int switchCnt = 0;
				for(int j=1; j<idx; j++) {
					if(isPalendrome(idx-1, j))
						switchCnt+=1;
					else break;
				}
				switchValue[idx-1] = switchValue[idx-1].equals("0")? "1": "0";
				if(switchCnt>0) {
					for(int k=1; k<=switchCnt; k++) {
						switchValue[idx-1+k] = switchValue[idx-1+k].equals("0")? "1": "0";
						switchValue[idx-1-k] = switchValue[idx-1-k].equals("0")? "1": "0";
					}
				}
			}
		}
		int cnt =0;
		for(int i=0; i<switchValue.length; i++) {
			System.out.printf("%s ", switchValue[i]);
			cnt +=1;
			if(cnt%20 ==0)
				System.out.println();
		}
		

	}

}

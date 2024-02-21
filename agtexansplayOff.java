// title is not what its supposed to be according to the assignment because it was saying the name was to long


import java.util.Scanner;

public class agtexansplayOff{

	public static void main(String[] args){


		Scanner sc = new Scanner(System.in);
		System.out.println("How many games did the texans play?");

		int size = sc.nextInt();



		int[] TexanScore = new int[size];
		int[] OpponentScore = new int[size];

		int totalGames = 1;
		for(int i = 0; i < TexanScore.length; i++){
			System.out.println("What was the texans score in game " + totalGames + " ?");
			int Tscore = sc.nextInt();
			TexanScore[i] = Tscore;
			System.out.println("What was the Opponents Score in game " + totalGames + " ?");
			int OScore = sc.nextInt();
			OpponentScore[i] = OScore;

			totalGames++;
		}
		double winT = 0;
		int needed2Win = (size / 3) *2;
		for(int i = 0; i < TexanScore.length; i++){

			System.out.println("Texan: " + TexanScore[i]);
			System.out.println("Opponent: " + OpponentScore[i]);

			if(TexanScore[i] > OpponentScore[i]){
				System.out.println("The texans need to win " + (needed2Win -1) + " to out of " + (size -1) + " to go to the playoffs");
			size--;
			needed2Win--;
			winT++;

				if(needed2Win ==0){
				System.out.println("The Texans made it to the playoffs");
				}
			}

			else{
				System.out.println("The texans need to win " + (needed2Win) + " to out of " + (size -1) + " to go to the playoffs");
			size--;
			}


		}
		System.out.println("Winning percent is: " + ((winT/TexanScore.length)*100) + "%");

		int TW = 0, sumTW = 0, TL = 0, sumTL = 0;
		double averageTW  = 0, averageTL = 0;
		for(int i = 0; i < TexanScore.length; i++){
			if(TexanScore[i] > OpponentScore[i]){
				TW++;
				sumTW += TexanScore[i];
				averageTW = sumTW / TW;

			}
			else{
				TL++;
				sumTL += TexanScore[i];
				averageTL = sumTL /TL;
			}

		}
		System.out.println("Texans average scores (win): " + averageTW);
		System.out.println("Texans average scores (lost): " + averageTL);

		int OW = 0, sumOW = 0, OL = 0, sumOL = 0; // OW = OpponentWin, OL = OpponentLost
		double averageOW  = 0, averageOL = 0;
		for(int i = 0; i < TexanScore.length; i++){
			if(OpponentScore[i] > TexanScore[i]){
				OW++;
				sumOW += OpponentScore[i];
				averageOW = sumOW / OW;

			}
			else{
				OL++;
				sumOL += OpponentScore[i];
				averageOL = sumOL / OL;
			}

		}
		System.out.println("The opponents average scores (win): " + averageOW);
		System.out.println("The Opponents average scores (lost): " + averageOL);

		int lowest = TexanScore[0], lowestGame = 0; // lowest = lowest score
		for(int i = 0; i < TexanScore.length; i++){
			if(TexanScore[i] < lowest){
				lowest = TexanScore[i];
				lowestGame = i +1;
			}

		}

		System.out.println("Lowest Houston Texans score was " + lowest + " in the " + lowestGame + "th game");

		int Deficit = 0, highestDeficit = (OpponentScore[0] - TexanScore[0]), game = 0;
		for(int i = 0; i < TexanScore.length; i++){

			if(TexanScore[i] < OpponentScore[i] ){
				Deficit = OpponentScore[i] - TexanScore[i];
				game = i + 1;
				if(Deficit > highestDeficit){
					highestDeficit = Deficit;
				}
			}

		}


		System.out.println("Largest deficit was " + highestDeficit + " and occurred in the " + game + "nd game.");
	}


}
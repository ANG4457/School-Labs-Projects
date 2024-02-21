import java.util.Random;
	public class Coin
	{
		private String sideUp;

		public Coin()
		{
			toss();
		}

		public void toss()
		{
			Random rando = new Random();
			int val = rando.nextInt(2);
			if(val == 1)
			{
				sideUp = "heads";
			}
			else
			{
				sideUp = "tails";
			}
		}

		public String getSideUp()
		{
			return sideUp;
		}





	}



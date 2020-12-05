package tsss;
import java.util.Scanner;

class car{
	private String color;
	private int speed;
	
	car(){
		color="black";
		speed=0;
	}
	
	void color(String value) {
		color=value;
		}
	
	void speed(int value) {
		if(speed+value>200)
			speed=200;
		else if(speed+value<0)
			speed=0;
		else
			speed+=value;
	}
	
	String getcolor() {return color;}
	int getspeed() {return speed;}
}


public class tesss {
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		car car=new car();
		String color,c_color;
		int speed,c_speed;
		
		color=car.getcolor();
		speed=car.getspeed();
		
		System.out.printf("변경하고자하는 색상을 black,red,white 중에 입력하세요 : ");
		while(true){
			c_color=sc.nextLine();
			if (c_color.equals("black") || c_color.equals("red") || c_color.equals("white"))
			{
				car.color(c_color);
				break;
			}
			else
			{
				System.out.printf("다시입력하세요 : ");
			}
		}
		
		System.out.printf("변경하고자 하는 속도를 입력하세요 : ");
		c_speed=sc.nextInt();
		car.speed(c_speed);
		
		c_color=car.getcolor();
		c_speed=car.getspeed();
		
		if (color.equals(c_color)) {
			System.out.printf("색상이 변경되지 않았으며, 속도가 %d 에서 %d로 변경되었습니다.",speed,c_speed );
		}
		else
		System.out.printf("색상이 %s 에서 %s로 변경되었고, 속도가 %d 에서 %d로 변경되었습니다.",color,c_color,speed,c_speed);
	}
}

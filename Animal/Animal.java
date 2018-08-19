class M{
	public M(){
		Animal a = new Animal("dog","woof");
		a.getCry();
	}
}
public class Animal{
	private String type;
	private String cry;
	public Animal(String type,String cry){
		this.type = type;
		this.cry = cry;
	}
	public String getType(){
		return this.type;
	}
	public String getCry(){
		return this.cry;
	}
}


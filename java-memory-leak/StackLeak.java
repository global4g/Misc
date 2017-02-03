public class StackLeak {

  public static void main (String[] args) {
	int i = 0, j=0;
	Stack sleak = new Stack();

	for ( i = 0; i < 10000; i ++) {

		for ( j = 0; i < 20; j++) {
			sleak.push(Integer.toString(i));
		}

		for ( j = 0; i < 20; j++) {
			sleak.pop();		
		}

		if ( i % 100 == 0 ) {
      try {
         Thread.sleep(100);
      } catch(InterruptedException ex) {
          Thread.currentThread().interrupt();
      }

		}		 
	}	
  }
}

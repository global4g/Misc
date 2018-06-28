import java.util.Scanner;
import java.net.*;

class DomainName
{

	public static String getDomainName(String url) throws URISyntaxException {
	    URI uri = new URI(url);
	    String domain = uri.getHost();
	    return domain.startsWith("www.") ? domain.substring(4) : domain;
	}



    public static void main(String[]args) throws URISyntaxException, MalformedURLException
    {
    	//For capturing user input
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the String for check:");
        String string = scanner.nextLine();
	
	String decodedURL = java.net.URLDecoder.decode(string);
	System.out.println("Url decoder output: " + decodedURL);

	URL urlobject = new URL(decodedURL);
        String targetDomain=urlobject.getAuthority();
	System.out.println("Authority: " + targetDomain);
	


	URI uri = new URI(string);
	String host = uri.getHost();
        System.out.println("Host: " + host);
    }
}

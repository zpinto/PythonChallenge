import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.Color;
import java.util.ArrayList;
import java.util.List;
/**
 * Write a description of class PictureTester here.
 * 
 * @author Zachary Pinto 
 * @version v1.0
 */
public class PictureTester
{
    public static void main(String[] args)
    {
        String thing = "";
        BufferedImage image = null;
        try{
            image = ImageIO.read(new File("gradient.png"));
        }
        catch(IOException e)
        {
            System.out.println("error");
        }
        int r=0,g=0,b=0;
        int w = image.getWidth();
        int h = image.getHeight();
        System.out.println("Image Dimension: Height-" + h + ", Width-"+ w);
        int total_pixels=(h * w);
        boolean add = true;
        String cha = "";
        //ArrayList <Color> arr = new ArrayList<Color>();
        for(int x=0;x<608;x++)
        {
                int rgb = image.getRGB(x, 1);
                Color c = new Color(rgb);
                add = true;
                cha = "" + (char)(c.getRed());
                /*for(int i = 0; i < thing.length(); i++)
                {
                    if(thing.contains(cha)){
                        add = false;
                    }
                }*/
                if(add)
                    thing += (char)(c.getRed());
                System.out.print("x: " + x + ": ");
                System.out.println(c);
        }
        System.out.println(thing);
        //answer: http://www.pythonchallenge.com/pc/def/integrity.html
        }
    }
